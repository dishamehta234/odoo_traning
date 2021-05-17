from odoo import  fields, models
class users(models.Model):
    _name = 'users'
    _description = "Users Details of Shopper"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address", translate=True)
    mobno = fields.Integer()
    password = fields.Char(string="Password")
    role = fields.Char(string="Role")
    s_name =  fields.Char(string="Sname")
    s_add = fields.Char(string="Sadd")
    s_zone = fields.Char(string="Zone")
    s_target = fields.Integer()

class users(models.Model):
    _name = 'admin'
    _description = "Users Details of  Admin"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address", translate=True)
    mobno = fields.Integer()
    password = fields.Char(string="Password")
    role = fields.Char(string="Role")


class sal_per(models.Model):
	_name = 'sal_per'
	_description = "Details of Sales Person"

	name = fields.Char(string="Name")
	email = fields.Char(string="Email")
	address = fields.Char(string="Address", translate=True)
	mobno = fields.Integer()
	password = fields.Char(string="Password")
	role = fields.Char(string="Role")

class shop_visit(models.Model):
	_name = 'shop_visit'
	_description = "Details of Visiting Shop"

	sal_id = fields.Many2one('sal_per',string="sal_id")
	visiting_day = fields.Char(string="VisitDay")
	z_name = fields.Char(string="Name")

class visiting_plan(models.Model):
	_name = 'visiting_plan'
	_description = "Details of Visiting Shop"

	sal_id = fields.Many2one('sal_per',string="sal_id")
	visiting_day = fields.Char(string="VisitDay")
	z_name = fields.Char(string="Name")
	shop_name = fields.Char(string="Shope Name")

class prdct(models.Model):
	_name = 'prdct'
	_description = "Details of Product"

	p_name = fields.Char(string="Name")
	p_price =  fields.Integer(string="Price")

class order(models.Model):
	_name = 'order'
	_description = "Details of Order"

	P_id = fields.Many2one('prdct', string="p_id")
	p_name = fields.Char(string="p_name")
	o_status = fields.Char(default="success")
	o_payment_status = fields.Char(default="pendig")

class payment(models.Model):
	_name = "payment"
	_description = "Details of Payment"

	P_id = fields.Many2one('order', string="P_id")
	p_amount =  fields.Float()
	p_mthd = fields.Char(string="Method")
	cheque_no = fields.Integer(string="Cheque no")
	bank_name = fields.Char(string="Bank Name")
	p_remark = fields.Char(string="Remarks")

class zone(models.Model):
	_name = "zone"
	_description = "Detail of Zone"
	
	z_name = fields.Char(string="Name")
	z_area = fields.Char(strin="area")
			
