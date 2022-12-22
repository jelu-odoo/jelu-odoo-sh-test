# -*- coding: utf-8 -*-

{
    'name': 'Scheduled Action for RFQ Approval', 
    'summary': """
Scheduled Action for RFQ Approval""", 
    'description': """
        Scheduled Action for RFQ Approval
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'version': '0.1', 
    'depends': ['sale_management', 'purchase'], 
    'data': [
        'data/scheduled_approval_for_rfq.xml',
        
    ], 
    'demo': [
        'demo/res_partner_demo.xml',
        
    ], 
}