from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    name= fields.Char(required=1, default="New", size=4)
    description= fields.Text()
    postcode= fields.Char(required=1)
    date_availability= fields.Date(default=fields.Date.today, copy=False)
    expected_price= fields.Float(digits=(0,5))
    selling_price= fields.Float(readonly=1)
    bedrooms= fields.Integer(default=2, copy=False)
    living_area= fields.Integer()
    facades= fields.Integer()
    garage= fields.Boolean()
    garden= fields.Boolean()
    garden_area= fields.Integer()
    garden_orientation= fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),        
    ], default='north')
    active= fields.Boolean(default=True)
    state= fields.Selection([
        ('new','New'),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled'),        
    ],string='status',default='new', copy=False, required=True)


    owner_id= fields.Many2one('owner', string='Owner')
    tag_ids= fields.Many2many('tag', string='Tags')

    
    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("Please Add A Valid Number!.")



    @api.model_create_multi
    def create(self, vals):
        res= super(Property, self).create(vals)
        print("isnide create method")
        return res

    @api.model 
    def _search(self, domain, offset=0, limit=None, order=None):
        res = super(Property, self)._search(domain, offset=offset, limit=limit, order=order)
        print("isnide search method")
        return res
    
    def write(self, vals):
        res= super(Property, self).write(vals)
        print("isnide write method")
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("isnide unlink method")
        return res