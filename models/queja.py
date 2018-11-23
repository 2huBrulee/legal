from odoo import models, fields     
class Queja(models.Model): 
    _name = 'queja' 
    name = fields.Char('Descripcion', required=True) 
