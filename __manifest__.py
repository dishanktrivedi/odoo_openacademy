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
        'security/groups.xml',
        'security/course_record_rules.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'wizards/course_unarchived_wizard.xml',
        'wizards/purchase_order_button_wizard_view.xml',
        'views/course_action.xml',
        'views/session_view.xml',
        'views/partner_inherit_views.xml',
        'views/course_menu.xml',
        'views/session_report.xml',
        'wizards/session_attendee_wizard_view.xml'],


    # Allows the module to be installed
    'installable': True,

    # Marks the module as a standalone application
    'application': True,
}