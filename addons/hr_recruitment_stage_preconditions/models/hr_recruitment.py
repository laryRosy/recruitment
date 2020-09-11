# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class Applicant(models.Model):
    _inherit = ['hr.applicant']

    @api.onchange('stage_id')
    def onchange_stage_id(self):
        if self._check_preconditions():
            return super(Applicant, self).onchange_stage_id()

    def _check_preconditions(self):
        stage = self.env['hr.recruitment.stage'].browse(self.stage_id.id)
        method_name = "_" + str.lower(stage.name.replace(" ", "_")) + "_preconditions"
        try:
            method = getattr(self, method_name)
            fulfilled = method()
        except ValidationError as e:
            # Catch all the validations errors thrown on _precondition methods
            raise ValidationError(e.name)
        except:
            # If the _preconditions method doesn't exist
            # stage change should be done
            fulfilled = True
        return fulfilled

    def _phone_call_preconditions(self):
        for applicant in self:
            if applicant.categ_ids:
                return True
            else:
                raise ValidationError(
                    _("Field %s must have value") %
                    (applicant.fields_get('categ_ids')['categ_ids']['string']))
