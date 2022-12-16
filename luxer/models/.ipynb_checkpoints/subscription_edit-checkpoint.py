from odoo import models, fields, api
import logging

_logger = logging.getLogger("sale_order.py")


class SaleOrder(models.Model): 
    # _name = "luxer.subscription_edit"
    # _description = "Adding res.partner field to Subscription"
    _inherit = 'sale.order'
    
    product_partner = fields.Many2one(comodel_name='res.partner', 
                                      help='Subscription services can be delivered to an alternative customer/address with this field.')
    
            
    def _create_invoices(self): 
        so = super(SaleOrder, self)._create_invoices()
        so['product_partner'] = self.product_partner
        
        # _logger.info(a.search_read([]))
        # _logger.info(type(a))
        return so
    
    @api.onchange('product_partner')
    def _compute_partner_shipping_id(self):
        # so = super(SaleOrder, self)._prepare_invoice()
        
        for order in self: 
            _logger.info(order.product_partner.address_get(['delivery'])['delivery'])
            order.partner_shipping_id = order.product_partner.address_get(['delivery'])['delivery'] if order.product_partner else order.partner_id.address_get(['delivery'])['delivery']

            
class AccountMove(models.Model): 
    _inherit = 'account.move'
    
    product_partner = fields.Many2one(comodel_name='res.partner',
                                      help='yea')
    
# class SaleOrder(models.Model): 
#     _inherit = 'sale.order'
    
#     product_partner = fields.Many2one(comodel_name='res.partner', 
#                                       help='yea2')
    
#     def _prepare_invoice(self):
#         """
#         Prepare the dict of values to create the new invoice for a sales order. This method may be
#         overridden to implement custom invoice generation (making sure to call super() to establish
#         a clean extension chain).
#         """
# #         self.ensure_one()

# #         return {
# #             'ref': self.client_order_ref or '',
# #             'move_type': 'out_invoice',
# #             'narration': self.note,
# #             'currency_id': self.currency_id.id,
# #             'campaign_id': self.campaign_id.id,
# #             'medium_id': self.medium_id.id,
# #             'source_id': self.source_id.id,
# #             'team_id': self.team_id.id,
# #             'partner_id': self.partner_invoice_id.id,
# #             'partner_shipping_id': self.partner_shipping_id.id,
# #             'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id._get_fiscal_position(self.partner_invoice_id)).id,
# #             'invoice_origin': self.name,
# #             'invoice_payment_term_id': self.payment_term_id.id,
# #             'invoice_user_id': self.user_id.id,
# #             'payment_reference': self.reference,
# #             'transaction_ids': [Command.set(self.transaction_ids.ids)],
# #             'company_id': self.company_id.id,
# #             'invoice_line_ids': [],
# #         }
        
#         invoice_vals = super(SaleOrder, self)._prepare_invoice()
#         print(invoice_vals, "before")
#         invoice_vals['product_partner'] = self.product_partner
#         print(invoice_vals, "after")
#         return invoice_vals

#     def action_invoice_subscription(self): 
        
#         a = super(SaleOrder, self).action_invoice_subscription()
#         _logger.info(a)
#         if a['context']: 
#             a['context'].update({'product_partner': self.product_partner}) 
#         _logger.info(a)
#         _logger.info(type(a))
#         return a
        # print(a)
        
#     def _create_recurring_invoice(self):
#         a = super(SaleOrder, self)._create_recurring_invoice()
#         _logger.info(a.search_read([]))
#         _logger.info(type(a))
#         return a
    

