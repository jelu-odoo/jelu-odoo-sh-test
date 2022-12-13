# -*- coding: utf-8 -*- 

from odoo import models, fields, api

class expired_quotation_deletion(models.Model): 
    _name = "tvu.expired_quotation_deletion"
    _description = ""
    
    def _remove_expired_quotations(self): 
        # get sales orders that are in 'draft'
        quotations = self.env['sale.order'].search([['state','=','draft']])
        # check if the sale orders field "is_expired"
        for q in quotations: 
            q.action_cancel()
            # non-empty, date value
                
        
            