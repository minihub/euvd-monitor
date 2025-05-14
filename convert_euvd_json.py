import json
import pandas as pd
from pathlib import Path
from collections import defaultdict

def flatten_euvd_data(json_path):
    with open(json_path, encoding="utf-8") as f:
        items = json.load(f)

    rows = []
    for entry in items:
        product_map = defaultdict(list)
        for p in entry.get("enisaIdProduct", []):
            name = p.get("product", {}).get("name", "").strip()
            version = p.get("product_version", "").strip()
            if name:
                product_map[name].append(version)

        product_strs = [
            f"{name}: {', '.join(v for v in versions if v)}"
            for name, versions in product_map.items()
        ]

        rows.append({
            "ID": entry.get("id"),
            "Published": entry.get("datePublished"),
            "Updated": entry.get("dateUpdated"),
            "CVSS Score": entry.get("baseScore"),
            "CVSS Version": entry.get("baseScoreVersion"),
            "CVSS Vector": entry.get("baseScoreVector"),
            "EPSS": entry.get("epss"),
            "CVE(s)": entry.get("aliases", "").strip().replace("\n", ", "),
            "Assigner": entry.get("assigner"),
            "Products": " | ".join(product_strs),
            "References": entry.get("references", "").replace("\n", " ").strip(),
            "Description": entry.get("description", "").replace("\n", " ").strip(),
        })

    return pd.DataFrame(rows)

def convert_to_formats(input_path):
    df = flatten_euvd_data(input_path)
    base = Path(input_path).with_suffix("")

    # CSV
    csv_file = base.with_suffix(".csv")
    df.to_csv(csv_file, index=False)
    print(f"✅ CSV gespeichert: {csv_file.name}")

    # HTML
    html_file = base.with_suffix(".html")
    df.to_html(html_file, index=False)
    print(f"✅ HTML gespeichert: {html_file.name}")

    # XML (optional)
    try:
        xml_file = base.with_suffix(".xml")
        xml_df = df.copy()
        xml_df.columns = [
            col.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
            for col in xml_df.columns
        ]
        xml_df.to_xml(xml_file, index=False, root_name="vulnerabilities", row_name="entry")
        print(f"✅ XML gespeichert: {xml_file.name}")
    except ImportError:
        print("⚠️  XML-Export nicht möglich: 'lxml' nicht installiert (empfohlen: pip install lxml)")
    except Exception as e:
        print(f"⚠️  XML-Export fehlgeschlagen: {e}")

def main():
    output_dir = Path("./output")
    json_files = list(output_dir.glob("*.json"))

    if not json_files:
        print("⚠️  Keine JSON-Dateien im 'output'-Verzeichnis gefunden.")
        return

    for json_file in json_files:
        print(f"\n🔄 Konvertiere Datei: {json_file.name}")
        convert_to_formats(json_file)

if __name__ == "__main__":
    main()