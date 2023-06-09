odoo.define('custom_pos_receipt.models', function(require) {
    "use strict";

    var { Order } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');

    const CustomOrder = (Order) => class CustomOrder extends Order {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
            result.employee_ln_address = this.pos.employee_ln_address;

	    console.log('inside CustomOrder.export_for_printing');
            console.log(this.pos.employee_ln_address);
            result.employee_ln_address_qr=this.pos.employee_ln_address_qr_base64;
            return result;
        }
    }
    Registries.Model.extend(Order, CustomOrder);
});
