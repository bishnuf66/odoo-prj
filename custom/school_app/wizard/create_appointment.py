from odoo import models, fields,api,_

class CreateAppointmentWizard (models.TransientModel):
    
    _name = 'create.appointment.wizard'
    _description = 'create appointment waizard'


    name = fields.Char( string = "Student name", tracking=True)
  
