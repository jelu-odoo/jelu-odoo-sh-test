from odoo import models, fields, api

class ScheduledApprovalForRFQ(models.Model): 
    _name = "scheduled_approval_for_rfq"
    _description = "to automatically confirm rfqs into purchase orders"
    
    def _approve_rfqs(self): 
        # get rfqs with a specific vendor id, this is id 9. 
        # mindesa specification would be ['partner_id.id','=','1'] instead
        rfqs = self.env['purchase.order'].search([['partner_id.id','=','9']])
        
        for rfq in rfqs: 
            rfq.button_confirm()
