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
    project_id = fields.Many2one('project.project', string='Project', required=True, ondelete='cascade')
    project_task_ids = fields.One2many('project.task', 'section_id', string='Task', copy='False')
    # currency_id = fields.Many2one('res.currency', string='Currency')

    labor = fields.Float(digits=(6, 2), string="Estimate Laboriousness",
                         help="Laboriousness of this Section according to the Estimate")
    wage_rate = fields.Float('Estimate Rate',
                                # currency_field='currency_id',
                                help="Cost according to the Estimate")
    planned_cost = fields.Float(string="Estimate Cost", compute='_take_cost')
    labor_int = fields.Float(digits=(6, 2), string="Internal Laboriousness",
                             help="Internal Laboriousness of this Section")
    wage_rate_int = fields.Float('Internal Rate',
                                # currency_field='currency_id',
                                help="Internal Cost of this Section")
    planned_cost_int = fields.Float(string="Internal Cost", compute='_take_cost')

    @api.depends('labor', 'wage_rate', 'labor_int', 'wage_rate_int')
    def _take_cost(self):
        for record in self:
            record.planned_cost = record.labor * record.wage_rate
            record.planned_cost_int = record.labor_int * record.wage_rate_int
