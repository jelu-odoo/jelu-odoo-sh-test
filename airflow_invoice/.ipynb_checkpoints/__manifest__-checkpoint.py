# -*- coding: utf-8 -*-

{
    'name': 'Invoice Editing', 
    'summary': """
Changes Invoice fields
    """, 
    'description': """
        Module that manages Invoice changing
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale_management', 
                'account', 
                'stock',
               ], 
    'data': [
        'report/report_invoice_inherit.xml',
        'views/account_view_form_inherit.xml',
        'views/sale_view_order_form_inherit.xml',
        
    ], 
    'demo': [
    ], 
}