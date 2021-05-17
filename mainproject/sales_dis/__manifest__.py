{
    'name': 'sales_dis',
    'version': '1.0',
    'category': 'Sales Distribution System',
    'sequence': 5,
    'summary': 'Sales Distribution System',
    'depends': ['base'],

    'description': """
            Module for Sales Distribution System
            """,

    'data' : [
        'security/ir.model.access.csv',
        'controller/templates.xml',
        'data/userdata.xml',
        'controller/design.xml'
    ],

    'application' : True

}