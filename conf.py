from odoo import models, fields
class myconf(models.Model):
    _name='legal.myconf'
    _description='lego'
    confname=fields.Char('ConfName' , Required=True)
    indexed=fields.Boolean('Indexed ?', Required=True)
    startdate=fields.Date('Start Date', Required=True)
    enddate=fields.Date('End Date', Required=True)    
    fee=fields.Float('Registration Fee', Required=True)
