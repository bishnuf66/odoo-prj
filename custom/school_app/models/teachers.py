from odoo import models, fields,api,_

class Teachers (models.Model):
    
    _name = 'school.teachers'
    _description = 'store information of parents'
    

    name = fields.Char( string = "Teachers name",help="please insert your name", required=True)
    binaryfield = fields.Binary(string="upload")
    
    binaryfilename=fields.Char(string="binaryfile")
    imagefield = fields.Image(string="upload imagge",max_width=200,max_height=200)
   
    mycurrency_id=fields.Many2one("res.currency",string="currency")
    salary=fields.Monetary(string="salary amount",currency_field="mycurrency_id")
    
    floatfield= fields.Float(digits="4" ,string="thi a fltfld")
    
    
     
    binarymultifield=fields.Many2many("ir.attachment",string="multi upload")
    
    
    
    
    
    @api.model
    def bishnu(self,arg1):
        pass       

    @api.model
    def bishnu1(self,arg1):
       pass
    
    @api.model
    def headerbtn(self,arg1):
        return{
            "name":"openwizard",
            "res_model":"create.appointment.wizard",
            "view_mode":"form",
            "target":"new",
            "type":"ir.actions.act_window"}
        
    
    @api.model
    def appointment(self,arg1):
        action = self.env.ref('school_app.action_create_appointment')
        return action


        