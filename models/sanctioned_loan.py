from odoo import models, fields, api


class GradsGradsWaySanctionedLoan(models.Model):
    _name = 'sanctioned.loan'
    _description = 'grads_gateway.grads_gateway.Bank'
    _inherit = ["mail.thread", "mail.activity.mixin"]



    bank = fields.Char(string='Bank')
    sanctioned_amount = fields.Integer(string='Sanctioned Amount')
    remaining_amount = fields.Integer(string='Remaining Amount')
    sanctioned_date = fields.Date(string='sanctioned Date')

    sanctioned_loan_bank_id = fields.Many2one('dizpods.grads_gateway_rep')