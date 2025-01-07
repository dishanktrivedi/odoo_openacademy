from odoo import models, fields, api


class SessionAttendeeWizard(models.TransientModel):
    _name = 'session.attendee.wizard'
    _description = 'Session Attendee Wizard'

    # Many2one field to select a session
    session_id = fields.Many2many('session.model', string='Session', required=True,
                                  default=lambda self: self._default_session_ids()  )

    # Many2many field to select multiple partners (attendees)
    partner_ids = fields.Many2many('res.partner', string='Attendees', required=True)

    @api.model
    def _default_session_ids(self):
        """Retrieve the current session(s) from the context."""
        return self.env['session.model'].browse(self._context.get('default_session_ids', []))


    def create_attendees(self):
        """Add the selected partners to the attendee_ids field of the session"""
        for session in self.session_id:
            session.attendee_ids = [(4, partner.id) for partner in self.partner_ids]
        return {'type': 'ir.actions.act_window_close'}
