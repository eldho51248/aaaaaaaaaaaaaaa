from odoo import models, fields, api

from odoo16.odoo.exceptions import ValidationError


class GradsGatewayStudentDashboard(models.Model):
    _name = 'dizpods.grads_gateway_student_dashboard'
    _description = 'Grads Gateway Student Dashboard'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = 'id desc'

    # related_application_id = fields.Many2one('dizpods.grads_gateway_student', string='Related Application')
    student_dashboard_id = fields.One2many('dizpods.grads_gateway_student', 'student_application_id')

    name = fields.Char(string='Name', readonly=True)
    status = fields.Char(string='Status', readonly=True)
    application_id = fields.Char(string='Application ID', readonly=True)

    student_dash_executive_name = fields.Char(string='Executive Name', readonly=True)
    student_dashboard_status = fields.Char(string='Status', eadonly=True)
    student_dash_last_updated_on = fields.Date(string='Last Updated on', readonly=True)
    student_dash_remark = fields.Char(string='Remark', readonly=True)
    student_dashboard_execu_number = fields.Char(string='Number', readonly=True)
    student_dashboard_remark = fields.Char(string='Remark', readonly=True)
    request_loan_amount = fields.Char(string='Requested Loan Amount', readonly=True)

    # Student Dashboard Loan Status

    # bank = fields.Char(string='Bank')
    bank_preference = fields.Char(string='Bank', readonly=True)
    student_dashboard_bank_ids = fields.One2many('bbank.bank', 'bank_id_1', readonly=True, string='')
    account_payment_id = fields.Many2one('dizpods.grads_gateway_admin', track_visibility=True)

    def view_to_student_application(self):
        xmlid = 'grads_gateway.grads_gateway_student_application_form_view_id'  # Replace with the actual XML ID you are using
        print(f"XML ID: {xmlid}")  # Add this line to print the XML ID for debugging

        # Split the XML ID into module and name
        module, name = xmlid.split('.', 1)

        # Find the view ID using the XML ID
        view_id = self.env.ref(xmlid).id

        return {
            'name': 'Open Form View1',
            'view_mode': 'form',
            'view_id': view_id,
            'res_model': 'dizpods.grads_gateway_student',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'current',
        }

        # view_id = self.env.ref('grads_gateway_student_dashboard_view_form').id
        # return {
        #     'name': 'Open Form View',
        #     'view_mode': 'form',
        #     'view_id': view_id,
        #     'res_model': 'dizpods.grads_gateway_student',
        #     'type': 'ir.actions.act_window',
        #     'res_id': self.id,
        #     'target': 'current',
        # }

    def view_to_student_upload_documents(self):
        view_id = self.env.ref('grads_gateway.grads_gateway_student_upload_ducuments_form_view').id
        return {
            'name': 'Open Form View',
            'view_mode': 'form',
            'view_id': view_id,
            'res_model': 'dizpods.student_upload.document',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'current',
        }
