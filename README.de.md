# EUVD Monitor & Exporter 🇩🇪

🇬🇧 [Read this in English](README.md)

Dieses Projekt ermöglicht automatisierte Abfragen der öffentlichen ENISA EU Vulnerability Database (EUVD) und wandelt die Ergebnisse in verschiedene Formate um.

## 📦 Funktionen

- Zeitgesteuerte Abfragen: daily, weekly, monthly  
- Konfigurierbares Vendor-Produkt-Mapping  
- Abfragefilter für Score, EPSS und Exploited-Status  
- Ausgabe in JSON + Konvertierung nach CSV, HTML, XML  
- Zeitbasierte Dateinamen für einfache Archivierung  

⚠️ **Hinweis zur API**  
Die aktuelle EUVD-API behandelt `vendor` und `product`-Parameter als **ODER**, nicht als UND.  
Dieses Tool kompensiert das, indem es gezielt nach definierten Kombinationen sucht.

## 🛠️ Setup

```bash
git clone https://github.com/minihub/euvd-monitor.git
cd euvd-monitor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Verwendung

```bash
python query_euvd.py --mode monthly
```

Die Ergebnisse landen im `output/`-Verzeichnis.

## 🔄 Konvertierung

```bash
python convert_euvd_json.py
```

Wandelt alle JSON-Dateien in `output/` in `.csv`, `.html`, `.xml`.

## 🗂️ Konfiguration

Die Datei `config.yaml` enthält:

- API-URL
- Vendor/Produkt-Mapping
- Filter für Score, EPSS, etc.
