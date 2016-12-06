# -*- coding: utf-8 -*-
##############################################################################
#   Project Sections for Project Module
##############################################################################
from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProjectSection(models.Model):
    _name = 'project.section'
    _description = 'Project Sections'
    _rec_name = 'project_section_id'

    @api.one
    def _get_sections_list(self):
        # _logger.info("START _get_sections_list")
        project = self.project_id.id
        # _logger.info(str(project))
        sections = self.env['project.section'].search([('project_id', '=', project)])
        ids = []
        for rec in sections:
            ids.append(rec.project_section_id.id)
        # _logger.info(str(ids))
        return ids

    # не работает фильтр:

    @api.onchange('project_section_id')
    def _get_domain(self):
        # _logger.info("START _get_domain")
        ids = self._get_sections_list()[0]
        res = {'domain':{'project_section_id':[('id', 'not in', ids)]}}
        # _logger.info(str(ids))
        return res

    project_section_id = fields.Many2one('project.section.list',
                                         string='Section', ondelete='restrict', index=True, required=True)
    project_id = fields.Many2one('project.project', string='Project',
                                 required=True, ondelete='cascade')
    project_task_ids = fields.One2many('project.task', 'section_id',
                                       string='Task', copy='False')
    #monetary field, wage-rate/ставка
    # currency_id = fields.Many2one('res.currency', string='Currency')
    wage_rate = fields.Float('Rate',
                                # currency_field='currency_id',
                                help="Cost of this section")
    labor = fields.Float(digits=(6, 2), string="Laboriousness", help="Laboriousness of this section")
    planned_cost = fields.Float(string="Planned cost", compute='_taken_cost')

    @api.depends('wage_rate', 'labor')
    def _taken_cost(self):
        for record in self:
            record.planned_cost = record.wage_rate * record.labor
