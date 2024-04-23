from odoo import fields,models

class Book(models.Model):
    _name = "library.book"
    _discription ="book"
    name =fields.Char("title", required=True)

    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published =  fields.Date()
    image = fields.Binary("cover")
    published_id =  fields.Many2one("res.partner",string="Publisher")
    author_ids = fields.Many2many("res.partner",string="Author")

    