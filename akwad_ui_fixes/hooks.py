from . import __version__ as app_version

app_name = "akwad_ui_fixes"
app_title = "Akwad UI Fixes"
app_publisher = "Akwad Programming"
app_description = "Akwad UI fixes for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "Blue"
app_email = "support@akwad.qa"
app_license = "MIT"

# ################# below lines added manually ##############################
website_context = {
	"favicon": 	"/assets/akwad/images/akwad-logo-symbol.svg",
	"splash_image": "/assets/akwad/images/akwad-logo-symbol.svg"
}

# Includes in <head>
# ------------------
# include js, css files in header of desk.html
# app_include_css = "/assets/akwad_ui_fixes/css/akwad_ui_fixes.css"
# ################# below lines added manually ##############################
# app_include_js = "/assets/akwad_ui_fixes/js/akwad_ui_fixes.js"
app_include_css = "/assets/akwad_ui_fixes/css/akwad_ui_fixes_desk.css"
# ################# below lines added manually ##############################
# include js, css files in header of web template
web_include_css = "/assets/akwad_ui_fixes/css/akwad_ui_fixes_web.css"
web_include_js = "/assets/akwad_ui_fixes/js/akwad_ui_fixes_web.js"
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "akwad_ui_fixes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "akwad_ui_fixes.install.before_install"
# after_install = "akwad_ui_fixes.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "akwad_ui_fixes.uninstall.before_uninstall"
# after_uninstall = "akwad_ui_fixes.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "akwad_ui_fixes.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"akwad_ui_fixes.tasks.all"
# 	],
# 	"daily": [
# 		"akwad_ui_fixes.tasks.daily"
# 	],
# 	"hourly": [
# 		"akwad_ui_fixes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"akwad_ui_fixes.tasks.weekly"
# 	]
# 	"monthly": [
# 		"akwad_ui_fixes.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "akwad_ui_fixes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "akwad_ui_fixes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "akwad_ui_fixes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"akwad_ui_fixes.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
