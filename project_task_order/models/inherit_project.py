# -*- coding: utf-8 -*-
##############################################################################
# Sort project tasks by project sequence
##############################################################################
from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class ProjectTaskSort(models.TransientModel):
    _name = 'project.task.sort'
    # _description = 'Sort Tasks'

    @api.multi
    def change_seq_tasks(self):
        _logger.info("Start MY function")
        projects = self.env['project.project'].search([]).sorted(key=lambda r: r.sequence)
        tasks = self.env['project.task'].search([]).sorted(key=lambda r: r.sequence)
        stages = self.env['project.task.type'].search([]).mapped('id')
        _logger.info('stages = ' + str(stages))
        for stage in stages:
            i = 0
            _logger.info('    stage = ' + str(stage))
            for project in projects:
                these_tasks = tasks.search([('project_id', '=', project.id)]).mapped('id')
                for task in tasks:
                    if task.stage_id.id == stage and task.id in these_tasks:
                        # _logger.info('IN IF!!! i = ' + str(i))
                        task.write({'sequence': i})
                        i += 1
        return {'type': 'ir.actions.act_window_close'}