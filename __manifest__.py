# -*- coding: utf-8 -*-
{
    'name': "Módulo Legal",

    'summary': """
         Módulo Legal del ODOO""",

    'description': """
         Módulo Legal del ODOO
    """,

    'author': "Smasha",
    'website': "https://upload.wikimedia.org/wikipedia/commons/9/9e/Johnnysins.jpg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	    #'views/legalmenu.xml',
	    'views/reportequeja_view.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
    #],
}
