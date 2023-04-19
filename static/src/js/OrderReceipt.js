/**@odoo-module */
import { PosGlobalState } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';
const HRPosGlobalState = (PosGlobalState) => class HRPosGlobalState extends PosGlobalState{
    async _processData(loadedData) {

    await super._processData(...arguments);
        this.employees = loadedData['hr.employee'];
        this.employee_by_id = loadedData['employee_by_id'];
        this.employee_ln_address = loadedData['employee_ln_address'];

        console.log(this.employees);
        var employee_ln_address = this.employees[0].employee_ln_address;
        console.log(employee_ln_address);


        this.employee_ln_address = loadedData['hr.employee'];
        //console.log(this.employee_ln_address);

//get_employee_ln_address() {
//    return this.employees[0].employee_ln_address;}
    }
}
Registries.Model.extend(PosGlobalState, HRPosGlobalState);