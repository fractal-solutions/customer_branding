from odoo import api, fields, models


class ResPartnerBrandLine(models.Model):
    _name = 'res.partner.brand.line'
    _description = 'Partner Joint Brand Name'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')
    name = fields.Char(string='Brand Name', required=True)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    branding_type = fields.Selection([
        ('default', 'Default (Usual Packaging)'),
        ('own', 'Own Brand'),
        ('joint', 'Joint Brand')
    ], string='Branding Type', default='default')

    brand_name = fields.Char(string='Brand Name')
    joint_brand_line_ids = fields.One2many(
        'res.partner.brand.line',
        'partner_id',
        string='Joint Brand Names',
    )

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cust_branding_type = fields.Selection(related='partner_id.branding_type', string='Customer Branding Type', readonly=False, store=True)
    cust_brand_name = fields.Char(related='partner_id.brand_name', string='Customer Brand Name', readonly=True, store=True)
    cust_joint_brand_names = fields.Char(
        string='Customer Joint Brand Names',
        compute='_compute_cust_joint_brand_names',
        store=True,
    )

    @api.depends('partner_id', 'partner_id.joint_brand_line_ids.name')
    def _compute_cust_joint_brand_names(self):
        for order in self:
            order.cust_joint_brand_names = ', '.join(
                order.partner_id.joint_brand_line_ids.mapped('name')
            )


