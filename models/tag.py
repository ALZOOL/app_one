from odoo import models,fields,api
from odoo.exceptions import ValidationError

class tag(models.Model):
    _name = 'tag'
    _description = 'Property Tags'

    name= fields.Char(required=1, default="New", size=12)
    