from odoo import models, fields, api, _
# import pdb

class TransferRequest(models.Model):
    _name = 'transfer.request'
    # _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Transfer Request'

    # def _get_default_state(self):
    #     state = self.env.ref('virtucent.stage1', raise_if_not_found=False)
    #     return state if state and state.id else False

    name = fields.Char(
        string='Reference',
        required=True,
        readonly=True,
    )

    stage_id = fields.Many2one(
        'crm.stage',
        string='Stages',
        # default=_get_default_state,
        default=lambda self: self.env.ref('virtucent.stage1'),
        group_expand='_read_group_stage_ids',
        # tracking=True,
        # ondelete='set null',
        readonly=True,
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        readonly=True,
    )

    sender_country_id = fields.Many2one(
        'res.currency',
        string='Send from',
        readonly=True,
    )

    recipient_country_id = fields.Many2one(
        'res.currency',
        string='Send to',
        readonly=True,
    )

    send_amount = fields.Monetary(
        string='Customer Send Amount',
        currency_field='sender_country_id',
        readonly=True,
    )

    recipient_get = fields.Monetary(
        string='Send to Recipient',
        compute='_compute_recipient_get',
        currency_field='recipient_country_id',
        readonly=True,
        store=True,
    )

    recipient_bank_acc_id = fields.Many2one(
        'res.partner.bank',
        string='Recipient Bank Account',
        readonly=True,
    )

    payment_proof = fields.Binary(
        string='Proof of Payment',
        readonly=True,
    )

    @api.depends('send_amount','sender_country_id','recipient_country_id')
    def _compute_recipient_get(self):
        for record in self:
            record.recipient_get = record.send_amount * record.recipient_country_id.rate

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('transfer.request')
        return super(TransferRequest, self).create(vals)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['crm.stage'].search([], order=order)

    def status_confirm(self):
        # pdb.set_trace()
        return self.write({'stage_id': self.env.ref('virtucent.stage2', raise_if_not_found=False)})
    
    def status_done(self):
        return self.write({'stage_id': self.env.ref('virtucent.stage3', raise_if_not_found=False)})