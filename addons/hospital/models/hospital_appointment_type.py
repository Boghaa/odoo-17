# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime


class HospitalAppointmentTypeInherit(models.Model):
    _inherit = 'appointment.type'

    user_doctor_id = fields.Many2one('res.users', 'Doctor', trackig=True)
    res_area_id = fields.Many2one('res.arae', 'Area', tracking=True)
    hospital_rooms_id = fields.Many2one('hospital.rooms', 'Room', tracking=True)

    hospital_prescription_id = fields.Many2one('hospital.prescription', 'prescription', tracking=True)
    hospital_clinics_id = fields.Many2one('hospital.clinics', 'Clinic', tracking=True)
    user_doctor_id = fields.Many2one('res.users', string='Doctor', domain="[('is_doctor', '=', True)]", tracking=True)
    user_leader_id = fields.Many2one('res.users', string='Leader Patients', domain="[('is_leader_patients', '=', True)]", tracking=True)
    partner_patient_id = fields.Many2one('res.partner', 'Patient', domain="[('is_patient', '=', True), ('parent_id', '=', user_leader_id.partner_id.id)]")

    state = fields.Char(string="Status")
    atype = fields.Char(string="Type")

    start_date = fields.Datetime(string='Start Date')
    start_date = fields.Datetime(string='End Date')
    real_duration = fields.Float(string='Real Duration')


