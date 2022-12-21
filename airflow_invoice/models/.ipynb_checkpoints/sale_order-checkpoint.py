from odoo import models, fields, api


class SaleOrder(models.Model): 
    _inherit = 'sale.order'
    
    project_manager = fields.Many2one(comodel_name='res.partner', 
                                     string='Project Manager')
    
    project_name = fields.Many2one(comodel_name='res.partner', 
                                   string='Project Name')
    
    def _prepare_invoice(self): 
        so = super(SaleOrder, self)._prepare_invoice()
        so['project_manager'] = self.project_manager
        so['project_name'] = self.project_name
        
        # _logger.info(a.search_read([]))
        # _logger.info(type(a))
        return so