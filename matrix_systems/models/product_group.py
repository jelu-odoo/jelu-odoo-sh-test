from odoo import models, fields, api

class ProductGroup(models.Model): 
    _name = 'matrix_systems.product_group'
    _description = 'for product group data'
    
    reference_no = fields.Char(string='Order Reference', required=True, readonly=True, default=lambda self: 'New')
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description') 
    
#     @api.onchange('product_group')
#     def _compute_barcode(self): 
#         if self.product_group:
#             for record in self: 
#                 self.barcode = self.product_group[:2] + "." + "therestofthebarcode"

    @api.model
    def create(self, vals):
        if vals.get('reference_no', 'New') == 'New':
            vals['reference_no'] = self.env['ir.sequence'].next_by_code('product_group.sequence') or 'New'
        res = super(ProductGroup, self).create(vals)
        return res