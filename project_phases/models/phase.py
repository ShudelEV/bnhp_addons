# -*- coding: utf-8 -*-

from datetime import datetime

from openerp import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP


class CatalogPhases(models.Model):

    _name = 'catalog.phases'
    _description = 'Catalog of Project Phases'

    name = fields.Char(required=True, string='Stage')
    description = fields.Char(string='Description')
    sequence = fields.Integer('Sequence')


class ProjectPhases(models.Model):

    _name = 'project.phases'
    _description = 'Project Phases'
    _rec_name = 'phase_id'

    phase_id = fields.Many2one('catalog.phases', string='Stage', ondelete='restrict')
    project_phase_line_id = fields.Many2one('project.project', string='Project', ondelete='cascade')
    date_contract = fields.Date(string='Date under the Сontract', help="Planing date for the Project Stage")
    currency_id = fields.Many2one('res.currency', string='Currency')
    revenue = fields.Monetary(string='Revenue', currency_field='currency_id', help="Cost of the Project Stage")
    project_manager = fields.Char(related='project_phase_line_id.user_id.name', string='Project Manager',
                                  store=True, readonly=True)
    date_accomplish = fields.Date(compute='_last_date', string='Actual Date')
    tasks_count = fields.Integer(compute='_last_date', string='Total of Tasks', readonly=True,
                                 help='Number of Initial Tasks in the Stage')
    tasks_completed = fields.Integer(compute='_last_date', string='Completed Tasks', readonly=True,
                                     help='Number of Completed Tasks in the Stage')
    accomplish = fields.Float(compute="_last_date", string='Accomplish', readonly=True,
                              help='')
    diff_days = fields.Integer(compute="_last_date", string='Differ Days', readonly=True, store=True)


    # @api.multi
    # def sq(self):
    #     sql = ('SELECT country_id, array_agg(id) '
    #            'FROM res_partner '
    #            'WHERE active=true AND country_id IS NOT NULL '
    #            'GROUP BY country_id')
    #     self.env.cr.execute(sql)
    #     country_model = self.env['res.country']
    #     result = {}
    #     for country_id, partner_ids in self.env.cr.fetchall():
    #         country = country_model.browse(country_id)
    #     partners = self.search(
    #         [('id', 'in', tuple(partner_ids))]
    #     )
    #     result[country] = partners
    #     return result

    @api.multi
    def _last_date(self):

        for pp in self:
            for project in pp.project_phase_line_id:
                last = None
                tasks_count = 0
                tasks_completed = 0
                for task in project.task_ids:
                    if pp.phase_id.name == task.phase_id.phase_id.name:
                        tasks_count += 1

                        if not last:
                            last = task.date_deadline
                        if last < task.date_deadline:
                            last = task.date_deadline

                        if task.stage_id.name == "Basic":
                            tasks_completed += 1

                try:
                    accomplish = float(tasks_completed) / float(tasks_count) * 100.0
                except TypeError:
                    accomplish = 0.0    # BAD CODE
                except ZeroDivisionError:
                    accomplish = 0.0

                diff_days = (datetime.strptime(last, DEFAULT_SERVER_DATETIME_FORMAT) - \
                             datetime.strptime(pp.date_contract, DEFAULT_SERVER_DATETIME_FORMAT)).days
                # diff_days = (datetime.strptime(last, "%Y-%m-%d") - datetime.strptime(pp.date_contract, "%Y-%m-%d")).days

                # pp.date_accomplish = datetime.strptime(last, "%Y-%m-%d").date()
                # pp.diff_days = diff_days
                # pp.tasks_count = tasks_count
                # pp.tasks_completed = tasks_completed
                # pp.accomplish = accomplish
                pp.write({
                    "diff_days": diff_days,
                    "task_count": tasks_count,
                    "date_accomplish": datetime.strptime(last, DEFAULT_SERVER_DATETIME_FORMAT).strftime(DEFAULT_SERVER_DATE_FORMAT),
                    "tasks_completed": tasks_completed,
                    "accomplish": accomplish,
                })


class ProjectProject(models.Model):

    _inherit = 'project.project'

    phase_line = fields.One2many('project.phases', 'project_phase_line_id', string='Project Stage Line', copy=True)
    amount_total_cost = fields.Monetary(compute='_amount_all', string='Total Revenue', store=True, readonly=True)

    @api.depends('phase_line')
    def _amount_all(self):
        for project in self:
            amount_total_cost = 0.0
            for phase in project.phase_line:
                amount_total_cost += phase.revenue

            project.update({
                'amount_total_cost': project.currency_id.round(amount_total_cost),
            })


class TaskPhase(models.Model):

    _inherit = 'project.task'

    phase_id = fields.Many2one('project.phases', string='Stage', help="Choose a Stage for the Task")
