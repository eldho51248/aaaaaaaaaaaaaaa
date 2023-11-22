from odoo import models, fields, api


class GradsGatewayBankRepDashboard(models.Model):
    _name = 'dizpods.grads_gateway_bank_rep'
    _description = 'grads_gateway.grads_gateway'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Rep Dashboard Tree View
    name = fields.Char(string='Name',editable=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    status = fields.Char(string='Status')
    last_update = fields.Date(string='Last Update')
    assigned = fields.Char(string='Assigned by')
    # Rep Dashboard Form view
    application_id = fields.Char(string='Application ID', readonly=True)
    request_loan_amount = fields.Char(string='Request Loan Amount', readonly=True)
    executive_name = fields.Many2one('res.partner', string='Executive Name')
    executive_phone = fields.Char(string='Phone')
    remark = fields.Char(string='Remark')

