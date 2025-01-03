from pkg_resources import require

from odoo import models, fields

class Course(models.Model):
    _name = 'course.model'
    _description = 'courses'
    _rec_name = "title"

    title = fields.Text(string='Name of the Course', required=True)
    description = fields.Text(string='Description of Course')

    responsible_user = fields.Many2one('res.users', string="Responsible User")

    session_ids = fields.One2many('session.model', 'course_id', string="Sessions")
