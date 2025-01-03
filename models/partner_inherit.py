from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string="Is an Instructor")

    attendee_session_ids = fields.Many2many('session.model', string='Attended Sessions')

    # category_ids = fields.Many2many('res.partner.category', string='Categories')