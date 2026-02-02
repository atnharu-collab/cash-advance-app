# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cash_advance"
app_title = "Cash Advance"
app_publisher = "Your Company"
app_description = "Cash Advance management application"
app_icon = "octicon octicon-credit-card"
app_color = "blue"
app_email = "your_email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cash_advance/css/cash_advance.css"
# app_include_js = "/assets/cash_advance/js/cash_advance.js"

# include js, css files in header of web template
# web_include_css = "/assets/cash_advance/css/cash_advance.css"
# web_include_js = "/assets/cash_advance/js/cash_advance.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# Website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cash_advance.install.before_install"
# after_install = "cash_advance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cash_advance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }

# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method",
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cash_advance.tasks.all"
# 	],
# 	"daily": [
# 		"cash_advance.tasks.daily"
# 	],
# 	"hourly": [
# 		"cash_advance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cash_advance.tasks.weekly"
# 	]
# }

# Testing
# -------

# before_tests = "cash_advance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cash_advance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cash_advance.task.get_dashboard_data"
# }
