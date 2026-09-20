{
    'name': 'Employee Portal Treasury Bridge',
    'version': '18.0.1.5.0',
    'summary': 'Connects Employee Portal Suite with Payment & Receipt Voucher treasury approvals and weekly cash plans.',
    'description': """
Technical integration bridge between Employee Portal Suite and Payment & Receipt Voucher.

The two main applications remain independent. When both are available, this bridge
installs automatically and adds authorized treasury functions to the Employee Portal.

Adds:
- CEO payment approvals and weekly cash plan access in the Employee Portal
- /my/employee/treasury/* portal routes
- Treasury dashboard cards and navigation links
    """,
    'license': 'LGPL-3',
    'author': 'Kinan',
    'category': 'Human Resources',
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': [
        'employee_portal_suite',
        'internal_transfer_voucher',
        'purchase',
    ],
    'data': [
        'views/treasury_templates.xml',
        'views/dashboard_extension.xml',
        'views/layout_extension.xml',
    ],
}
