from odoo import models, fields

class SessionAttendeeWizard(models.TransientModel):
    _name = 'session.attendee.wizard'
    _description = 'Session Attendee Wizard'

    # Many2one field to select a session
    session_id = fields.Many2one('session.model', string='Session', required=True)

    # Many2many field to select multiple partners (attendees)
    partner_ids = fields.Many2many('res.partner', string='Attendees', required=True)

    def create_attendees(self):
        # Loop through each selected partner and add them as attendees to the session
        for partner in self.partner_ids:
            self.env['openacademy.attendee'].create({
                'session_id': self.session_id.id,
                'partner_id': partner.id,
            })
        return {'type': 'ir.actions.act_window_close'}
