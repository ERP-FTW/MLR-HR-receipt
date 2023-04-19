odoo.define('pos_hr.employees', function (require) {
    "use strict";

var { PosGlobalState, Order } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const HrPosGlobalState = (PosGlobalState) => class HrPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
        await super._processData(...arguments);
        //if (this.config.module_mrl_hr_receipt) {
            this.employees = loadedData['hr.employee'];
            this.employee_by_id = loadedData['employee_by_id'];
            this.employee_ln_address = loadedData['employee_ln_address'];
            //}
        }


    //get_employee_ln_address() {
    //    return this.employee_ln_address;}
            }



Registries.Model.extend(PosGlobalState, HRPosGlobalState);});