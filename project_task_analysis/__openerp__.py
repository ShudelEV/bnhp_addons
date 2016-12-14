# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Project Task Analysis',
    'version': '1.0.0',
    'category': 'Project Management',
    'sequence': 15,
    'summary': '',
    'description': """
Project Task Analysis
=====================
Add fields: section, phase
    """,
    'author':  'ShEV',
    'images': [],
    'depends': [
        'project_section',
    ],
    'data': [
        'inherit_project_report_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}