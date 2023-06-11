from odoo import api, models, fields
from PIL import Image
import io
import base64
import qrcode
import lnurl

class custom_info(models.Model):

    _inherit = 'hr.employee'
    employee_ln_address = fields.Char(string="Employee lightning address : ", default="sagar@zbd.gg")
    employee_ln_qr_image = fields.Image(compute="_generate_qr",string="Employee lightning QR Image")


    #@api.depends("image_1920","employee_ln_address")
    def _compute_ln_qr_image(self):
        for record in self:
            print('loading hr_employee records')
            #print('image_1920:')
            #print(record.image_1920)
            print('employee_ln_address')
            print(record.employee_ln_address)
            logo = Image.open(io.BytesIO(base64.b64decode(record.image_1920)))
            basewidth = 200
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            lnusr,lndomain = record.employee_ln_address.split('@')
            qrmessage = 'lightning:'+record.employee_ln_address
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

    def _generate_qr(self):  # called by compute field to change binary into QR
        for rec in self:
            if qrcode and base64:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    # use low error correction to keep QR less complex and small
                    box_size=8,
                    border=4,
                )
                qr.add_data(rec.employee_ln_address)
                qr.make(fit=True)
                img = qr.make_image()
                temp = io.BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                rec.update({'employee_ln_qr_image': qr_image})  # update the field with QR
            else:
                print('Necessary Requirements To Run This Operation Is Not Satisfied')
