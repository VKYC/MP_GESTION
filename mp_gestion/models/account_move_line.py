from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_date = fields.Date(related='move_id.invoice_date')
    l10n_latam_document_type_id = fields.Many2one(related='move_id.l10n_latam_document_type_id')
    journal_id = fields.Many2one(related='move_id.journal_id')
