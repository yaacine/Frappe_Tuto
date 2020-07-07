# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestLibraryMembership(unittest.TestCase):
	
	def test_member_havent_access(self):
		# set library member
		frappe.set_user("yacine.zidemlal@leam.ae")
		doc = frappe.get_doc("Library Membership", frappe.db.get_value("Library Membership",
            {"member_first_name":"yacine"}))
		self.assertFalse(frappe.has_permission("Library Membership", doc=doc))
        