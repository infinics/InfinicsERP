frappe.pages['erp-stuff'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'ERP Stuff',
		single_column: true
	});
}