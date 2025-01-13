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

    archived = fields.Boolean(string="Archived", default=False)

    _sql_constraints = [
        # Ensure that the course title and description are different
        ('check_title_description_diff',
         'CHECK(title != description)',
         'The course title and description must be different.'),

        # Ensure that the course title is unique
        ('unique_course_title',
         'UNIQUE(title)',
         'The course title must be unique.')
    ]

    def copy(self, default=None):

        # Call the super method to ensure the course is duplicated
        default = dict(default or {})

        # Set the new title for the copy
        default['title'] = "Copy of %s" % self.title

        # Call the copy method on the parent model
        return super(Course, self).copy(default=default)


    def action_archive_courses(self):

        for record in self:
            record.archived = True