# # -*- coding: utf-8 -*-
# # Part of Odoo. See LICENSE file for full copyright and licensing details.
# # Copyright (C) 2004-2008 PC Solutions (<http://pcsol.be>). All Rights Reserved
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_hr_employee(self):
        return {
            'search_params': {
                'domain': [('user_id', '=', self.env.user.id)],
                'fields': ['employee_ln_address','employee_ln_qr_image'],
            },
        }

    def _get_pos_ui_hr_employee(self, params):
        result = super()._pos_ui_models_to_load()
        employee = self.env['hr.employee'].search_read(**params['search_params'])[0]
        return employee

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        new_models_to_load = ['hr.employee']
        result.extend(new_models_to_load)
        return result
