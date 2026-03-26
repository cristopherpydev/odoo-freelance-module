# -*- coding: utf-8 -*-
from odoo import api, models, fields # type: ignore

class FreelanceTimeTrack(models.Model):
    _name = 'freelance.time.track'
    _description = 'Freelance Time Track model for freelance module'

    project_id = fields.Many2one('freelance.project', required=True)
    line_id = fields.Many2one('freelance.project.line')
    date = fields.Date(required=True)
    description = fields.Char(required=True)
    hours = fields.Float(required=True)
    usuario_id = fields.Many2one('res.users', default=lambda self: self.env.user)
