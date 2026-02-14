from odoo import models,fields,api

class Clinet(models.Model):
    _name = 'cus.client'
    
    _inherit = 'owner'
    