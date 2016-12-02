# -*- coding: utf-8 -*-
##############################################################################
# Change the order of projects
##############################################################################
from openerp import models, fields


class ProjectChangeOrder(models.Model):
    _inherit = 'project.project'
    _order = 'sequence, date, name'
