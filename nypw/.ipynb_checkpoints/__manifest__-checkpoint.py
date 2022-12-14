# -*- coding: utf-8 -*-

{
    'name': 'Auto Calculated Price', 
    'summary': """Adds two fields to product template, with restrictions""", 
    'description': """
         NY P&W Shoes : Auto-calculated price
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'license': 'OPL-1',
    'version': '0.1', 
    'depends': ['sale', ], 
    'data': [
        'views/product_template_view.xml',
        
    ], 
    'demo': [
    ], 
}