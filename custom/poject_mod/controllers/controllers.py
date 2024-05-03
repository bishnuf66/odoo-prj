# -*- coding: utf-8 -*-
# from odoo import http


# class PojectMod(http.Controller):
#     @http.route('/poject_mod/poject_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/poject_mod/poject_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('poject_mod.listing', {
#             'root': '/poject_mod/poject_mod',
#             'objects': http.request.env['poject_mod.poject_mod'].search([]),
#         })

#     @http.route('/poject_mod/poject_mod/objects/<model("poject_mod.poject_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('poject_mod.object', {
#             'object': obj
#         })
