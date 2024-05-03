from odoo import models, fields, api

class poject_mod(models.Model):
     
     _inherit = "project.project"
     
     

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(store=True)
     description = fields.Text()
     bishnu = fields.Char(string="bishnu")
     projecttime = fields.Integer(string="time")
     
