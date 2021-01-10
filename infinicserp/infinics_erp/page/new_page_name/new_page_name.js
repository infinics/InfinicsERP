frappe.pages['new-page-name'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'New Page Name',
		single_column: true
	});
}