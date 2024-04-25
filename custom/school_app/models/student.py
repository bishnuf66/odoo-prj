from odoo import models, fields

class Student (models.Model):
    
    _name = 'school.student'
    _description = 'store information of students'
    
    student_id = fields.Integer(string="ID", tracking=True) 
    name = fields.Char( string = "Students", tracking=True)
    age = fields.Integer(string="age" ,tracking=True)
    class_id =  fields.Integer(string='Class', tracking=True)
    section_id = fields.Char(string="Section" ,tracking=True)
    guardian_contact =fields.Integer(string='Contact', tracking=True)
    address = fields.Char(string = "Address")
    gender = fields.Selection([('male','male'),('femlae','female'),('others','others')])