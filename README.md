# EUVD Monitor & Exporter

Dieses Projekt ermöglicht es, über die öffentliche ENISA EU Vulnerability Database (EUVD) automatisierte Abfragen nach Schwachstellen für bestimmte Vendor-/Produkt-Kombinationen durchzuführen und die Ergebnisse in verschiedenen Formaten (JSON, CSV, HTML, XML) zu exportieren.

## 📦 Funktionen

- Zeitgesteuerte Abfrage (daily, weekly, monthly)
- Präzises Vendor-Produkt-Mapping
- Formatierte Ausgabe im Ordner `./output`
- Konvertierung in CSV, HTML und XML
- Keine Authentifizierung erforderlich (EUVD ist öffentlich)

⚠️ **Hinweis**: Die aktuelle EUVD-API behandelt `vendor` und `product`-Parameter als **ODER**, nicht als UND. Um präzise Ergebnisse zu erhalten, filtert dieses Tool nur gezielt vordefinierte Kombinationen aus der Konfigurationsdatei.

## 🚀 Setup & Nutzung

### 1. Klone das Repository

```bash
git clone https://github.com/minihub/euvd-monitor.git
cd euvd-monitor
```

### 2. Erstelle eine virtuelle Umgebung

```bash
python -m venv .venv
source .venv/bin/activate  # oder .venv\Scripts\activate unter Windows
```

### 3. Installiere Abhängigkeiten

```bash
pip install -r requirements.txt
```

### 4. JSON-Download ausführen

```bash
python query_euvd.py --mode monthly
```

### 5. Daten konvertieren

```bash
python convert_euvd_json.py
```

## 🛠 Konfiguration

Bearbeite `config.yaml`, um Vendoren, Produkte und Filter zu steuern. Beispiel:

```yaml
query:
  vendor_product_map:
    Cisco:
      - IOS
    F5:
      - BIG-IP
```

## 📂 Ausgabe

Alle Abfragen landen im `output/`-Verzeichnis als:

- `*.json` (Originaldaten)
- `*.csv` (tabellarisch)
- `*.html` (visuelle Ansicht)
- `*.xml` (strukturierter Export)

## 📋 Lizenz

MIT License – frei verwendbar mit Namensnennung.
