// Copyright (c) 2020, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	// refresh: function(frm) {

	// }

	"library_member" : function(frm) {
        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Library Member",
                name: frm.doc.library_member
            },
            callback: function (data) {
                frappe.model.set_value(frm.doctype,
                    frm.docname, "member_name",
                    data.message.first_name
                    + (data.message.last_name ?
                        (" " + data.message.last_name) : ""))
            }
        })
    }
});
