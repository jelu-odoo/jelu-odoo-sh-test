# -*- coding: utf-8 -*-

{
    'name': 'TVU Cron', 
    'summary': """A Cron job to delete expired quotations""", 
    'description': """
         A cron job module
    """, 
    'author': 'Odoo',
    'website': 'https://www.odoo.com', 
    'category': 'Training',
    'license': 'OPL-1',
    'version': '0.1', 
    'depends': ['sale', ], 
    'data': [
        'data/cron_job.xml',
    ], 
    'demo': [
    ], 
}