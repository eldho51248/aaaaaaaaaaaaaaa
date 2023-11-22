from odoo import models, fields, api


class GradsGatewayAdmin(models.Model):
    _name = 'dizpods.grads_gateway_admin'
    _description = 'grads_gateway.grads_gateway'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Admin Dashboard Tree View
    name = fields.Char(string='Name', editable=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    status = fields.Selection(
        [('signup', 'Sign Up'), ('contracted', 'contracted'), ('unresponsive', 'Unresponsive'),
         ('loan_application_accepted', 'Loan Application Accepted'), ('cancelled', 'Cancelled'),
         ('visa_issued', 'Visa Issued'), ('declined', 'Declined')])
    last_update = fields.Date(string='Last Update')
    assigned = fields.Char(string='Assigned')
    # Admin Dashboard Form view
    application_id = fields.Char(string='Application ID', readonly=True)
    request_loan_amount = fields.Char(string='Request Loan Amount', readonly=True)
    executive_name = fields.Many2one('res.partner', string='Executive Name')
    executive_phone = fields.Char(string='Phone')
    remark = fields.Char(string='Remark')
    student_data_transfered = fields.Boolean(default=False)

    finance_analysis_ids = fields.One2many('dizpods.grads_gateway_student_dashboard', 'account_payment_id',
                                           string="Finance Analysis", track_visibility=True)
    student_dashboard_bank_ids = fields.One2many('bbank.bank', 'bank_id', string='')
    student_dashboard_status = fields.Char(strin='Status')

    student_dash_executive_name = fields.Char(string='Executive Name')
    student_dashboard_execu_number = fields.Char(string='Number')
    student_dashboard_remark = fields.Char(string='Remark')

    def CreateRepDashboard(self):
        existing_record = self.env['dizpods.grads_gateway_student_dashboard'].search([])

        item = [(0, 0, {'bank': i.bank.id, 'student_dashboard_status': i.student_dashboard_status,
                        'student_dash_last_updated_on': i.student_dash_last_updated_on,
                        'student_dash_remark': i.student_dash_remark}) for i in self.student_dashboard_bank_ids]
        extra_data = {
            # Add other fields as needed
        }

        if existing_record:
            existing_record.write({
                'student_dashboard_bank_ids': item,
                'student_dash_executive_name': self.student_dash_executive_name,
                'student_dashboard_execu_number': self.student_dashboard_execu_number,
                'student_dashboard_remark': self.student_dashboard_remark,
            })
        else:
            self.env['dizpods.grads_gateway_student_dashboard'].create({
                'student_dashboard_bank_ids': item,
                'student_dash_executive_name': self.student_dash_executive_name,
                'student_dashboard_execu_number': self.student_dashboard_execu_number,
                'student_dashboard_remark': self.student_dashboard_remark,

            })


class Bank(models.Model):
    _name = 'bbank.bank'

    bank = fields.Many2one('dizpods.bank', string='Bank')
    bank_id = fields.Many2one('dizpods.grads_gateway_admin')
    bank_id_1 = fields.Many2one('dizpods.grads_gateway_student_dashboard')
    student_dashboard_status = fields.Char(string='Status')
    student_dash_last_updated_on = fields.Date(string='Last Updated on', default=lambda self: fields.Datetime.now())
    student_dash_remark = fields.Char(string='Remark')
