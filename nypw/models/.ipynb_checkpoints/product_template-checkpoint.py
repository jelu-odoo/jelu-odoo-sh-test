from odoo import models, fields, api

class ProductTemplate(models.Model): 
    _inherit = 'product.template'
    
    price_per_case = fields.Integer(string='Pairs of Shoes in Case',
                                       help='Enter an integer which is the number of pair of shoes in the case')
    
    price_per_pair = fields.Monetary(string='Price per pair',
                                     help='Enter a price for each pair of shoes')