# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Recruitment Stages Preconditions',
    'version': '1.0',
    'category': 'Human Resources/Recruitment',
    'sequence': 90,
    'summary': 'Add preconditions to stages workflow',
    'description': "",
    'depends': [
        'hr_recruitment',
    ],
    'data': ['data/hr_recruitment_data.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
