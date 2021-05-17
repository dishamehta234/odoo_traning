from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/home', type="http")
    def home(self, **kwargs):
        request.session.get('user_id') and request.session.pop('user_id')
        request.session.get('user_name') and request.session.pop('user_name')
        request.session.get('role') and request.session.pop('role')
        user = request.env['users'].search([])
        return request.render('sales_dis.home')
        return request.redirect('/login')

    @http.route('/login', type="http")
    def login(self, **kwargs):
        return request.render('sales_dis.login')

    @http.route('/login_page', type="http", csrf=False)
    def login_page(self, **kwargs):

        return request.redirect('/login_page')

    @http.route('/login_submit', type="http", csrf=False)
    def login_submit(self, **kwargs):

        res_sh = request.env['users'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])
        res_adm = request.env['admin'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])
        res_sp = request.env['sal_per'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])
        print(res_sh)
        # print(res_adm)
        print(res_sp)
        # import pdb; pdb.set_trace()
        if len(res_sp) or len(res_sh) or len(res_adm):
            if len(res_sh):
                request.session['user_id'] = res_sh.id
                request.session['user_name'] = res_sh.name
                request.session['role'] = res_sh.role
                print("Shopper" + request.session['user_name'])
                print("Shopper" + request.session['role'])

                return request.render('sales_dis.login_page')
            elif len(res_adm):
                request.session['user_id'] = res_adm.id
                request.session['user_name'] = res_adm.name
                request.session['role'] = res_adm.role
                print("Shopper" + request.session['user_name'])
                print("Shopper" + request.session['role'])

                return request.render('sales_dis.login_page')
            else:
                request.session['user_id'] = res_sp.id
                request.session['user_name'] = res_sp.name
                request.session['role'] = res_sp.role
                print("Sales Person" + request.session['user_name'])
                print("Shopper" + request.session['role'])
                return request.render('sales_dis.login_page')
        else:
            return http.local_redirect('/login')
        print(kwargs.get("user_id"))
        print("unm")

    #### ---- Inserting User ---- ####
    @http.route('/create_user', type="http")
    def create_user(self, **kwargs):
        return request.render('sales_dis.create_user')

    @http.route('/signup', type="http")
    def signup(self, **kwargs):
        return request.render('sales_dis.signup')

    ##Submit Data of Creating User
    @http.route('/signup_submit', type="http", method="POST", csrf=False)
    def signup_submit(self, **kwargs):
        print("unm")
        request.env['users'].create({
            'name': kwargs.get("fname"),
            'email': kwargs.get("unm"),
            'address': kwargs.get("address"),
            'mobno': kwargs.get("mobno"),
            'password': kwargs.get("pass"),
            'role': kwargs.get("role"),
            's_name': kwargs.get("sname"),
            's_add': kwargs.get("sadd"),
            's_zone': kwargs.get("szone"),
            's_target': kwargs.get("starget"),
            })
        return http.local_redirect('/login')

    ## add product from admin
    @http.route('/add_product', type="http")
    def add_product(self, **kwargs):
        return request.render('sales_dis.add_product')

    #Adding Product
    @http.route('/product_submit', type="http", method="POST", csrf=False)
    def product_submit(self, **kwargs):
        #print(kwargs.get("unm"))
        request.env['prdct'].create({
            'p_name': kwargs.get("pname"),
            'p_price': kwargs.get("price"),
            })
        return request.render('sales_dis.login_page')

    @http.route('/add_visiting_plan', type="http")
    def add_visiting_plan(self, **kwargs):
        return request.render('sales_dis.add_visiting_plan')

    #Adding New visiting Plan
    @http.route('/visiting_submit', type="http", method="POST", csrf=False)
    def visiting_submit(self, **kwargs):
        request.env['visiting_plan'].create({
            'sal_id': 1,
            'visiting_day': kwargs.get("day"),
            'z_name': kwargs.get("zone"),
            'shop_name': kwargs.get("shopnm"),
            })
        return request.render('sales_dis.login_page')

    ## add zone from admin
    @http.route('/add_zone', type="http")
    def add_zone(self, **kwargs):
        return request.render('sales_dis.add_zone')

    ## Adding Zone
    @http.route('/zone_submit', type="http", method="POST", csrf=False)
    def zone_submit(self, **kwargs):
        print(kwargs.get("unm"))
        request.env['zone'].create({
            'z_name': kwargs.get("zname"),
            'z_area': kwargs.get("zarea"),
            })
        return http.local_redirect('/login_page')
    ##      Sales Person   ####

    ##Submit Data of Sales User
    
    @http.route('/add_sp', type="http")
    def add_sp(self, **kwargs):
        return request.render('sales_dis.add_sp')
    # Submit data
    @http.route('/sp_submit', type="http", method="POST", csrf=False)
    def sp_submit(self, **kwargs):
        print(kwargs.get("unm"))
        request.env['sal_per'].create({
            'name': kwargs.get("sname"),
            'email': kwargs.get("s_unm"),
            'address': kwargs.get("s_address"),
            'mobno': kwargs.get("s_mobno"),
            'password': kwargs.get("s_pass"),
            'role': kwargs.get("s_role"),
            })
        return request.render('sales_dis.all_sp')

    @http.route('/salesprofile', type="http")
    def salesprofile(self, **kwargs):
        sales = request.env['sal_per'].search([])
        return request.render('sales_dis.salesprofile', {'sales': sales})

    @http.route('/adminprofile', type="http")
    def adminprofile(self, **kwargs):
        admins = request.env['admin'].search([])
        return request.render('sales_dis.adminprofile', {'admins': admins})

    ##View All Products
    @http.route('/avl_product_shopper', type="http")
    def avl_product_shopper(self, **kwargs):
        products = request.env['prdct'].search([])
        print(products)
        return request.render('sales_dis.avl_product_shopper', {'products': products})

    @http.route('/avl_product_sp', type="http")
    def avl_product_sp(self, **kwargs):
        products_sp = request.env['prdct'].search([])
        print(products_sp)
        return request.render('sales_dis.avl_product_sp', {'products_sp': products_sp})
        # View new arrived orders
    @http.route('/new_order', type="http")
    def new_order(self, **kwargs):
        orders = request.env['order'].search([])
        return request.render('sales_dis.new_order', {'orders': orders})

        # Add order
    @http.route('/order/<int:product_id>', type="http")
    def order(self, product_id, **kwargs):
        print(product_id)
        products = request.env['prdct'].browse(product_id)
        print(products)
        request.env['order'].create({
            'P_id': products.id,
            'p_name': products.p_name,
            'o_status': "pending",
            'o_payment_status': "pending",
            })
        return request.render('sales_dis.new_order')



    # Payment
    @http.route('/payment/<int:order_id>', type="http")
    def payment(self, order_id, **kwargs):
        return request.render('sales_dis.do_payment', {'order_id': order_id})

    @http.route('/do_payment', type="http")
    def do_payment(self, **kwargs):
        return request.render('sales_dis.do_payment')

    # Do Payment by cash
    @http.route('/payment_by_cash', type="http")
    def payment_by_cash(self, **kwargs):
        return request.render('sales_dis.payment_by_cash')


    @http.route('/pay_cash', type="http", method="POST", csrf=False)
    def pay_cash(self, **kwargs):
        request.env['payment'].create({
            'P_id' : 1,
            'p_amount': kwargs.get("amount"),
            'p_mthd': "Cash",
            'p_remark': "Successfull",
            })
        return request.render('sales_dis.payment_list')

    # Do Payment by cheque
    @http.route('/payment_by_cheque', type="http")
    def payment_by_cheque(self, **kwargs):
        return request.render('sales_dis.payment_by_cheque')

    @http.route('/pay_cheque', type="http", method="POST", csrf=False)
    def pay_cheque(self, **kwargs):
        request.env['payment'].create({
            'P_id' : 2,
            'p_amount': kwargs.get("amount"),
            'p_mthd': "Cheque",
            'cheque_no': kwargs.get("cheque"),
            'bank_name':kwargs.get("bankname"),
            'p_remark': "Successfull",
            })
        return request.render('sales_dis.payment_list')

    #View Payment List
    @http.route('/payment_list', type="http")
    def payment_list(self, **kwargs):
        payments = request.env['payment'].search([])
        return request.render('sales_dis.payment_list', {'payments': payments})

    @http.route('/day_list', type="http")
    def day_list(self, **kwargs):
        days = request.env['visiting_plan'].search([])
        return request.render('sales_dis.day_list', {'days': days})

    # View Completed order List 
    @http.route('/completed_order', type="http")
    def completed_order(self, **kwargs):
        return request.render('sales_dis.completed_order')

    #---------------------------------------Shopper--------------------------------------------------------

    @http.route('/shopper_profile', type="http")
    def shopper_profile(self, **kwargs):
        shoppers = request.env['users'].search([])
        return request.render('sales_dis.shopper_profile', {'shoppers': shoppers})

    # @http.route('/shopper_profile', type="http")
    # def shopper_profile(self, **kwargs):
    #     shopper = request.env['users'].search([])
    #     return request.render('sales_dis.shopper_profile', {'shopper': shopper})

    ## All SP List admin side
    @http.route('/all_sp', type="http")
    def all_sp(self, **kwargs):
        allsp = request.env['sal_per'].search([])
        return request.render('sales_dis.all_sp', {'allsp': allsp})

    # #### ---- Removing Sales Person ---- ####
    @http.route('/delete/<model("sal_per"):usr>', type="http")
    def delete(self, usr, **kwargs):
        usr.unlink()
        return http.local_redirect('/all_sp')

    @http.route('/delete_prd/<model("prdct"):pr_remove>', type="http")
    def delete_prd(self, pr_remove, **kwargs):
        pr_remove.unlink()
        return http.local_redirect('/avl_product_shopper')


    ## All Payments Admin Side
    @http.route('/all_payment', type="http")
    def all_payment(self, **kwargs):
        all_payment = request.env['payment'].search([])
        print(all_payment)
        return request.render('sales_dis.all_payment', {'all_payment': all_payment})
    ## Logout 
    @http.route('/logout', type="http")
    def logout(self, **kwargs):
        return http.local_redirect('/home')

    # #### ---- Removing Sales Person ---- ####
    # @http.route('/delete/<model("users"):usr>', type="http")
    # def delete(self, usr, **kwargs):
    #     usr.unlink()
    #     return request.redirect('/home')