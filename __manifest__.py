{
    'name': 'Customer Branding Labels',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Custom branding labels for customers',
    'description': """
        This module provides custom branding labels for customers.
    """,
    'depends': ['base', 'sale'],
    'data': [
        'views/customer_branding_views.xml',
    ],
    'installable': True,
    'application': True,
}