# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Task Report',
    'version': '1.0.0',
    'category': 'Project Management',
    'sequence': 15,
    'summary': '',
    'description': """
Project Task Report
==================
    """,
    'author':  'ShEV',
    'images': [],
    'depends': [
        'project',
        'project_timesheet',
        'project_task_default_stage',
    ],
    'data': [
        'project_task_report.xml',
        'project_task_report2.xml',
    ],
    'installable': True,
}