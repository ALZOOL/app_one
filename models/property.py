from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name= fields.Char(required=1, default="New", size=4)
    description= fields.Text(tracking=1)
    postcode= fields.Char(required=1)
    date_availability= fields.Date(default=fields.Date.today, copy=False, tracking= 1)
    expected_price= fields.Float(digits=(0,5))
    selling_price= fields.Float(readonly=1)
    diff = fields.Float(compute='_compute_diff')
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
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ],string='status',default='draft', copy=False)


    owner_id= fields.Many2one('owner', string='Owner')
    tag_ids= fields.Many2many('tag', string='Tags')

    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff= rec.expected_price - rec.selling_price


    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("Please Add A Valid Number!.")

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.state='draft'

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.state='pending'

    def action_sold(self):
        for rec in self:
            print("inside sold action")
            rec.state='sold'

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