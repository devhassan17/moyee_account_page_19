# Moyee Account Page 19 (`moyee_account_page_19`)

Advanced portal management and custom account page for Moyee Coffee subscriptions on Odoo 19.

## Features

- **Soft Remove**: Move sale order lines to a 'removed' state with metadata instead of hard deleting.
- **Backend Visibility**: Removed lines are hidden from standard views but accessible to administrators.
- **Invoice Integration**: Automatically excludes zero-quantity or removed lines from invoices and PDF reports.
- **Portal Self-Service**:
    - Update delivery and billing addresses.
    - Postpone next delivery dates.
    - Add or remove products from active subscriptions.
    - Pause and resume subscriptions.
- **Multi-Company & Company Configuration Filter**:
    - Dynamic enablement/disablement per active company.
    - Company-level allowed filter configuration options in backend settings.

## Technical Details

- **Module Name**: `moyee_account_page_19`
- **Author**: Managemyweb.co
- **Maintainer**: ali@moyeecoffee.com
- **License**: LGPL-3
- **Odoo Version**: 19.0

## Installation

1. Install the module `moyee_account_page_19` from the Odoo Apps menu.
2. Ensure dependencies (`sale_management`, `sale_subscription`, `account`, `portal`, `website`) are installed.
3. Configure settings under **Moyee Portal > Configuration**.
4. Portal users will see the custom account page with subscription self-service controls.

---
© 2026 Managemyweb.co
