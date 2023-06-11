odoo.define('pos_hr.employees_custom', function (require) {
    "use strict";

var { PosGlobalState } = require('point_of_sale.models');
var Registries = require('point_of_sale.Registries');


const HrPosGlobalState = (PosGlobalState) => class HrPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
            await super._processData(...arguments);
            this.employee_ln_address = loadedData['hr.employee'].employee_ln_address;
            this.employee_ln_message = "lightning:" + this.employee_ln_address;
            this.employee_ln_qr_image = loadedData['hr.employee'].employee_ln_qr_image;
            const codeWriter = new window.ZXing.BrowserQRCodeSvgWriter();
            let qr_code_svg = new XMLSerializer().serializeToString(codeWriter.write(this.employee_ln_message, 150, 150));
            this.employee_ln_qr = "data:image/svg+xml;base64,"+ window.btoa(qr_code_svg);
        }
    }

Registries.Model.extend(PosGlobalState, HrPosGlobalState);});
