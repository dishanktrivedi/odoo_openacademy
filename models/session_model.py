from odoo import models, fields, api


class Session(models.Model):
    _name = 'session.model'
    _description = 'Session'

    name = fields.Char(string='Session Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Integer(string='Duration (days)', required=True)
    seats = fields.Integer(string='Number of Seats', required=True)

    instructor_id = fields.Many2one('res.partner',
                                    string="Instructor",
                                    domain=[
                                        # '|',
                                        ('is_instructor','=','True'),
                                            # ('category_ids.name', 'in', ['Teacher / Level 1','Teacher / Level 2'])
                                            ])

    course_id = fields.Many2one('course.model', string="Course", required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats_percentage = fields.Float(
        string='Taken Seats',
        compute='_compute_taken_seats_percentage',
        store=True
    )

    @api.depends('attendee_ids', 'seats')
    def _compute_taken_seats_percentage(self):
        for session in self:
            if session.seats > 0:
                session.taken_seats_percentage = (len(session.attendee_ids) / session.seats) * 100
            else:
                session.taken_seats_percentage = 0.0