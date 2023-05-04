# -*- coding: utf-8 -*-
import logging

from odoo import models, fields
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Presupuesto(models.Model):
    _name = 'presupuesto'
    _description = 'peliculas.peliculas'
    _inherit = ['image.mixin']

    name = fields.Char(string='Pelicula')
    clasificacion = fields.Selection(selection=[
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17'),

    ], string='Clasificacion')
    fch_estreno = fields.Date(string='Fecha de estreno')
    puntuacion = fields.Integer(string='Puntuacion')
    active = fields.Boolean(string='Activo', default=True)
    director_id = fields.Many2one(comodel_name='res.partner', string="Director")
    categoria_director_id = fields.Many2one(comodel_name='res.partner.category', string='Categoria Director',
                                            default=lambda self: self.env['res.partner.category'].search(
                                                [('name', "=", 'Director')]))
    genero_ids = fields.Many2many(comodel_name='genero', string='Generos')
    vista_general = fields.Text(string='Descripcion')
    link_trailer = fields.Char(string='Trailer')
    es_libro = fields.Boolean(string='Version Libro')
    libro = fields.Binary(string='Libro')
    libro_filename = fields.Char(string='Nombre del libro')
    state = fields.Selection(selection=[('borrador', 'Borrador'),
                                        ('aprobado', 'Aprobado'),
                                        ('cancelado', 'Cancelado'),
                                        ], default='borrador', string='Estados', copy=False)
    fch_aprobado = fields.Datetime(string='Fecha aprobado', copy=False)

    def aprobar_presupuesto(self):
        logger.info('Entro a la funcion aprobar presupuesto')
        self.state = 'aprobado'
        self.fch_aprobado = fields.Datetime.now()

    def cancelar_presupuesto(self):
        logger.info('Entro a la funcion cancelar presupuesto')
        self.state = 'cancelado'

    def unlink(self):
        logger.info('**************** se disparo la funcion unlink ')
        if self.state != 'cancelado':
            raise UserError(
                '****************** no se puede eliminar el registro por que no se encuentra en el estado cancelado')
        super(Presupuesto, self).unlink()


    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100
