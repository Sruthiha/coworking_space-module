{
    'name': 'Coworking Space Management',
    'version': '1.0',
    'summary': 'Manage coworking spaces',
    'author': 'Your Name',
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/coworking_space_views.xml',
        'views/coworking_space_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
