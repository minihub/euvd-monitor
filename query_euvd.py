import os
import time
import yaml
import json
import argparse
from datetime import date, timedelta, datetime
from urllib.parse import quote_plus
import requests
import calendar

def load_config(path='config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def determine_time_range(mode: str):
    today = date.today()
    if mode == 'daily':
        return today - timedelta(days=1), today
    elif mode == 'weekly':
        monday = today - timedelta(days=today.weekday())
        return monday, today
    elif mode == 'monthly':
        first_day = today.replace(day=1)
        return first_day, today
    else:
        return None, None

def fetch_vulnerabilities(api_url, vendor, product, from_date, to_date, query_cfg):
    all_results = []
    page = 0
    headers = {
        "User-Agent": "curl/8.0"
    }

    while True:
        params = {
            'vendor': vendor,
            'product': product,
            'fromDate': from_date.isoformat(),
            'toDate': to_date.isoformat(),
            'fromScore': query_cfg.get('from_score', 0),
            'toScore': query_cfg.get('to_score', 10),
            'fromEpss': query_cfg.get('from_epss', 0),
            'toEpss': query_cfg.get('to_epss', 100),
            'exploited': str(query_cfg.get('exploited', False)).lower(),
            'page': page,
            'size': query_cfg.get('page_size', 100),
        }

        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])
        total = data.get("total", 0)

        all_results.extend(items)
        print(f"  Page {page + 1}: {len(items)} entries loaded (total: {total})")

        if len(all_results) >= total or not items:
            break

        page += 1
        time.sleep(query_cfg.get('sleep_seconds', 1))
    return all_results

def get_output_filename(vendor, product, from_date, to_date, mode):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    base = f"{vendor}_{product}"

    if mode == "weekly":
        weeknum = from_date.isocalendar().week
        return f"{base}_Week{weeknum}_{timestamp}"
    elif mode == "monthly":
        monthname = calendar.month_name[from_date.month]
        return f"{base}_{monthname}_{timestamp}"
    else:
        return f"{base}_{from_date}_{to_date}"

def main():
    parser = argparse.ArgumentParser(description="EUVD Query Tool")
    parser.add_argument('--mode', choices=['daily', 'weekly', 'monthly'], help='Time range mode')
    parser.add_argument('--config', default='config.yaml', help='Path to configuration file')
    args = parser.parse_args()

    cfg = load_config(args.config)
    api_url = cfg['api']['url']
    query_cfg = cfg['query']
    out_dir = cfg['output']['folder']
    os.makedirs(out_dir, exist_ok=True)

    mode = args.mode
    if mode:
        from_date, to_date = determine_time_range(mode)
        if from_date is None:
            raise ValueError("Invalid time mode")
        query_cfg['time_ranges'] = [
            {'from': from_date.isoformat(), 'to': to_date.isoformat()}
        ]
    else:
        from_date = to_date = None  # fallback to manual range

    vendor_product_map = query_cfg['vendor_product_map']

    for vendor, products in vendor_product_map.items():
        for product in products:
            for tr in query_cfg['time_ranges']:
                from_str = tr['from']
                to_str = tr['to']
                from_d = date.fromisoformat(from_str)
                to_d = date.fromisoformat(to_str)

                print(f"\n🔍 Query: {vendor} / {product} ({from_str} → {to_str})")
                data = fetch_vulnerabilities(
                    api_url,
                    vendor,
                    product,
                    from_d,
                    to_d,
                    query_cfg
                )

                if not data:
                    print(f"⚠️  No entries for {vendor} / {product} → nothing saved.")
                    continue

                fname_base = get_output_filename(vendor, product, from_d, to_d, mode)
                json_path = os.path.join(out_dir, f"{fname_base}.json")

                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                print(f"✅ {len(data)} entries saved:")
                print(f"   - JSON: {json_path}")

if __name__ == '__main__':
    main()