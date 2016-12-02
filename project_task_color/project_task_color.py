# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################

from openerp import models, fields, api


class ProjectTaskSetColor(models.Model):
    _inherit = 'project.task'

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        """
        Gets the associated project_id for the tasks and adds 'color' to the vals list
        """
        if 'project_id' in vals:
            project_obj = self.env['project.project']
            project = project_obj.browse(vals['project_id'])
            vals['color'] = project.color

        return super(ProjectTaskSetColor, self).create(vals)

    @api.multi
    def write(self, vals):
        """
        If there's a 'project_id', the function writes the 'color_id' in the vals to change the 'color_id'
         for every existing task which is associated to the project
        """
        project = vals.get('project_id')
        if project:
            project_obj = self.env['project.project']
            project = project_obj.browse(project)
            vals['color'] = project.color

        return super(ProjectTaskSetColor, self).write(vals)


class ProjectSetColor(models.Model):
    _inherit = 'project.project'

    @api.multi
    def write(self, vals):
        """
        Extends the write method to change the color of the associated tasks accordingly if the color is changed
        """
        color = vals.get('color')
        ids = self.ids if isinstance(self.ids, list) else [self.ids]
        tasks = self.env['project.task'].search([('project_id', 'in', ids)])
        for task in tasks:
            task.write({'color': color})

        return super(ProjectSetColor, self).write(vals)
