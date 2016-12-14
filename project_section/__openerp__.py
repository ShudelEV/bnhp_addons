# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Project Sections',
    'version': '1.0.0',
    'category': 'Project Management',
    'sequence': 15,
    'summary': '',
    'description': """
Project Sections
==================
Add project sections
    """,
    'author':  'ShEV',
    'images': [],
    'depends': [
        'project',
        'project_timesheet',
        'decimal_precision',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        # 'views/project_data.xml',
        'views/project_section_view.xml',
        'views/project_section_list_view.xml',
        'views/project_task_section_view.xml',
        # 'report/project_task_report_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}