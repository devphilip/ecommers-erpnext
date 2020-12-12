import frappe

def get_context(context):
    context['custom1'] = 'Custom Phomepage'
    context['users'] = frappe.get_all('User')
