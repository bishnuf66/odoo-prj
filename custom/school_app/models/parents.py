from odoo import models, fields,api,_

class Parents (models.Model):
    
    _name = 'school.parents'
    _description = 'store information of parents'
    _rec_name = 'contact'
    
    
    name = fields.Char( string = "Parents name", tracking=True,required=True, website_form_blacklisted=False)
    contact =fields.Integer(string='Parents/Guardian Contact', tracking=True, website_form_blacklisted=True)
    address = fields.Char(string = "Address")
    gender = fields.Selection([('male','male'),('femlae','female'),('others','others')])
   

    def name_get(self):
        res=[]
        for rec in self:
            name=f'{rec.contact} - {rec.name}'
            res.append((rec.id,name))
        return res
