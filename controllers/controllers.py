from odoo import http
from odoo.http import request
 
class Controller(http.Controller):

	@http.route('/', type='http', auth="public", website=True)
	def _get_country_list(self, **kw):
		return http.request.render("virtucent.virtucent_homepage", {
			'website1':request.env['website'].search([]),
			'website2':request.env['website'].search([]),
		})

	@http.route(['/submit'], type='http', auth="public", website=True)
	def transfer_request_submit(self, **post):
		return request.render("virtucent.transfer_request_submitted", {
			'request' : request.env['res.currency.rate'].create({
				'company_id' : request.website.company_id.id,
				'currency_id': int(post.get('recipient_country_id')),				
			}),
			'request' : request.env['transfer.request'].create({
	        	'partner_id' : request.env.user.partner_id.id,
	        	'sender_country_id' : int(post.get('sender_country_id')),
	        	'recipient_country_id' : int(post.get('recipient_country_id')),
	        	'send_amount': float(post.get('send_amount')),
	        	# 'recipient_get': post.get('recipient_get'),
        	})
		})

