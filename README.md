# EUVD Monitor & Exporter 🇬🇧

🇩🇪 [Diese Seite auf Deutsch lesen](README.de.md)

This project enables automated queries against the public ENISA EU Vulnerability Database (EUVD) for selected vendor/product combinations and exports results in various formats (JSON, CSV, HTML, XML).

## 📦 Features

- Scheduled queries (daily, weekly, monthly)
- Precise vendor-product mapping
- Formatted output in `./output` folder
- Conversion to CSV, HTML and XML
- No authentication required (EUVD is public)

⚠️ **Note**: The current EUVD API treats `vendor` and `product` parameters as **OR**, not AND. To ensure precise results, this tool filters only explicitly defined combinations from the config file.
