# -*- coding: utf-8 -*-

{
    'name': 'Adding res.partner to Subscription & Invoice', 
    'summary': """
        Adding res.partner to Subscription & Invoice
    """, 
    'description': """
        Adding res.partner to Subscription & Invoice
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale_subscription', 'sale_management', 'sale'], 
    'data': [
        'views/subscription_edit.xml',
        
    ], 
    'demo': [
    ], 
}