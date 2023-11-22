from odoo import models, fields, api


class GradsGatewayBank(models.Model):
    _name = 'dizpods.bank'
    _description = 'grads_gateway.grads_gateway.Bank'
    _inherit = ["mail.thread", "mail.activity.mixin"]



    name = fields.Char(string='Bank')