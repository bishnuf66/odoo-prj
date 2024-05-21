from odoo import models, fields, api

class custommodel(models.Model):

     _inherit="product.product"
     _name="custom.products"
     _inherits = {'product.template': 'product_tmpl_id'}
     _inherit = ['mail.thread', 'mail.activity.mixin']
     
     
     name=fields.Char(string="bishnu name")
