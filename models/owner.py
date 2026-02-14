from odoo import models,fields,api

class owner(models.Model):
    _name = 'owner'
    _description = 'Property Owners'
    
    name= fields.Char(required=1, default="New", size=12)
    phone= fields.Char()
    address= fields.Text()

    property_ids= fields.One2many('estate.property', 'owner_id', string='Properties')