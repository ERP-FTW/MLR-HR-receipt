odoo.define('pos_hr.employees_custom', function (require) {
    "use strict";

var { PosGlobalState } = require('point_of_sale.models');
var Registries = require('point_of_sale.Registries');


const HrPosGlobalState = (PosGlobalState) => class HrPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
            await super._processData(...arguments);
            this.employee_ln_address = loadedData['hr.employee'].employee_ln_address;
            await this._loadLnQR(loadedData);
            console.log('this is called from custom posglobalstate');
            console.log(this.employee_ln_address);
            console.log('logging employee_ln_qr_image from LoadLnQR')
            console.log(this.employee_ln_address_qr_base64)
            console.log('logging employee_ln_qr_image from hr.employee');
            console.log(loadedData['hr.employee'].employee_ln_qr_image);
            this.employee_ln_address_qr_base64=this.employee_ln_address_qr_base64;
        }

    async _loadLnQR(loadedData) {
        this.employee_ln_address_qr = new Image();
        return new Promise((resolve, reject) => {
            this.employee_ln_address_qr.onload = () => {
                let img = this.employee_ln_address_qr;
                let ratio = 1;
                let targetwidth = 200;
                let maxheight = 200;
                if (img.width !== targetwidth) {
                    ratio = targetwidth / img.width;
                }
                if (img.height * ratio > maxheight) {
                    ratio = maxheight / img.height;
                }
                let width  = Math.floor(img.width * ratio);
                let height = Math.floor(img.height * ratio);
                let  c = document.createElement('canvas');
                c.width  = width;
                c.height = height;
                let ctx = c.getContext('2d');
                ctx.drawImage(this.employee_ln_address_qr,0,0, width, height);

                this.employee_ln_address_qr_base64 = c.toDataURL();
                resolve();
            };
            this.employee_ln_address_qr.onerror = () => {
                reject();
            };
            this.employee_ln_address_qr.crossOrigin = "anonymous";
            console.log('printing the user.id');
            console.log(this.user.id);
            this.employee_ln_address_qr.src = `/web/image?model=hr.employee&id=${loadedData['hr.employee'].id}&field=employee_ln_qr_image`;
        });

    }
}



Registries.Model.extend(PosGlobalState, HrPosGlobalState);});
