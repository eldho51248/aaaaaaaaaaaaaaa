from odoo import models, fields, api


class StudentsUploadDocument(models.Model):
    _name = 'dizpods.student_upload.document'
    _description = 'grads_gateway.Student upload documents'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    aadhar_card_ids = fields.Many2many('ir.attachment', 'aadhar_card_ids', 'event_id', 'card_id',string='Upload')
    passport_copy_ids = fields.Many2many('ir.attachment', 'passport_copy_ids', 'event_id', 'card_id',string='Upload')
    twelfth_score_card_ids = fields.Many2many('ir.attachment', 'twelfth_score_card_ids', 'event_id', 'card_id',string='Upload')
    master_individual_memos_and_provisional_ids = fields.Many2many('ir.attachment', 'master_individual_memos_and_provisional_ids', 'event_id', 'card_id',string='Upload')
    ielts_ids = fields.Many2many('ir.attachment', 'ielts_ids', 'event_id', 'card_id',string='Upload')
    duolingo_ids = fields.Many2many('ir.attachment', 'duolingo_ids', 'event_id', 'card_id',string='Upload')
    visa_copy_ids = fields.Many2many('ir.attachment', 'visa_copy_ids', 'event_id', 'card_id',string='Upload')

    pan_card_ids = fields.Many2many('ir.attachment', 'pan_card_ids', 'event_id', 'card_id',string='Upload')
    tenth_score_card_ids = fields.Many2many('ir.attachment', 'tenth_score_card_ids', 'event_id', 'card_id',string='Upload')
    bachelors_individual_memos_and_provisional_ids = fields.Many2many('ir.attachment', 'bachelors_individual_memos_and_provisional_ids', 'event_id', 'card_id',string='Upload')
    gre_score_card_ids = fields.Many2many('ir.attachment', 'gre_score_card_ids', 'event_id', 'card_id',string='Upload')
    toefl_ids = fields.Many2many('ir.attachment', 'toefl_ids', 'event_id', 'card_id',string='Upload')
    admission_letter_ids = fields.Many2many('ir.attachment', 'admission_letter_ids', 'event_id', 'card_id',string='Upload')
    one_twenty_document_ids = fields.Many2many('ir.attachment', 'one_twenty_document_ids', 'event_id', 'card_id',string='Upload')

    # Student Co Applicant_1 Document
    co_applicant1_aadhar_card_ids = fields.Many2many('ir.attachment', 'co_applicant1_aadhar_card_ids', 'event_id', 'card_id',string='Upload')
    co_applicant1_pan_card_ids = fields.Many2many('ir.attachment', 'co_applicant1_pan_card_ids', 'event_id', 'card_id',string='Upload')
    latest_electricity_bill_house_tax_paid_receipt_ids = fields.Many2many('ir.attachment', 'latest_electricity_bill_house_tax_paid_receipt_ids', 'event_id', 'card_id',string='Upload')
    passport_size_photo_ids = fields.Many2many('ir.attachment', 'passport_size_photo_ids', 'event_id', 'card_id',string='Upload')
    latest_2_years_form_16_ids = fields.Many2many('ir.attachment', 'latest_2_years_form_16_ids', 'event_id', 'card_id',string='Upload')
    latest_3_months_salary_credited_bank_statement_ids = fields.Many2many('ir.attachment', 'latest_3_months_salary_credited_bank_statement_ids', 'event_id', 'card_id',string='Upload')
    latest_6_months_salary_credited_bank_statement_ids = fields.Many2many('ir.attachment', 'latest_6_months_salary_credited_bank_statement_ids', 'event_id', 'card_id',string='Upload')
    latest_6_months_savings_and_current_statement_ids = fields.Many2many('ir.attachment', 'latest_6_months_savings_and_current_statement_ids', 'event_id', 'card_id',string='Upload')
    agriculture_income_certificate_ids = fields.Many2many('ir.attachment', 'agriculture_income_certificate_ids', 'event_id', 'card_id',string='Upload',help='*only if the co applicant is into Agriculture')
    business_proof_ids = fields.Many2many('ir.attachment', 'business_proof_ids', 'event_id', 'card_id',string='Upload')
    two_itr_filing_along_with_scheduler_ids = fields.Many2many('ir.attachment', 'two_itr_filing_along_with_scheduler_ids', 'event_id', 'card_id',string='Upload')

    #student Collateral Documents

    property_sale_deed_ids = fields.Many2many('ir.attachment', 'property_sale_deed_ids', 'event_id', 'card_id',string='Upload')
    tax_receipt_ids = fields.Many2many('ir.attachment', 'tax_receipt_ids', 'event_id', 'card_id',string='Upload')
    linked_documents_ids = fields.Many2many('ir.attachment', 'linked_documents_ids', 'event_id', 'card_id',string='Upload')
    layout_plan_ids = fields.Many2many('ir.attachment', 'layout_plan_ids', 'event_id', 'card_id',string='Upload')

    #Student Other Documents

    drag_and_drops_files = fields.Many2many('ir.attachment',string='Upload')





