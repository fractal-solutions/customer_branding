from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    branding_type = fields.Selection([
        ('default', 'Default (Usual Packaging)'),
        ('own', 'Own Brand'),
        ('joint', 'Joint Brand')
    ], string='Branding Type', default='default')

    brand_name = fields.Char(string='Brand Name')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # 'related' makes Odoo pull the value from the customer automatically
    # 'readonly=False' allows salesperson to override it on a specific order if needed
    cust_branding_type = fields.Selection(related='partner_id.branding_type', string='Customer Branding Type', readonly=False, store=True)
    cust_brand_name = fields.Char(related='partner_id.brand_name', string='Customer Brand Name', readonly=False, store=True)