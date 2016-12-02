# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProjectTaskAddDepartment(models.Model):
    _inherit = 'project.task'

    @api.model
    def _get_default_department(self):
        department_id = self.env['hr.department']
        for employee in self.env.user.employee_ids:
            if employee and employee.department_id:
                department_id = employee.department_id.id
                break
        return department_id

    department_id = fields.Many2one(
        comodel_name='hr.department',
        string='Department',
        default=_get_default_department,
    )

    # override onchange_user_id method
    @api.multi
    def onchange_user_id(self, user_id):
        department_id = self.search_user_department(user_id)
        if department_id:
            self.write({'department_id': department_id})
        else:
            self.write({'department_id': None})
        return super(ProjectTaskAddDepartment, self).onchange_user_id(user_id)

    @api.multi
    def search_user_department(self, user_id):
        for employee in self.env['res.users'].browse(user_id).employee_ids:
            if employee and employee.department_id:
                return employee.department_id.id
        # return 0 if employee doesn't have department
        return 0
