from odoo import api, models, fields
from PIL import Image
import io
import base64
import qrcode
import lnurl

class custom_info(models.Model):

    _inherit = 'hr.employee'
    employee_ln_address = fields.Char(string="Employee lightning address : ", required=False)
    employee_ln_qr_image = fields.Image(compute="_compute_ln_qr_image",string="Employee lightning QR code")


    @api.depends("image_1920","employee_ln_address")
    def _compute_ln_qr_image(self):
        for record in self:
            print('loading hr_employee records')
            print('image_1920:')
            print(record.image_1920)
            print('employee_ln_address')
            print(record.employee_ln_address)
            logo = Image.open(io.BytesIO(base64.b64decode(record.image_1920)))
            basewidth = 200
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            lnusr,lndomain = record.employee_ln_address.split('@')
            qrmessage = 'lightning:'+lnurl.encode('https://'+lndomain+'/.well-known/lnurlp/'+lnusr)
            QRcode.add_data(qrmessage)
            QRcode.make()
            QRcolor = 'Black'
            QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')# adding color to QR code
            pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
            QRimg.paste(logo, pos)
            QRinMem = io.BytesIO()
            QRimg.save(QRinMem,"JPEG")
            QRinMem.seek(0)
            record.employee_ln_qr_image=base64.b64encode(QRinMem.read())
