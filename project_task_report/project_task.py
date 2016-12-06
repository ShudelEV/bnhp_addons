# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
from openerp import models, fields, api, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.multi
    def get_project_info(self):
        projects = self.env['project.project'].search([])
        return projects.mapped(lambda self: (self.id, self.name))