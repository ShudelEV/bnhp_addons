# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Project Entity',
    'version': '1.0.0',
    'category': 'Project Management',
    'sequence': 15,
    'summary': '',
    'description': """
Project Entity
==================
    """,
    'author':  'ShEV',
    'images': [],
    'depends': [
        'project',
    ],
    'data': [
        # 'report/project_report_view.xml',
        # 'security/ir.model.access.csv',
        'views/project_entity_view.xml',
        'views/project_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}