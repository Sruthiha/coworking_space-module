# coworking_space/models/coworking_space.py
from odoo import models, fields

class CoworkingSpace(models.Model):
    _name = 'coworking.space'
    _description = 'Coworking Space'

    name = fields.Char(string='Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    amenities = fields.Text(string='Amenities')
    availability = fields.Boolean(string='Available', default=True)
