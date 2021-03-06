# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2018 QubiQ (http://www.qubiq.es)

import base64
from odoo import models, fields, api


class FileDownloadModel(models.AbstractModel):
    _name = 'file.download.model'

    data = fields.Binary(
        string='File',
        readonly=True
    )
    name = fields.Char(
        string='File name',
        readonly=True
    )
    comments = fields.Text(
        string='Comments'
    )

    def get_filename(self):
        return ''

    def get_content(self):
        return ''

    def warning(self, mensaje):
        return {
            'type': 'ir.actions.client',
            'tag': 'action_warn',
            'name': ('Aviso'),
            'params': {
               'title': 'Error',
               'text': mensaje,
               'sticky': True}
            }

    @api.multi
    def set_file(self):
        name = self.get_filename()
        out = base64.encodestring(self.get_content())
        self.write({'data': out, 'name': name})
        view = self.env.ref('file_download.wizard_file_download')
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'view_mode': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
