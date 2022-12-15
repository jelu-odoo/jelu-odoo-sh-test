from odoo import models, fields, api

class ProductTemplate(models.Model): 
    _inherit = 'product.template'
    
    product_group = fields.Many2one(comodel_name='matrix_systems.product_group',
                                    ondelete='cascade')

    @api.onchange('product_group')
    def _compute_barcode(self): 
        if self.product_group: 
            self.barcode = self.product_group.name[:2] + "." + self.product_group.reference_no[2:]