# Repository Contents - Cash Advance App

This repository contains the complete Cash Advance app with all related DocTypes and configurations.

## Complete File List

### App Structure Files
- `setup.py` - App setup and installation configuration
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `.gitignore` - Git ignore rules

### App Core Files
- `cash_advance/__init__.py` - App initialization
- `cash_advance/hooks.py` - App hooks and configuration
- `cash_advance/modules.txt` - Module definitions (Cash Advance)

### Module Configuration
- `cash_advance/cash_advance/__init__.py` - Module initialization
- `cash_advance/cash_advance/config/desktop.py` - Desktop icon configuration

### DocTypes

#### 1. Cash Advance Request (Main DocType)
- `cash_advance/doctype/cash_advance_request/__init__.py`
- `cash_advance/doctype/cash_advance_request/cash_advance_request.json` - DocType definition
- `cash_advance/doctype/cash_advance_request/cash_advance_request.py` - Python server logic
- `cash_advance/doctype/cash_advance_request/cash_advance_request.js` - JavaScript client logic

#### 2. Cash Advance Liquidation (Child Table DocType)
- `cash_advance/doctype/cash_advance_liquidation/__init__.py`
- `cash_advance/doctype/cash_advance_liquidation/cash_advance_liquidation.json` - Child table definition
- `cash_advance/doctype/cash_advance_liquidation/cash_advance_liquidation.py` - Python logic

## Total Files: 16

## App Information

- **App Name:** cash_advance
- **App Title:** Cash Advance
- **Module:** Cash Advance
- **DocTypes:** 
  - Cash Advance Request (Main)
  - Cash Advance Liquidation (Child Table)

## Installation

```bash
bench get-app https://github.com/atnharu-collab/cash-advance-app.git
bench --site [your-site] install-app cash_advance
bench --site [your-site] migrate
bench --site [your-site] clear-cache
```

## Repository URL

https://github.com/atnharu-collab/cash-advance-app
