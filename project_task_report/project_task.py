# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
from openerp import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def get_project_info(self):
        projects = self.env['project.project'].search([])
        return projects.mapped(lambda self: (self.id, self.name))

    def get_task_recs(self, task_ids):
        tasks = self.env['project.task'].browse(task_ids)
        employees = tasks.mapped('user_id')
        stages = self.env['project.task.type'].search([('case_default', '=', True)])
        # Header
        res = list()
        res.append(['employee'])
        res[0] += ([st.name for st in stages])
        # Table's Body
        for employee in employees:
            res2 = dict()
            res2['employee'] = employee.name
            for stage in stages:
                res2[stage.name] = tasks.search_count(['&', ('user_id', '=', employee.id), ('stage_id', '=', stage.id)])
            res.append(res2)
        return res
