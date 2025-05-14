# EUVD Monitor & Exporter 🇩🇪

🇬🇧 [Read this in English](README.md)

Dieses Projekt ermöglicht es, über die öffentliche ENISA EU Vulnerability Database (EUVD) automatisierte Abfragen nach Schwachstellen für bestimmte Vendor-/Produkt-Kombinationen durchzuführen und die Ergebnisse in verschiedenen Formaten (JSON, CSV, HTML, XML) zu exportieren.

## 📦 Funktionen

- Zeitgesteuerte Abfrage (daily, weekly, monthly)
- Präzises Vendor-Produkt-Mapping
- Formatierte Ausgabe im Ordner `./output`
- Konvertierung in CSV, HTML und XML
- Keine Authentifizierung erforderlich (EUVD ist öffentlich)

⚠️ **Hinweis**: Die aktuelle EUVD-API behandelt `vendor` und `product`-Parameter als **ODER**, nicht als UND. Um präzise Ergebnisse zu erhalten, filtert dieses Tool nur gezielt vordefinierte Kombinationen aus der Konfigurationsdatei.
