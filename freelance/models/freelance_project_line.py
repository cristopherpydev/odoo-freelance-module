# -*- coding: utf-8 -*-
from odoo import models, fields, api # type: ignore

class FreelanceProjectLine(models.Model):
    _name = 'freelance.project.line'
    _description = 'Freelance Project Line model'

    project_id = fields.Many2one('freelance.project', ondelete='cascade', required=True)
    hitus_name = fields.Char(required=True)
    description = fields.Char()
    estimated_hours = fields.Float(digits=(12,2), required=True)
    real_hours = fields.Float(digits=(12,2))
    hours_price = fields.Float(digits=(12,2), required=True)
    subtotal = fields.Float(digits=(12,2), compute='_compute_subtotal')
    completed = fields.Boolean()


    # ====== COMPUTE FIELDS ======== #

    @api.depends('estimated_hours', 'hours_price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.estimated_hours * record.hours_price
