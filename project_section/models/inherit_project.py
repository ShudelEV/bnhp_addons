# -*- coding: utf-8 -*-
##############################################################################
#   Add Project Section by Project
##############################################################################
from openerp import models, fields, api

class ProjectProject(models.Model):

    _inherit = 'project.project'

    section_line = fields.One2many('project.section', 'project_id',
                                   string='Section', copy=True)
    profit = fields.Monetary(string='Profitability', store=True,
                             readonly=True, compute='_amount_profit',
                             help='Profitability = (Total_Estimate_Cost - Total_Internal_Cost) / Total_Estimate_Cost')

    # Подсчет полных трудозатрат и стоимости
    @api.depends('section_line')
    def _amount_profit(self):
        for project in self:
            total_estimate_cost = total_internal_cost = 0.0

            for section in project.section_line:
                total_estimate_cost += section.planned_cost
                total_internal_cost += section.planned_cost_int

            if total_estimate_cost:
                project.update({
                    'profit': project.currency_id.round( \
                        (total_estimate_cost - total_internal_cost) / total_estimate_cost
                    ),
                })

    # amount_total_labor = fields.Monetary(string='Total Estimate Laboriousness', store=True,
    #                                   readonly=True, compute='_amount_all')
    # amount_total_cost = fields.Monetary(string='Total Estimate Cost', store=True,
    #                                   readonly=True, compute='_amount_all')
