from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    customer = fields.Boolean(
        string='Customer',
    )