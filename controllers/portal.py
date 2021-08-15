from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager 

class transferRequestPortal(CustomerPortal):

	def _prepare_home_portal_values(self, counters):
		values = super()._prepare_home_portal_values(counters)
		partner = request.env.user.partner_id

		TransferRequest = request.env['transfer.request']
		if 'request_count' in counters:
			values['request_count'] = TransferRequest.search_count([
				('partner_id.id', '=', partner.id)
			]) if TransferRequest.check_access_rights('read', raise_exception=False) else 0

		return values

	@http.route(['/my/requests', '/my/requests/page/<int:page>'], type='http', auth="user", website=True)
	def portal_my_requests(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
		values = self._prepare_portal_layout_values()
		partner = request.env.user.partner_id
		TransferRequest = request.env['transfer.request']

		# domain = [
		# 	('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
		# 	('state', 'in', ['sent', 'cancel'])
		# ]

		# searchbar_sortings = {
		# 	'date': {'label': _('Order Date'), 'order': 'date_order desc'},
		# 	'name': {'label': _('Reference'), 'order': 'name'},
		# 	'stage': {'label': _('Stage'), 'order': 'state'},
		# }

		# # default sortby order
		# if not sortby:
		# 	sortby = 'date'
		# sort_order = searchbar_sortings[sortby]['order']

		# # if date_begin and date_end:
		# # 	domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

		# # count for pager
		# requests_count = TransferRequest.search_count(domain)
		# # make pager
		# pager = portal_pager(
		# 	url="/my/quotes",
		# 	url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
		# 	total=requests_count,
		# 	page=page,
		# 	step=self._items_per_page
		# )
		# # search the count to display, according to the pager data
		# quotations = TransferRequest.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
		# request.session['my_quotations_history'] = quotations.ids[:100]

		values.update({
			# 'date': date_begin,
			# 'quotations': quotations.sudo(),
			# 'page_name': 'quote',
			# 'pager': pager,
			# 'default_url': '/my/quotes',
			# 'searchbar_sortings': searchbar_sortings,
			# 'sortby': sortby,
			'requests' : request.env['transfer.request'].search([
				('partner_id.id', '=', partner.id)
			]),
		})
		
		return request.render("virtucent.portal_my_requests", values)