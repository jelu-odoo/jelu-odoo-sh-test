# -*- coding: utf-8 -*- 

from odoo import models, fields, api
from datetime import date

class ExpiredQuotationDeletion(models.Model): 
    _name = "expired_quotation_deletion"
    _description = "test description"
    
    def _remove_expired_quotations(self): 
        # get sales orders that are in 'draft'
        quotations = self.env['sale.order'].search([['state','=','draft'],
                                                    ['validity_date','!=',False],
                                                    ['validity_date','<',date.today()]])
        # check if the sale orders field "is_expired"
        for q in quotations: 
            # q.validity_date
            q.action_cancel()
            # non-empty, date value
                
        
            