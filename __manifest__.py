# -*- coding: utf-8 -*-
{
    'name': "peliculas",

    'summary': """
        modulo de administracion de peliculas """,

    'description': """
        modulo de administracion de peliculas
    """,

    'author': "Arturo Chavez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/presupuesto_views.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
