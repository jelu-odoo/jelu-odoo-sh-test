# -*- coding: utf-8 -*-

{
    'name': 'Matrix Systems : Sequential Number for Barcode', 
    'summary': """
        Matrix Systems : Sequential Number for Barcode
    """, 
    'description': """
        Matrix Systems : Sequential Number for Barcode
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale_management', 'sale'], 
    'data': [
        'security/matrix_systems_product_group_security.xml',
        'security/ir.model.access.csv',
        'data/pg_seq.xml',
        'views/addon.xml',
        'views/product_group.xml',
        'views/product_group_menuitems.xml',
        
    ], 
    'demo': [
        'demo/matrix_systems_demo.xml',
        
    ], 
}