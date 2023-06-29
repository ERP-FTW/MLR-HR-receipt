from odoo import api, models, fields
from PIL import Image
import io
import base64
import qrcode
import lnurl
import binascii

class custom_info(models.Model):

    _inherit = 'hr.employee'
    employee_ln_address = fields.Char(string="Employee lightning address : ", required=False)
    employee_ln_qr_image = fields.Image(compute="_compute_ln_qr_image",string="Employee lightning QR code")
    avatar_in_ln_qr = fields.Boolean(string="Display Avatar in Lightning QR?")

    def _compute_ln_qr_image(self):
        for record in self:
            record.employee_ln_qr_image=False
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            if record.employee_ln_address:
                lnusr,lndomain = record.employee_ln_address.split('@')
                qrmessage = 'lightning:'+lnurl.encode('https://'+lndomain+'/.well-known/lnurlp/'+lnusr)
                QRcode.add_data(qrmessage)
                QRcode.make()
                QRcolor = 'Black'
                QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')# adding color to QR code
                if record.image_1920 and record.avatar_in_ln_qr:
                    logo = Image.open(io.BytesIO(base64.b64decode(record.image_1920)))
                    basewidth = 200
                    wpercent = (basewidth/float(logo.size[0]))
                    hsize = int((float(logo.size[1])*float(wpercent)))
                    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
                    pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
                    QRimg.paste(logo, pos)
                QRinMem = io.BytesIO()
                QRimg.save(QRinMem,"JPEG")
                QRinMem.seek(0)
                record.employee_ln_qr_image=base64.b64encode(QRinMem.read())

    @api.onchange('employee_ln_address','avatar_in_ln_qr','image_1920')
    def onchange_ln_qr(self):
        self.employee_ln_qr_image=False
        if not self.avatar_in_ln_qr:
            return
        return {
               'warning': {'title': "Info", 'message': "You need to reload the page to vew the updated QR Code after the changes are saved"},
        }
