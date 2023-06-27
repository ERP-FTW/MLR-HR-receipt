odoo.define('ln_pos_hr.models', function (require) {
    "use strict";

var { PosGlobalState, Order } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const LnPosPosGlobalState = (PosGlobalState) => class LnPosPosGlobalState extends PosGlobalState{
    async _processData(loadedData) {
        await super._processData(...arguments);
        console.log('logging from LnPosPosGlobalState')
        console.log(this.config.module_pos_hr)
        if (!this.config.module_pos_hr) {
            this.employees = loadedData['hr.employee'];
            if(this.employees[0] !== undefined) {
                console.log('this.employee passed')
                console.log(this.employees)
                this.user.employee_ln_address=this.employees[0].employee_ln_address;
                this.user.employee_ln_qr_image=this.employees[0].employee_ln_qr_image;
            }
        }
    }

    reset_cashier() {
        this.cashier = {name: null, id: null, barcode: null, user_id: null, pin: null, role: null, employee_ln_address: null, employee_ln_qr_image: null};
    }
}
Registries.Model.extend(PosGlobalState, LnPosPosGlobalState);

});
