# -*- coding: utf-8 -*-
from odoo import models, api, fields # type: ignore

class FreelanceProject(models.Model):
    _name = 'freelance.project'

    # ========= FIELDS ========== #

    name = fields.Char(required=True)
    client_id = fields.Many2one('res.partner', required = True)
    description = fields.Char()
    initial_date = fields.Date()
    estimated_deadline = fields.Date()
    state = fields.Selection(selection=[('in_draft', 'In Draft'), ('in_progress', 'In progress'), ('paused', 'Paused'), ('invoiced', 'Invoiced'), ('closed', 'Closed')])
    line_ids = fields.One2many('freelance.project.line', 'project_id')
    time_track_ids = fields.One2many('freelance.time.track', 'project_id')
    total_budget = fields.Float(digits=(12,2), compute='_compute_total_budget')
    worked_hours = fields.Float(digits=(12,2), compute ='_compute_worked_hours')
    invoiced = fields.Float(digits=(12,2))
    outstanding_balance = fields.Float(digits=(12,2), compute='_compute_outstanding_balance')


    # ========== COMPUTED FIELDS ========== #

    @api.depends('line_ids.subtotal')
    def _compute_total_budget(self):
        for record in self:
            budget = sum(record.mapped('line_ids.subtotal'))
            record.total_budget = budget


    @api.depends('time_track_ids.hours')
    def _compute_worked_hours(self):
        for record in self:
            total_hours = record.mapped('time_track_ids.hours')
            record.worked_hours = total_hours


    @api.depends('total_budget', 'outstanding_balance')
    def _compute_outstanding_balance(self):
        for record in self:
            record.outstanding_balance = record.total_budget - record.invoiced