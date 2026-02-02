# Cash Advance App

A Frappe/ERPNext application for managing employee cash advance requests with liquidation tracking.

## Description

Cash Advance is a complete Frappe application designed for handling employee cash advance requests, including tracking requests, releases, liquidations, and refunds. This app includes the Cash Advance Request DocType and related components.

## App Information

- **App Name:** `cash_advance`
- **App Title:** Cash Advance
- **Module:** Cash Advance
- **DocType:** Cash Advance Request

## Features

- Employee cash advance request management
- Release tracking with date management
- Liquidation management with child table
- Refund and return handling
- Status tracking with reasons
- Integration with company, branch, and department structure
- Auto-calculation of totals (requested, liquidated, unliquidated)
- Desktop icon integration

## Installation

### Using Bench

1. **Clone or download this repository:**
   ```bash
   cd /path/to/your/bench
   bench get-app https://github.com/atnharu-collab/cash-advance-app.git
   ```

2. **Install the app:**
   ```bash
   bench --site [your-site] install-app cash_advance
   ```

3. **Migrate:**
   ```bash
   bench --site [your-site] migrate
   bench --site [your-site] clear-cache
   bench restart
   ```

### Manual Installation

1. **Copy the app to your bench:**
   ```bash
   cp -r cash_advance /path/to/your/bench/apps/
   ```

2. **Add to apps.txt:**
   ```bash
   echo "cash_advance" >> /path/to/your/bench/sites/apps.txt
   ```

3. **Install and migrate:**
   ```bash
   bench setup requirements
   bench --site [your-site] migrate
   bench --site [your-site] clear-cache
   ```

## App Structure

```
cash_advance/
├── setup.py                    # App setup configuration
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── cash_advance/
│   ├── __init__.py            # App initialization
│   ├── hooks.py               # App hooks and configuration
│   ├── modules.txt            # Module definitions
│   ├── cash_advance/          # Cash Advance module
│   │   ├── __init__.py
│   │   └── config/
│   │       └── desktop.py     # Desktop icon configuration
│   └── doctype/
│       └── cash_advance_request/
│           ├── __init__.py
│           ├── cash_advance_request.json
│           ├── cash_advance_request.py
│           └── cash_advance_request.js
```

## DocType Details

### Cash Advance Request

- **Name:** Cash Advance Request
- **Module:** Cash Advance
- **App:** cash_advance
- **Autoname Format:** CA.{#####}
- **Engine:** InnoDB

## Usage

1. Navigate to the Cash Advance section in your ERPNext desk
2. Create a new Cash Advance Request
3. Fill in the request details (company, branch, department, payee)
4. Add liquidation items in the child table
5. The system will automatically calculate totals
6. Track release dates and liquidation status

## Requirements

- Frappe Framework (v14+)
- ERPNext (optional, for accounting features)

## License

MIT

## Author

Developed for logistics management system.

## Repository

GitHub: https://github.com/atnharu-collab/cash-advance-app
