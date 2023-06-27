# # -*- coding: utf-8 -*-
# # Part of Odoo. See LICENSE file for full copyright and licensing details.
# # Copyright (C) 2004-2008 PC Solutions (<http://pcsol.be>). All Rights Reserved
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class PosSession(models.Model):
    _inherit = 'pos.session'


    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        new_model = 'hr.employee'
        if new_model not in result:
            result.append(new_model)
        return result

    def _loader_params_hr_employee(self):
        result= super()._loader_params_hr_employee()
        if not self.config_id.module_pos_hr:
            result['search_params']['domain']=[('user_id', '=', self.env.user.id)]
        result['search_params']['fields'].extend(['employee_ln_address', 'employee_ln_qr_image'])

        return result

    def _get_pos_ui_hr_employee(self, params):
        employees=super()._get_pos_ui_hr_employee(params)
  
        print('Calling from pos_session hr_employee')

        for employee in employees:
            print(type(employee))
            employee.compute_ln_qr_image()

        return employees
