from odoo import models, fields, api

class Book(models.Model):
    _name = "library.book"
    _discription= "Book"
    _order="name,date_pulished desc"
    _recname="name"
    _table="library_books"
    _log_access=True
    _auto=True


    name = fields.Char("ISBN")
    book_type =fields.Selection(
        [("paper","paperback"),
         ("hard","hardcover"),
         ("electrioic","Electronic"),
         ("other","Others")],
         "Type")
    notes = fields.Integer(default=1)
    descr = fields.Float("Average Rating",(3,2))
    price=fields.Monetary("price","current_id")



    currency_id = fields.Many2one("res.currency")

    date_published = fields.Date()
    last_burrow_date = fields.Datetime()(
        "last Burrowed on",
        default=lambda self: fields.Datetime.now())