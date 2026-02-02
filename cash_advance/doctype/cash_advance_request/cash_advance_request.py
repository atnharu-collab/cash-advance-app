# -*- coding: utf-8 -*-
# Copyright (c) 2025, AgilaSoft and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class CashAdvanceRequest(Document):
	def validate(self):
		# Validate that total requested is not negative
		if self.total_requested and self.total_requested < 0:
			frappe.throw("Total Requested cannot be negative")
		
		# Auto-calculate totals on save
		self.calculate_total()
	
	def calculate_total(self):
		"""Calculate Total Requested, Total Liquidated, and Unliquidated"""
		total_requested = 0
		total_liquidated = 0
		
		# Calculate Total Requested from Amount Requested in liquidation table
		if self.liquidation:
			for item in self.liquidation:
				if item.amount_requested:
					total_requested += flt(item.amount_requested)
				if item.amount_liquidated:
					total_liquidated += flt(item.amount_liquidated)
		
		# Set calculated values
		self.total_requested = total_requested
		self.total_liquidated = total_liquidated
		self.unliquidated = total_requested - total_liquidated
		
		return {
			'total_requested': total_requested,
			'total_liquidated': total_liquidated,
			'unliquidated': self.unliquidated
		}
