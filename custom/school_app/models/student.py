from odoo import models, fields,api,_
from odoo.exceptions import ValidationError

class Student (models.Model):
    
    _name = 'school.student'
    _description = 'store information of students'
    _inherit = ['mail.thread']
    
    student_id = fields.Integer(string="ID", tracking=True) 
    name = fields.Char( string = "Student name", tracking=True)
    age = fields.Integer(string="age" ,tracking=True)
    is_child = fields.Boolean(string ="is child",tracking=True)
    class_id =  fields.Integer(string='Class', tracking=True)
    section_id = fields.Char(string="Section" ,tracking=True)
    guardian_contact =fields.Integer(string='Parents/Guardian Contact', tracking=True)
    address = fields.Char(string = "Address")
    gender = fields.Selection([('male','male'),('femlae','female'),('others','others')])
    capitalized_name = fields.Char(string='capitalised Name',compute="compute_field_name",store = True)
    ref = fields.Char(string="reference",default=lambda self:_('SN'))



    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref']=self.env["ir.sequence"].next_by_code('school.student')
            

        return super(Student,self).create(vals_list)
  

    
    
    @api.constrains('is_child','age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age==0:
                raise ValidationError(_("age can't be 0"))


    
    
    
    @api.depends('name')
    def compute_field_name(self):
        for rec in self:   
            if rec.name:
                rec.capitalized_name = rec.name.upper()

            else:
                rec.capitalized_name = ""


  

    @api.onchange('age')
    def onchange_age(self):
        if self.age <= 10:
            self.is_child = True

        else:
            self.is_child=False

