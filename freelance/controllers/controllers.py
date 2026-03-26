# -*- coding: utf-8 -*-
# from odoo import http


# class Freelance(http.Controller):
#     @http.route('/freelance/freelance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/freelance/freelance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('freelance.listing', {
#             'root': '/freelance/freelance',
#             'objects': http.request.env['freelance.freelance'].search([]),
#         })

#     @http.route('/freelance/freelance/objects/<model("freelance.freelance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('freelance.object', {
#             'object': obj
#         })

