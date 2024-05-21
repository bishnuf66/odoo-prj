# -*- coding: utf-8 -*-
# from odoo import http


# class Custommodel(http.Controller):
#     @http.route('/custommodel/custommodel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custommodel/custommodel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custommodel.listing', {
#             'root': '/custommodel/custommodel',
#             'objects': http.request.env['custommodel.custommodel'].search([]),
#         })

#     @http.route('/custommodel/custommodel/objects/<model("custommodel.custommodel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custommodel.object', {
#             'object': obj
#         })
