# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Cash Advance"),
			"items": [
				{
					"type": "doctype",
					"name": "Cash Advance Request",
					"label": _("Cash Advance Request"),
					"description": _("Cash Advance Request Management"),
					"onboard": 1,
				}
			]
		}
	]
