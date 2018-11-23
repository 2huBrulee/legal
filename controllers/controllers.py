# -*- coding: utf-8 -*-
from odoo import http

# class Legal(http.Controller):
#     @http.route('/legal/legal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legal/legal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('legal.listing', {
#             'root': '/legal/legal',
#             'objects': http.request.env['legal.legal'].search([]),
#         })

#     @http.route('/legal/legal/objects/<model("legal.legal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legal.object', {
#             'object': obj
#         })