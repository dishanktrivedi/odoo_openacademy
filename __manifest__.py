{
    # Name of the module, will be shown in the Apps menu
    'name': 'Open Academy',
    'version': '1.0',
    'author': 'Dishank Trivedi',
    'category': 'Uncategorized',
    'summary': 'Courses for all category',
    'depends': ['base'],

    # List of XML files for views
    'data': [
        'demo/course_demo.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_inherit_views.xml',
        'views/course_action.xml',
        'views/course_menu.xml'],


    # Allows the module to be installed
    'installable': True,

    # Marks the module as a standalone application
    'application': True,
}