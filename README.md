# EUVD Monitor & Exporter 🇬🇧

🇩🇪 [Diese Seite auf Deutsch lesen](README.de.md)

This tool automates queries against the public ENISA EU Vulnerability Database (EUVD) and converts the results into various formats.

## 📦 Features

- Scheduled queries: daily, weekly, monthly  
- Configurable vendor-product mapping  
- Filter by score, EPSS, exploited status  
- Output to JSON + conversion to CSV, HTML, XML  
- Timestamped filenames for easy archiving  

⚠️ **API Note**  
The current EUVD API treats `vendor` and `product` parameters as **OR**, not AND.  
This tool compensates by querying explicitly defined combinations only.

## 🛠️ Setup

```bash
git clone https://github.com/minihub/euvd-monitor.git
cd euvd-monitor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python query_euvd.py --mode monthly
```

Results will appear in the `output/` directory.

## 🔄 Conversion

```bash
python convert_euvd_json.py
```

Converts all JSON files in `output/` to `.csv`, `.html`, and `.xml`.

## 🗂️ Configuration

The `config.yaml` file includes:

- API URL
- Vendor/product mapping
- Filters for score, EPSS, etc.
