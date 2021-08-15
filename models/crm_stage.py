from odoo import fields, models, _

class Stage(models.Model):
    _name = 'crm.stage'
    _description = 'CRM Status'
    _sql_constraints = [('crm_state_name_unique', 'unique(name)', 'State name already exists')]

    name = fields.Char(
        required=True,
        translate=True
    )

    sequence = fields.Integer(
        help="Used to order the note stages",
    )
    transfer_request_line = fields.One2many(
        'transfer.request',
        'stage_id',
        string='Transfer Request',
    )
