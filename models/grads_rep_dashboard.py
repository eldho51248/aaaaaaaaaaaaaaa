from odoo import models, fields, api


class GradsGatewayRepDashboard(models.Model):
    _name = 'dizpods.grads_gateway_rep'
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
    student_dash_executive_name = fields.Char(string='Phone')
    student_dashboard_execu_number = fields.Char(string='Phone')
    remark = fields.Char(string='Remark')
    student_data_transfered = fields.Boolean(default=False)

    # disbursement
    rep_disbursement = fields.Char(string='Student Disbursement')
    rep_disbursement_date = fields.Date(string='Date')
    rep_disbursement_amount = fields.Integer(string='Amount')






    def CreateBankRepDashboard(self):
        if not self.student_data_transfered:
            for rec in self:
                self.env['dizpods.grads_gateway_bank_rep'].create({
                    'name': self.name,

                })
                self.student_data_transfered = True

    # def CreateBankRepDashboard(self):
    #     if not self.student_data_transfered:
    #         self.env['dizpods.grads_gateway_student_dashboard'].update({
    #             'name': self.name,
    #             'application_id': self.application_id,
    #             'request_loan_amount': self.request_loan_amount,
    #             'status': self.status,
    #             # 'executive_name': self.executive_name,
    #             'executive_phone': self.executive_phone,
    #             'student_disbursement': self.rep_disbursement,
    #             'student_disbursement_date': self.rep_disbursement_date,
    #             'student_disbursement_amount': self.rep_disbursement_amount,
    #
    #
    #         })
    #         self.student_data_transfered = True
            # self.env['dizpods.grads_gateway_student_dashboard'].create({
            #     'student_disbursement': self.rep_disbursement,
            #     'student_disbursement_date': self.rep_disbursement_date,
            #     'student_disbursement_amount': self.rep_disbursement_amount,
            #
            # })
            # self.student_data_transfered = True
