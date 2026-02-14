from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    property_id= fields.Many2one('estate.property', string='Property')

    def action_confirm(self):
        res= super(SaleOrder, self).action_confirm()
        print("Sale Order Confirmed from App One Module")
        return res