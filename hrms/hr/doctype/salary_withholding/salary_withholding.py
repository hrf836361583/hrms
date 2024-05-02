# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SalaryWithholding(Document):
	pass


@frappe.whitelist()
def get_employee_details(employee):
	employee_doc = frappe.get_doc("Employee", employee)

	list = frappe.db.get_list(
		"Salary Structure Assignment",
		filters={"employee": employee},
		fields=["salary_structure"],
		order_by="from_date desc",
	)
	payroll_frequency = len(list) and frappe.db.get_value(
		"Salary Structure", list[0].salary_structure, "payroll_frequency"
	)

	details = {
		"date_of_joining": employee_doc.date_of_joining,
		"relieving_date": employee_doc.relieving_date,
		"employee_name": employee_doc.employee_name,
		"resignation_letter_date": employee_doc.resignation_letter_date,
		"notice_number_of_days": employee_doc.notice_number_of_days,
		"payroll_frequency": payroll_frequency,
	}
	return details