from odoo import models, fields

class custom_info(models.Model):
    _inherit = 'hr.employee'

    employee_ln_address = fields.Char(string="Employee lightning address : ", required=False)
    employee_ln_qr_image = fields.Image(string="Employee lightning QR code")
