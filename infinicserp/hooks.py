# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "infinicserp"
app_title = "Infinics ERP"
app_publisher = "Infinics Limited"
app_description = "Infinics ERP - Used by more than 5000 companies across the world"
app_icon = "device-desktop"
app_color = "#6DAFC9"
app_email = "info@infinics.co.uk"
app_license = "Infinics Limited"
app_logo_url = '/assets/infinicserp/images/erp-logos/infinicserp-icon.svg'


website_context = {
	"favicon": 	"/assets/infinicserp/images/erp-logos/favicon.png",
	"splash_image": "/assets/infinicserp/images/erp-logos/infinicserp-icon.svg"
}



# Includes in <head>
# ------------------

# include js, css files in header of desk.html

app_include_css = "/assets/infinicserp/css/infinicserp.css"
#app_include_js = "/assets/infinicserp/js/infinicserp.js"
# include js, css files in header of web template
web_include_css = "/assets/infinicserp/css/infinicserp.css"
web_include_js = "/assets/infinicserp/js/infinicserp.js"

# include js in page
page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "infinicserp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "infinicserp.install.before_install"
# after_install = "infinicserp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "infinicserp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
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
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"infinicserp.tasks.all"
# 	],
# 	"daily": [
# 		"infinicserp.tasks.daily"
# 	],
# 	"hourly": [
# 		"infinicserp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"infinicserp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"infinicserp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "infinicserp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "infinicserp.event.get_events"
# }

