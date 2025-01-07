
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'session.model'
    _description = 'Session'

    name = fields.Char(string='Session Name', required=True)
    start_date = fields.Date(string='Start Date', required=True, default=fields.Date.context_today)
    end_date = fields.Date(string="End Date", required=True)
    duration = fields.Integer(string='Duration (days)', compute='_onchange_dates', store=True)
    seats = fields.Integer(string='Number of Seats', required=True)
    active = fields.Boolean(string='Active', default=True)

    instructor_id = fields.Many2one('res.partner',
                                    string="Instructor",
                                    domain=[
                                        # '|',
                                        ('is_instructor','=','True'),
                                            # ('category_ids.name', 'in', ['Teacher / Level 1','Teacher / Level 2'])
                                            ])

    course_id = fields.Many2one('course.model', string="Course", required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    # New Computed Field
    attendees_count = fields.Integer(string="Attendees Count",compute="_compute_attendees_count",
                                     store=True)



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


    @api.onchange('seats')
    def _onchange_seats(self):
         if self.seats < 0:
            return {
                'warning': {
                    'title': "Invalid Seat Number",
                    'message': "The number of seats cannot be negative.",
                }
            }

    @api.onchange('attendee_ids')
    def _onchange_attendees(self):
        if self.attendee_ids and len(self.attendee_ids) > self.seats:
            return {
                'warning': {
                    'title': "Too Many Attendees",
                    'message': "The number of attendees cannot exceed the number of seats.",
                }
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise ValidationError("The instructor cannot be an attendee in their own session.")


    @api.depends('start_date', 'end_date')
    def _onchange_dates(self):
        if self.start_date and self.end_date:
            start = fields.Date.from_string(self.start_date)
            end = fields.Date.from_string(self.end_date)
            if end < start:
                raise ValidationError("The end date cannot be earlier than the start date.")
            self.duration = (end - start).days

    @api.depends('attendee_ids')
    def _compute_attendees_count(self):
        for session in self:
            session.attendees_count = len(session.attendee_ids)