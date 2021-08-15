from odoo import models, fields, api
import requests

class CurrencyRate(models.Model):
    _inherit = 'res.currency.rate'
    _sql_constraints = [
        ('unique_name_per_day', 'CHECK(1=1)', 'Only one currency rate per day allowed!'),
        ('currency_rate_check', 'CHECK(1=1)', 'The currency rate must be strictly positive.'),
    ]

    rate = fields.Float(
        help='The rate of the currency to the currency of rate 1',
        compute='_compute_current_rate',
        store=True,
    )

    @api.depends('currency_id', 'company_id')
    def _compute_current_rate(self):
        for record in self:
            record.rate = float(requests.get('https://data.fixer.io/api/convert?access_key=59fbf81af567c668fc4694fb20a783ba&from={}&to={}&amount=1'.format(record.company_id.currency_id.name, record.currency_id.name)).json()['result'])
    