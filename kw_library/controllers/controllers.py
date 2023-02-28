# -*- coding: utf-8 -*-
# from odoo import http


# class KwLibrary(http.Controller):
#     @http.route('/kw_library/kw_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kw_library/kw_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kw_library.listing', {
#             'root': '/kw_library/kw_library',
#             'objects': http.request.env['kw_library.kw_library'].search([]),
#         })

#     @http.route('/kw_library/kw_library/objects/<model("kw_library.kw_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kw_library.object', {
#             'object': obj
#         })
