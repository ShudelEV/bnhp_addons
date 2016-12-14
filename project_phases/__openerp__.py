# -*- coding: utf-8 -*-
{
    'name': "Project Phases",

    'summary': """Add phases to the Project and to the Tasks""",

    'description': """Setting up phases for Projects and Tasks""",

    'author': "padznich",
    'website': "softin.cloud",
    'category': 'Project extend',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/catalog_phases_view.xml',
        'views/project_phases_view.xml',
        'views/task_phase_view.xml',
        'views/phases_catalog_data.xml',
        # 'report/inherit_project_report_view.xml',
    ],
}