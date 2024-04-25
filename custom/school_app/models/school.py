from odoo import models, fields

class School(models.Model):
    
    _name = 'school.student'
    _description = 'store information of students'
    
    student_id = fields.Integer(string="ID")
    name = fields.Char( string = "Student name")
    class_id=  fields.Integer(string='Class')
    section_id = fields.Char(string="Section")
    guardian_contact =fields.Integer(string='Contact')
    address = fields.Char(string = "Address")
     