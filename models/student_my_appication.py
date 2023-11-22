from odoo import models, fields, api

from odoo16.odoo.exceptions import ValidationError


class GradsGatewayStudents(models.Model):
    _name = 'dizpods.grads_gateway_student'
    _description = 'grads_gateway.grads_gateway.Student.Application'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'reference_no'

    # student Details Fields
    student_application_id = fields.Many2one('dizpods.grads_gateway_student_dashboard')

    reference_no = fields.Char(string='Sequence Number',
                               readonly=True, default='New', required=True)
    status = fields.Selection(
        [('signup', 'Sign Up'), ('contracted', 'contracted'), ('unresponsive', 'Unresponsive'),
         ('loan_application_accepted', 'Loan Application Accepted'),
         ('cancelled', 'Cancelled'), ('credit-review', 'Credit Review'), ('loan_approved', 'Loan Approved'),
         ('declined', 'Declined'), ('additional_information', 'Additional Information'),
         ('processing_fee_paid', 'Processing Fee Paid'), ('processing_fee_unpaid', 'Processing Fee Unpaid'),
         ('sanction_letter_issued', 'Sanction Letter-Issued'), ('visa_issued', 'Visa Issued'), ('declined', 'Declined'),
         ('loan_agreement', 'Loan Agreement'), ('disbursed', 'Disbursed'),
         ('pending_disbursement', 'Pending Disbursement'),
         ('closed', 'Closed')], readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    current_address = fields.Text(string='Current Address')
    state = fields.Selection(
        [('andhra_pradesh', 'Andhra Pradesh'), ('arunachal_pradesh', 'Arunachal Pradesh'), ('assam', 'Assam'),
         ('bihar', 'Bihar'),
         ('chhattisgarh', 'Chhattisgarh'), ('goa', 'Goa'), ('gujarat', 'Gujarat'), ('haryana', 'Haryana'),
         ('himachal_pradesh', 'Himachal Pradesh')
            , ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('jharkhand', 'Jharkhand'),
         ('karnataka', 'Karnataka'), ('kerala', 'Kerala')], )
    city = fields.Char(string='City')
    email_id = fields.Char(string='Email ID')
    last_college_university_attended = fields.Char(string='Last College University Attended')
    marks_obtained_in_the_last_course = fields.Char(string='Marks Obtained in the last Course')
    mobile_number = fields.Char(string='Mobile Number')
    name_of_the_last_course_completed = fields.Char(string='Name Of the last Course Completed')

    # student Course Details Fields

    country_of_study = fields.Many2one('res.country', string='Country Of Study')
    course_type = fields.Char(string='Course Type')
    course_name = fields.Char(string='Course Name')
    when_loan_is_required = fields.Date(string='When Loan is Required')
    bank_preference = fields.Many2many('dizpods.bank', string='Bank Preference')
    type_of_collateral_Offered = fields.Char(string='Type of CollateralOffered')
    city_where_collateral_located = fields.Char(string='City Where Collateral Located')
    current_status = fields.Char(string='Current Status')
    course_duration = fields.Char(string='Course Duration')
    university_college_of_study = fields.Char(string='University / College of study')
    loan_amount_in_rupees = fields.Char(string='Loan Amount in Rupees')
    select_the_type_of_loan_required = fields.Selection(
        [('secured', 'Secured'), ('non_secured', 'Non Secured')], default='secured')
    market_value_of_the_collateral = fields.Char(string='Market value of the collateral')
    state_where_collateral_located = fields.Char(string='State where collateral located')

    # student Co Applicant-1 Detail

    applicant1_first_name = fields.Char(string='First Name')
    relationship_with_student = fields.Char(string='Relationship with Student')
    applicant1_state = fields.Char(string='State')
    co_applicant1_current_address = fields.Text(string='Co Applicant current Address')
    co_applicant1_mobile_number = fields.Char(string='Co Applicant Mobile Number')
    profession_of_co_applicant = fields.Char(string='Profession of Co Applicant')
    name_of_employer_business = fields.Char(string='Name of employer / Business')
    co_applicant1_first_name = fields.Char(string='First Name')
    applicant2_relationship_with_student = fields.Char(string='Relationship with Student')
    applicant2_state = fields.Char(string='State')
    co_applicant2_current_address = fields.Text(string='Co Applicant current Address')
    co_applicant2_mobile_number = fields.Char(string='Co Applicant 2 Mobile Number')

    # student Co Applicant-2 Detail
    applicant1_last_name = fields.Char(string='last Name')
    applicant1_date_of_birth = fields.Date(string='Date of Birth')
    co_applicant1_city = fields.Char(string='City')
    co_applicant1_email_address = fields.Char(string='Co Applicant email address')
    designation_of_co_applicant1 = fields.Char(string='Designation of Co applicant')
    net_monthly_income_salary = fields.Char(string='Net Monthly Income / Salary')
    applicant2_last_name = fields.Char(string='Last Name')
    applicant2_date_of_birth = fields.Date(string='Date of Birth')
    co_applicant2_city = fields.Char(string='City')
    co_applicant2_email_address = fields.Char(string='Co Applicant 2 email address')
    student_data_transfered = fields.Boolean(default=False)

    # finance_analysis_ids = fields.One2many('dizpods.grads_gateway_student_dashboard','account_payment_id', string="Finance Analysis", track_visibility=True)

    @api.model
    def create(self, vals):
        vals['reference_no'] = self.env['ir.sequence'].next_by_code(
            'dizpods.grads_gateway_student')
        res = super(GradsGatewayStudents, self).create(vals)
        return res

    def CreateAdminDashboard(self):
        self.status = 'signup'
        if not self.student_data_transfered:
            for rec in self:
                # Create a record in dizpods.grads_gateway_admin
                admin_record = self.env['dizpods.grads_gateway_admin'].create({
                    'name': self.first_name,
                    'phone': self.mobile_number,
                    'email': self.email_id,
                    'status': self.status,
                    'application_id': self.reference_no,
                    'request_loan_amount': self.loan_amount_in_rupees,
                })


                self.env['dizpods.grads_gateway_student_dashboard'].create({
                    'name': self.first_name,
                    'application_id': self.reference_no,
                    'request_loan_amount': self.loan_amount_in_rupees,
                    'status': self.status,
                })

                self.student_data_transfered = True

    # def CreateAdminDashboard(self):
    #     self.status = 'signup'
    #     if not self.student_data_transfered:
    #         for rec in self:
    #             # Create a record in dizpods.grads_gateway_admin
    #             admin_record = self.env['dizpods.grads_gateway_admin'].create({
    #                 'name': self.first_name,
    #                 'phone': self.mobile_number,
    #                 'email': self.email_id,
    #                 'status': self.status,
    #                 'application_id': self.reference_no,
    #                 'request_loan_amount': self.loan_amount_in_rupees,
    #             })
    #
    #             # Create records in dizpods.grads_gateway_student_dashboard for each bank preference
    #             for bank_preference in rec.bank_preference:
    #                 self.env['dizpods.grads_gateway_student_dashboard'].create({
    #                     'name': self.first_name,
    #                     'application_id': self.reference_no,
    #                     'request_loan_amount': self.loan_amount_in_rupees,
    #                     'status': self.status,
    #                     'bank_preference': bank_preference.name,
    #                 })
    #
    #             self.student_data_transfered = True

    # def CreateAdminDashboard(self):
    #     Dashboard = self.env['dizpods.grads_gateway_student_dashboard']
    #
    #     for application in self:
    #         for record in application.bank_preference:
    #             # Create a new record in student.dashboard for each value in the Many2many field
    #             Dashboard.create({
    #                 'bank_preference': record.bank_preference,
    #                 # Replace with the actual field name in student.dashboard
    #                 # Add other fields as needed
    #             })
    #
    #     return True

    # def CreateAdminDashboard(self):
    #     self.status = 'signup'
    #     if not self.student_data_transfered:
    #         for rec in self:
    #             self.env['dizpods.grads_gateway_admin'].create({
    #                 'name': self.first_name,
    #                 'phone': self.mobile_number,
    #                 'email': self.email_id,
    #                 'status': self.status,
    #                 'application_id': self.reference_no,
    #                 'request_loan_amount': self.loan_amount_in_rupees,
    #
    #             })
    #             self.student_data_transfered = True
    #         for record in self:
    #             for rec in record:
    #                 self.env['dizpods.grads_gateway_student_dashboard'].create({
    #                     'name': self.first_name,
    #                     'application_id': self.reference_no,
    #                     'request_loan_amount': self.loan_amount_in_rupees,
    #                     'status': self.status,
    #                     'bank_preference': rec.bank_preference.name,
    #
    #                 })
    #                 self.student_data_transfered = True
