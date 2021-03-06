# -*- coding: utf-8 -*-
##############################################################################
#   List of Project Sections
##############################################################################
from openerp import models, fields


class ProjectSectionList(models.Model):

    _name = 'project.section.list'
    _description = 'Catalog of Sections'
    _order = 'sequence'
    _rec_name = 'short_name'
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (long_name)', 'Long name must be unique.'),
        ('short_name_uniq', 'UNIQUE (short_name)', 'Short name must be unique.')
    ]

    long_name = fields.Char(string='Long Name', required=True, size=200)
    short_name = fields.Char(string='Short Name', required=True, size=50)
    sequence = fields.Integer('Sequence')