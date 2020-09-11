# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import common
from odoo.tests import Form
from odoo.exceptions import ValidationError


class TestRecruitmentStagePreconditions(common.TransactionCase):

    def setUp(self):
        super(TestRecruitmentStagePreconditions, self).setUp()
        self.application = self.env.ref("hr_recruitment.hr_case_dev0")
        self.stage = self.env.ref("hr_recruitment_stage_preconditions.stage_job6")
        self.form = Form(self.application)
        self.form.save()

    def test_move_application_to_phone_call_stage_with_tags_registered(self):
        self.form.stage_id = self.stage
        self.form.save()
        self.assertEqual(self.application.stage_id, self.stage)

    def test_move_application_to_phone_call_stage_without_tags_registered(self):
        self.form.categ_ids.clear()
        with self.assertRaises(ValidationError):
            self.form.stage_id = self.stage
            self.form.save()

    def test_move_application_to_stage_without_precondition(self):
        self.stage = self.env.ref("hr_recruitment.stage_job2")
        self.test_move_application_to_phone_call_stage_with_tags_registered()
