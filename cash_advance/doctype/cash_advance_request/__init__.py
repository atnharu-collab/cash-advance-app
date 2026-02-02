# -*- coding: utf-8 -*-
# Copyright (c) 2025, AgilaSoft and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CashAdvanceRequest(Document):
	def validate(self):
		if self.total_requested and self.total_requested < 0:
			frappe.throw("Total Requested cannot be negative")
	
	def calculate_total(self):
		total_liquidated = 0
		if self.liquidation:
			for item in self.liquidation:
				if item.amount:
					total_liquidated += item.amount
		
		self.total_liquidated = total_liquidated
		
		if self.total_requested:
			self.unliquidated = self.total_requested - self.total_liquidated
		else:
			self.unliquidated = 0
		
		self.save()
