from odoo import models, fields, _

class PurchaseOrderButtonWizard(models.TransientModel):
    _name = "purchase.order.button.wizard"
    _description = "Purchase Order Button Wizard"

    selected_orders = fields.Many2many('purchase.order',string="Selected Orders")


    def process_selected_orders(self):

        # Print the context dictionary
        current_context = self.env.context
        print("Inside Process Orders",current_context)

        if len(self) > 1:
            raise ValueError("This operation is only supported for a single wizard record.")

        for order in self.selected_orders:
            print(f"Processing Purchase Order: {order.name}")
        return {'type': 'ir.actions.act_window_close'}


    def open_purchase_button_wizard(self):

        # Print the context dictionary
        current_context = self.env.context.get('active_ids')
        print("Inside Button Method",current_context)

        """ Launch the wizard """
        return {
            'type': 'ir.actions.act_window',
            'target': 'new',
            'name': _('Open Purchase Button Wizard'),
            'view_mode': 'form',
            'res_model': 'purchase.order.button.wizard',
            'context': {'default_selected_orders': [(6, 0, current_context)]},
        }