# -*- coding: utf-8 -*-

from openerp import models, fields


class ReportProjectTaskUser(models.Model):
    _inherit = "report.project.task.user"

    section_id = fields.Many2one('project.section', 'Section', readonly=True)
    phase_id = fields.Many2one('project.phases', 'Phase', readonly=True)

    def _select(self):
        return super(ReportProjectTaskUser, self)._select() + """,
            t.section_id,
            t.phase_id
            """

    def _group_by(self):
        return super(ReportProjectTaskUser, self)._group_by() + """,
            t.section_id,
            t.phase_id
            """