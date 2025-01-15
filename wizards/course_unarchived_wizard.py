from odoo import models, fields, api

class CourseUnarchivedWizard(models.TransientModel):
    _name = 'course.unarchived.wizard'
    _description = 'Course Unarchived Wizard'

    course_name = fields.Text(string="Name Of The Courses to Unarchived", readonly=True)
    unarchived_courses_id = fields.Many2many('course.model', string="Courses")

    def unarchived_course_wizard(self):
        # Print the context dictionary
        current_context = self.env.context
        print(current_context)

        for wizard in self:
            for course in wizard.unarchived_courses_id:
                course.archived = False

