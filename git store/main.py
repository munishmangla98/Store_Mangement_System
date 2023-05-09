from flask import Flask, render_template, request,flash, redirect
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from flask_login import UserMixin, login_user, current_user, logout_user,login_required
from datetime import datetime


# from flask_login import UserMixin, login_user, current_user, logout_user,login_required 
#to check the authentication weather the user is registered or not

from werkzeug.security import generate_password_hash,check_password_hash 
# to generate the password and to check the password

from flask_login import LoginManager
from enum import unique
#------------------------------------------------------------------------------------------------------

# import sqlite3
# from datetime import datetime

app = Flask(__name__)
app.secret_key = "flash message"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/storeuniproj'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pythonproj'

'''app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder
                                            mysql://username:password@server/database name'''

db = SQLAlchemy(app)
login_manager = LoginManager()

# db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# login.login_view='login'

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


    
class Users(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(300))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)




########################################################

#################################################################



class Employee_master(db.Model):
    employee_id = db.Column(db.Integer,primary_key=True)
    date_of_registration = db.Column(db.String(100), nullable=False)
    staff_Fname = db.Column(db.String(100),nullable=True)
    staff_Mname = db.Column(db.String(100),nullable=True)
    staff_Lname = db.Column(db.String(100),nullable=True)
    staff_email = db.Column(db.String(100),nullable=True)
    staff_mobile_no = db.Column(db.String(100),nullable=True)
    staff_alternative_mobile_no = db.Column(db.String(100),nullable=True)
    staff_gender = db.Column(db.String(100),nullable=True)
    nature_of_job = db.Column(db.String(100),nullable=True)
    staff_date_of_joining=db.Column(db.String(100),nullable=True)
    staff_date_of_retirement=db.Column(db.String(100),nullable=True)
    staff_category=db.Column(db.String(100),nullable=True)
    staff_designatin=db.Column(db.String(100),nullable=True)
    staff_house_address=db.Column(db.String(100),nullable=True)
    staff_remarks=db.Column(db.String(100),nullable=True)

class Vendor_Master(db.Model):
    vendor_id = db.Column(db.Integer,primary_key=True)
    date_of_registration = db.Column(db.String(100),nullable=False)
    vendor_company_name = db.Column(db.String(100),nullable=False)
    GST_NO = db.Column(db.String(100),nullable=False)
    vendor_status = db.Column(db.String(100),nullable=False)
    vendor_email = db.Column(db.String(100),nullable=False)
    vendor_mobile_num = db.Column(db.String(100),nullable=False)
    vendor_alternative_mobile_num = db.Column(db.String(100),nullable=False)
    vendor_addres = db.Column(db.String(100),nullable=False)
    Remarks = db.Column(db.String(100),nullable=False)

class Order_Transaction_Details(db.Model):
    transaction_id = db.Column(db.String(100),primary_key=True)
    vendor_id = db.Column(db.String(100),nullable=False)
    order_id = db.Column(db.String(100),nullable=False)
    item_id = db.Column(db.String(100),nullable=False)
    item_received_date = db.Column(db.String(100),nullable=False)
    Remarks = db.Column(db.String(100),nullable=False)

class Budget_Head(db.Model):
    Budget_head_id = db.Column(db.Integer,primary_key=True)
    Budget_name = db.Column(db.String(100),nullable=False)
    budget_amount = db.Column(db.String(100),nullable=False)
    Session = db.Column(db.String(100),nullable=False)
    Remarks = db.Column(db.String(100),nullable=False)

class Order_Master(db.Model):
    order_id = db.Column(db.Integer,primary_key=True)
    items= db.Column(db.String(100),nullable=False)
    order_date_placed = db.Column(db.String(100),nullable=False)
    order_recieve_date = db.Column(db.String(100),nullable=False)
    vendor_company_name = db.Column(db.String(100),nullable=False)
    total_order_amount = db.Column(db.String(100),nullable=False)
    payment_status = db.Column(db.String(100),nullable=False)
    Mode_of_payment = db.Column(db.String(100),nullable=False)
    transaction_id = db.Column(db.String(100),nullable=False)
    Bill_No = db.Column(db.String(100),nullable=False)
    Remarks = db.Column(db.String(100),nullable=False)


class Item_Master(db.Model):
    item_id = db.Column(db.Integer,primary_key=True)
    vendor_company_name = db.Column(db.String(100),nullable=False)
    item_name = db.Column(db.String(100),nullable=False)
    item_configuration = db.Column(db.String(100),nullable=False)
    item_model = db.Column(db.String(100),nullable=False)
    item_company = db.Column(db.String(100),nullable=False)
    item_warranty = db.Column(db.String(100),nullable=False)
    item_price = db.Column(db.String(100),nullable=False)
    item_quantity = db.Column(db.String(100),nullable=False)
    budget_id = db.Column(db.String(100),nullable=False)
    project_id = db.Column(db.String(100),nullable=False)
    item_purchase_date = db.Column(db.String(100),nullable=False)
    Purchase_under = db.Column(db.String(100),nullable=False)
    stock_register_page_no = db.Column(db.String(100),nullable=False)
    online_entry_id = db.Column(db.String(100),nullable=False)

class Item_Allotment(db.Model):
    allotment_Id = db.Column(db.String(100),primary_key=True)
    employee_Id =db.Column(db.String(100),nullable=False)
    item_id = db.Column(db.String(100),nullable=False)
    item_Issue_Date = db.Column(db.String(100),nullable=False)
    item_Quantity_Issue = db.Column(db.String(100),nullable=False)
    item_Placement_Area = db.Column(db.String(100),nullable=False)
    project_Id = db.Column(db.String(100),nullable=False)
    Remarks = db.Column(db.String(100),nullable=False)

class Item_Receive_Back(db.Model):
    item_receive_back_id = db.Column(db.String(100),primary_key=True)
    employee_id	=db.Column(db.String(100),nullable=False)
    project_id=db.Column(db.String(100),nullable=False)
    item_id=db.Column(db.String(100),nullable=False)
    allotment_Id=db.Column(db.String(100),nullable=False)
    item_receive_date=db.Column(db.String(100),nullable=False)
    item_receive_quantity = db.Column(db.String(100),nullable=False)
    item_placement_area=db.Column(db.String(100),nullable=False)
    Remarks=db.Column(db.String(100),nullable=False)

class Project_Details(db.Model):
    project_id = db.Column(db.Integer,primary_key=True)
    employee_id = db.Column(db.String(100),nullable=False)
    item_name = db.Column(db.String(100),nullable=False)
    items_requiered = db.Column(db.String(100),nullable=False)
    total_item_issues = db.Column(db.String(100),nullable=False)
    Budget_name = db.Column(db.String(100),nullable=False)
    project_budget= db.Column(db.String(100),nullable=False)
    project_budget_session=db.Column(db.String(100),nullable=False)
    Remarks =db.Column(db.String(100),nullable=False)

class Item_place(db.Model):
    item_place_id = db.Column(db.String(100),primary_key=True)
    item_name = db.Column(db.String(100),nullable=False)
    item_place_area = db.Column(db.String(100),nullable = False)
    no_item = db.Column(db.String(100),nullable=False)
    remarks = db.Column(db.String(100),nullable=False)

@app.route("/item_place", methods=["GET","POST"])
def itemplace():
    if(request.method=='POST'): 
        '''Add entry to the database'''
        itm_plc_id = request.form.get('itm_plc_id')
        itm_name = request.form.get('itm_name')
        itm_plc = request.form.get('itm_plc')
        no_itm = request.form.get('no_itm')
        rmks = request.form.get('rmks')


        entry =Item_place(item_place_id=itm_plc_id,	item_name=itm_name,item_place_area=itm_plc,no_item=no_itm,remarks=rmks)

        db.session.add(entry)
        db.session.commit()
    return render_template ('item_place.html')

@app.route("/item_place_detrails", methods=["GET","POST"])
def item_place_detrails():
        itemplace = Item_place.query.filter_by().all()
        return render_template ('item_place_detrails.html',item_place=itemplace)
#######################################################


#############################################################
@app.route("/")
def hello_world():

    return render_template('register.html')


@app.route("/index",methods=["GET","POST"])
@login_required
def hello():
    return render_template('index.html')


############################     NEW  ###############################################



@app.route("/budget", methods=["GET","POST"])
@login_required
def Budget_head_i():
        budget_head_details = Budget_Head.query.filter_by().all()
        return render_template ('budget.html',budget_head=budget_head_details)

@app.route("/employee", methods=["GET","POST"])
@login_required
def Employee_full_detail():
        employee_master = Employee_master.query.filter_by().all()
        return render_template ('employee.html',employee_master=employee_master)

@app.route("/vendor", methods=["GET","POST"])
@login_required
def vendor_details():
        vendor_master = Vendor_Master.query.filter_by().all()
        return render_template ('vendor.html',vendor_master=vendor_master)

@app.route("/item", methods=["GET","POST"])
@login_required
def item_details():
    item_master_details = Item_Master.query.filter_by().all()
    return render_template ('item.html',item__master=item_master_details)

@app.route("/order", methods=["GET","POST"])
@login_required
def order_master_detail():
        order_master_details = Order_Master.query.filter_by().all()
        return render_template ('order.html',order_master=order_master_details)

@app.route("/project", methods=["GET","POST"])
@login_required
def project_detail():
    project_full_details = Project_Details.query.filter_by().all()
    return render_template ('project.html',project__details=project_full_details)

##################################################################################

@app.route("/add_emp", methods=["GET","POST"])
@login_required
def employee_master():
    if(request.method=='POST'):
        '''Add entry to the database'''
        # employee_id = " "
        e_id = request.form.get('e_id')
        registration = request.form.get('registration')
        Fname = request.form.get('Fname')
        Mname = request.form.get('Mname')
        Lname = request.form.get('Lname')
        email = request.form.get('email')
        mobile_no = request.form.get('mobile_no')
        alternative_mobile_no = request.form.get('alternative_mobile_no')
        gender = request.form.get('gender')
        noj = request.form.get('noj')
        doj = request.form.get('doj')
        dor = request.form.get('dor')
        category = request.form.get('category')
        designation = request.form.get('designation')
        house_address = request.form.get('house_address')
        remarks = request.form.get('remarks')

        entry = Employee_master(employee_id=e_id,date_of_registration=registration, staff_Fname=Fname,staff_Mname = Mname,staff_Lname=Lname,staff_email=email,staff_mobile_no=mobile_no,staff_alternative_mobile_no=alternative_mobile_no,staff_gender=gender,nature_of_job=noj,staff_date_of_joining=doj,staff_date_of_retirement=dor,staff_category=category,staff_designatin=designation,staff_house_address=house_address,staff_remarks=remarks)

        db.session.add(entry)
        db.session.commit()
    return render_template ('add_emp.html')

@app.route("/Order_transaction_details", methods=["GET","POST"])
@login_required
def order_transaction_details():
    if(request.method=='POST'):
        '''Add entry to the database'''
        # trans_id = ""
        # ven_id = ""
        # ord_id = ""
        # itm_id = ""
        # ird = ""
        # rm = ""

        trans_id = request.form.get("trans_id")
        ven_id = request.form.get("ven_id")
        ord_id = request.form.get("ord_id")
        itm_id = request.form.get("itm_id")
        ird = request.form.get("ird")
        rm = request.form.get("rm")
        
        entry = Order_Transaction_Details(transaction_id=trans_id,vendor_id=ven_id,order_id=ord_id,item_id=itm_id,item_received_date=ird,remarks=rm)
       

        db.session.add(entry)
        db.session.commit()
    return render_template ('Order_transaction_details.html')



@app.route("/add_order", methods=["GET","POST"])
@login_required
def order_master():
    if(request.method=='POST'):
        '''Add entry to the database'''
        or_id = request.form.get('or_id')
        item = request.form.get("items")
        odp = request.form.get('odp')
        ord = request.form.get('ord')
        vcn=request.form.get('vcn')
        toa = request.form.get("toa")
        p_s = request.form.get("p_s")
        Mop = request.form.get("Mop")
        trans_id = request.form.get("trans_id")
        B_n = request.form.get("B_n")
        Rmk = request.form.get("Rmk")
        entry = Order_Master(order_id=or_id,items=item,order_date_placed=odp,order_recieve_date=ord,vendor_company_name=vcn,total_order_amount=toa,payment_status=p_s,Mode_of_payment=Mop,transaction_id=trans_id,Bill_No=B_n,Remarks=Rmk)
        db.session.add(entry)
        db.session.commit()
    return render_template ('add_order.html')


@app.route("/add_item", methods=["GET","POST"])
@login_required
def item_master():
    if(request.method=='POST'):
        '''Add entry to the database'''

        itm_id = request.form.get('itm_id')
        vcn=request.form.get('vcn')
        itm_name = request.form.get('itm_name')
        itm_config = request.form.get('itm_config')
        itm_mdl = request.form.get('itm_mdl')
        itm_comp = request.form.get('itm_comp')
        itm_warnt = request.form.get('itm_warnt')
        itm_pr = request.form.get('itm_pr')
        itm_qnt = request.form.get('itm_qnt')
        bgt_id = request.form.get('bgt_id')
        prj_id = request.form.get('prj_id')
        ipd = request.form.get('ipd')
        pur_und = request.form.get('pur_und')
        srpn = request.form.get('srpn')
        oei= request.form.get('oei')

        entry = Item_Master(item_id=itm_id,vendor_company_name=vcn,item_name=itm_name,item_configuration=itm_config,item_model=itm_mdl,item_company=itm_comp,item_warranty=itm_warnt,item_price=itm_pr,item_quantity=itm_qnt,budget_id=bgt_id,project_id=prj_id,item_purchase_date=ipd,Purchase_under=pur_und,stock_register_page_no=srpn,online_entry_id=oei)
        db.session.add(entry)
        db.session.commit()
    return render_template ('add_item.html')



@app.route("/add_budget", methods=["GET","POST"])
@login_required
def budget_head():
    if(request.method=='POST'):
        '''Add entry to the database'''
        bh_id=request.form.get('bh_id')
        bgt_name=request.form.get('bgt_name')
        bgt_amt=request.form.get('bgt_amt')
        secn=request.form.get('secn')
        rmk=request.form.get('rmk')
        entry = Budget_Head(Budget_head_id=bh_id,Budget_name=bgt_name,budget_amount=bgt_amt,Session=secn,Remarks=rmk)
        db.session.add(entry)
        db.session.commit()
    return render_template ('add_budget.html')

@app.route("/add_ven", methods=["GET","POST"])
@login_required
def vendor_master():
    if(request.method=='POST'):
        '''Add entry to the database'''
        ven_id=request.form.get('ven_id')
        vcn=request.form.get('vcn')
        dor = request.form.get('dor')
        gst= request.form.get('gst')
        ven_st=request.form.get('ven_st')
        v_a=request.form.get('v_a')
        v_e=request.form.get('v_e')
        vmn = request.form.get('vmn')
        vamn=request.form.get('vamn')
        rmk=request.form.get('rmk')        
        entry = Vendor_Master(vendor_id=ven_id,date_of_registration=dor,vendor_company_name=vcn,GST_NO=gst,vendor_status=ven_st,vendor_email=v_e,vendor_addres=v_a,vendor_mobile_num=vmn,vendor_alternative_mobile_num=vamn, Remarks=rmk)
        db.session.add(entry)
        db.session.commit()
    return render_template ('add_ven.html')

@app.route("/Item_allotment", methods=["GET","POST"])
@login_required
def item_allotment():
     if(request.method=='POST'):
        '''Add entry to the database'''
        allotmen_Id = request.form.get('a_id')
        e_id = request.form.get('e_id')
        itm_id = request.form.get('itm_id')
        i_i_d = request.form.get('i_i_d')
        i_q_i = request.form.get('i_q_i')
        i_p_a =request.form.get('i_p_a')
        prj_id = request.form.get('prj_id')
        rk = request.form.get('rk')

        entry=Item_Allotment(allotment_Id=allotmen_Id,employee_Id=e_id,item_id=itm_id,item_Issue_Date=i_i_d,item_Quantity_Issue=i_q_i,item_Placement_Area=i_p_a,project_Id=prj_id,Remarks=rk)
        db.session.add(entry)
        db.session.commit()
     return render_template ('Item_allotment.html')

@app.route("/Item_receive_back", methods=["GET","POST"])
@login_required
def Item_receive_back():
    if(request.method=='POST'):
        '''Add entry to the database'''
        i_r_b =request.form.get('i_r_b')
        e_id =request.form.get('e_id')
        prj_id =request.form.get('prj_id')
        itm_id =request.form.get('itm_id')
        allotmen_id =request.form.get('a_id')
        i_r_d =request.form.get('i_r_d')
        i_pl_a =request.form.get('i_pl_a')
        i_r_q = request.form.get('i_r_q')
        rmks =request.form.get('rmks')
        
        entry= Item_Receive_Back(item_receive_back_id=i_r_b, employee_id=e_id, project_id=prj_id, item_id=itm_id, allotment_Id=allotmen_id, item_receive_date=i_r_d, item_placement_area=i_pl_a,item_receive_quantity=i_r_q, Remarks=rmks)
        db.session.add(entry)
        db.session.commit()
    return render_template ('Item_receive_back.html')

@app.route("/add_project", methods=["GET","POST"])
@login_required
def project_details():
    if(request.method=='POST'):
        '''Add entry to the database'''
        prj_id= request.form.get('prj_id')
        e_id = request.form.get('e_id')
        itm_name = request.form.get('itm_name')
        itm_req =request.form.get('itm_req')
        t_i_i = request.form.get('t_i_i')
        bgt_name=request.form.get('bgt_name')
        p_b_s = request.form.get('p_b_s')
        prj_bgt =request.form.get('prj_bgt')
        remk =request.form.get('remk')
        entry=Project_Details(project_id=prj_id,employee_id=e_id,item_name=itm_name,items_requiered=itm_req,total_item_issues=t_i_i,Budget_name=bgt_name,project_budget_session=p_b_s,project_budget=prj_bgt,Remarks=remk)
        db.session.add(entry)
        db.session.commit()
    return render_template ('add_project.html')




@app.route("/Order_trans_details", methods=["GET","POST"])
@login_required
def order_master_details():
        order__transaction__details = Order_Transaction_Details.query.filter_by().all()
        return render_template ('Order_trans_details.html',order__transaction__details=order__transaction__details)

@app.route("/Budget_head_details", methods=["GET","POST"])
@login_required
def Budget_head_id():
        budget_head_details = Budget_Head.query.filter_by().all()
        return render_template ('Budget_head_details.html',budget_head=budget_head_details)


@app.route("/item_allotment_details", methods=["GET","POST"])
@login_required
def item_allotment_detail():
    item_allotment_details = Item_Allotment.query.filter_by().all()
    return render_template ('item_allotment_details.html',item_allotment=item_allotment_details)

@app.route("/item_receive_detail", methods=["GET","POST"])
@login_required
def item_receive_details():
    item_receive_detail = Item_Receive_Back.query.filter_by().all()
    return render_template ('item_receive_detail.html',item__receive__back=item_receive_detail)




    
#.........................................................................................................................
                                                        #Edit Section






#.........................................................................................................
                                                # Delete Section


@app.route("/deleteitmrec/<string:i_r_b>", methods=["GET","POST"])
@login_required
def deleteitmrec(i_r_b):
    flash("Data Deleted Successfully")
    item_receive_back = Item_Receive_Back.query.filter_by(item_receive_back_id=i_r_b).first()
    db.session.delete(item_receive_back)
    db.session.commit()
    return redirect ('/item_receive_detail')

@app.route("/deleteitemallotdlt/<string:a_id>", methods=["GET","POST"])
@login_required
def deleteitmdlt(a_id):
    flash("Data Deleted Successfully")
    item_allotment = Item_Allotment.query.filter_by(allotment_Id=a_id).first()
    db.session.delete(item_allotment)
    db.session.commit()
    return redirect ('/item_allotment_details')

@app.route("/deleteproject/<string:prj_id>", methods=["GET","POST"])
@login_required
def deleteproj(prj_id):
    flash("Data Deleted Successfully")
    project_details = Project_Details.query.filter_by(project_id=prj_id).first()
    db.session.delete(project_details)
    db.session.commit()
    return redirect ('/project')


@app.route("/deleteorderdetail/<string:or_id>", methods=["GET","POST"])
@login_required
def deleteorddlt(or_id):
    flash("Data Deleted Successfully")
    order_master = Order_Master.query.filter_by(order_id=or_id).first()
    db.session.delete(order_master)
    db.session.commit()
    return redirect ('/order_detail')

@app.route("/deleteBgthd/<string:bh_id>", methods=["GET","POST"])
@login_required
def deleteBgthd(bh_id):
    flash("Data Deleted Successfully")
    budget_head = Budget_Head.query.filter_by(Budget_head_id=bh_id).first()
    db.session.delete(budget_head)
    db.session.commit()
    return redirect ('/budget')

@app.route("/deletevendor/<string:ven_id>", methods=["GET","POST"])
@login_required
def deletevendor(ven_id):
    flash("Data Deleted Successfully")
    vendor_master = Vendor_Master.query.filter_by(vendor_id=ven_id).first()
    db.session.delete(vendor_master)
    db.session.commit()
    return redirect ('/vendor')


@app.route("/deleteemployee/<string:e_id>", methods=["GET","POST"])
@login_required
def deleteemployee(e_id):
    flash("Data Deleted Successfully")
    employee__master = Employee_master.query.filter_by(employee_id=e_id).first()
    db.session.delete(employee__master)
    db.session.commit()
    return redirect ('/employee')

@app.route("/deleteitem/<string:itm_id>", methods=["GET","POST"])
@login_required
def deleteitem(itm_id):
    flash("Data Deleted Successfully")
    item__master = Item_Master.query.filter_by(item_id=itm_id).first()
    db.session.delete(item__master)
    db.session.commit()
    return redirect ('/item_details')

@app.route("/deleteorder/<string:trans_id>", methods=["GET","POST"])
@login_required
def deleteorder(trans_id):
    flash("Data Deleted Successfully")
    order__transaction__details = Order_Transaction_Details.query.filter_by(employee_id=trans_id).first()
    db.session.delete(order__transaction__details)
    db.session.commit()
    return redirect ('/Order_trans_details')


@app.route("/vendor_details", methods=["GET","POST"])
@login_required
def delete_vendor():
                vendor_master = Vendor_Master.query.filter_by().all()
                return render_template ('vendor_details.html',vendor_master=vendor_master)




#------------------------------------------Edit ----------------------------------------------

@app.route("/empupdate/<int:e_id>", methods=["GET","POST"])
@login_required
def Empupdating(e_id):
   

    if(request.method=='POST'):
        flash("Employee Member Update Sucessfull")
        '''Add entry to the database'''
        
        employee_master = Employee_master.query.filter_by(employee_id=e_id).first()
       
        registration = request.form.get('registration')
        Fname = request.form.get('Fname')
        Mname = request.form.get('Mname')
        Lname = request.form.get('Lname')
        email = request.form.get('email')
        mobile_no = request.form.get('mobile_no')
        alternative_mobile_no = request.form.get('alternative_mobile_no')
        gender = request.form.get('gender')
        noj = request.form.get('noj')
        doj = request.form.get('doj')
        dor = request.form.get('dor')
        category = request.form.get('category')
        designation = request.form.get('designation')
        house_address = request.form.get('house_address')
        remarks = request.form.get('remarks')

        

        employee_master.date_of_registration=registration
        employee_master.staff_Fname=Fname
        employee_master.staff_Mname=Mname
        employee_master.staff_Lname=Lname
        employee_master.staff_email=email
        employee_master.staff_mobile_no=mobile_no
        employee_master.staff_alternative_mobile_no=alternative_mobile_no
        employee_master.staff_gender=gender
        employee_master.nature_of_job=noj
        employee_master.staff_date_of_joining=doj
        employee_master.staff_date_of_retirement=dor
        employee_master.staff_category=category
        employee_master.staff_designatin=designation
        employee_master.staff_house_address=house_address
        employee_master.staff_remarks=remarks

        db.session.commit()



    else:
        employee_master = Employee_master.query.filter_by(employee_id=e_id).first()
    return render_template ('empupdate.html',employee_master=employee_master)



@app.route("/venupdate/<int:ven_id>", methods=["GET","POST"])
@login_required
def venupdating(ven_id):
    if(request.method=='POST'):
        flash("Vendor Update Sucessfull")
        '''Add entry to the database'''
        
        vendor_master = Vendor_Master.query.filter_by(vendor_id=ven_id).first()

        dor = request.form.get('dor')
        vcn=request.form.get('vcn')
        gst= request.form.get('gst')
        ven_st=request.form.get('ven_st')
        v_e=request.form.get('v_e')
        vmn = request.form.get('vmn')
        vamn=request.form.get('vamn')
        v_a=request.form.get('v_a')
        rmk=request.form.get('rmk') 

        vendor_master.date_of_registration=dor
        vendor_master.vendor_company_name=vcn
        vendor_master.GST_NO=gst
        vendor_master.vendor_status=ven_st
        vendor_master.vendor_email=v_e
        vendor_master.vendor_mobile_num=vmn
        vendor_master.vendor_alternative_mobile_num=vamn
        vendor_master.vendor_addres=v_a
        vendor_master.Remarks=rmk


        # print(dor,vcn,gst,ven_st,v_e,vmn,vamn,v_a,rmk)

        db.session.commit()

    else:
        vendor_master = Vendor_Master.query.filter_by(vendor_id=ven_id).first()



#the below comment function is done due to the date time in the data base (# dor = vendor_master.date_of_registration
                                                                            # dor_rep = f'{dor.year}-{str(dor.month).zfill(2)}-{dor.day}'
                                                                            # flash(dor_rep)
    # return render_template ('venupdate.html',vendor_master=vendor_master,dor_rep=dor_rep))



@app.route("/itemupdate/<string:itm_id>", methods=["GET","POST"])
@login_required
def itemupdate(itm_id):
        if(request.method=='POST'):
            flash("Item Update Sucessfull") 
            '''Add entry to the database'''
            item__master = Item_Master.query.filter_by(item_id=itm_id).first()
            item__master.display()

            ven_id = request.form.get('ven_id')
            itm_name = request.form.get('itm_name')
            itm_config = request.form.get('itm_config')
            itm_mdl = request.form.get('itm_mdl')
            itm_comp = request.form.get('itm_comp')
            itm_warnt = request.form.get('itm_warnt')
            itm_pr = request.form.get('itm_pr')
            itm_qnt = request.form.get('itm_qnt')
            bgt_id = request.form.get('bgt_id')
            prj_id = request.form.get('prj_id')
            ipd = request.form.get('ipd')
            pur_und = request.form.get('pur_und')
            srpn = request.form.get('srpn')
            oei= request.form.get('oei')
        
            item__master.vendor_id = ven_id
            item__master.item_name = itm_name
            item__master.item_configuration = itm_config
            item__master.item_model = itm_mdl
            item__master.item_company = itm_comp
            item__master.item_warranty = itm_warnt
            item__master.item_price = itm_pr
            item__master.item_quantity=itm_qnt
            item__master.budget_id=bgt_id
            item__master.project_id=prj_id
            item__master.item_purchase_date=ipd
            item__master.Purchase_under=pur_und
            item__master.stock_register_page_no=srpn
            item__master.online_entry_id=oei
        else:
            item__master = Item_Master.query.filter_by(item_id=itm_id).first()

            return render_template('itemupdate.html',item__master=item__master)
        


@app.route("/orderupdate/<string:or_id>", methods=["GET","POST"])
@login_required
def orderupdate(or_id):
        if(request.method=='POST'):
            flash("Order Update Sucessfull") 
            '''Add entry to the database'''
            order_master = Order_Master.query.filter_by(item_id=or_id).first()

            or_id = request.form.get('or_id')
            item = request.form.get("items")
            odp = request.form.get('odp')
            ord = request.form.get('ord')
            vcn=request.form.get('vcn')
            toa = request.form.get("toa")
            p_s = request.form.get("p_s")
            Mop = request.form.get("Mop")
            trans_id = request.form.get("trans_id")
            B_n = request.form.get("B_n")
            Rmk = request.form.get("Rmk")
    
            order_master.items=item
            order_master.order_date_placed = odp
            order_master.order_recieve_date=ord
            order_master.vendor_company_name=vcn
            order_master.total_order_amount = toa
            order_master.payment_status = p_s
            order_master.Mode_of_payment = Mop
            order_master.transaction_id=trans_id
            order_master.Bill_No=B_n
            order_master.Remarks=Rmk
        
        else:
            order_master = Order_Master.query.filter_by(order_id=or_id).first()

            return render_template('orderupdate.html',order_master=order_master)
        




# @app.route("/venupdate/<int:ven_id>", methods=["GET","POST"])
# @login_required
# def venupdating(ven_id):
#     if(request.method=='POST'):
#         flash("Vendor Update Sucessfull")
#         '''Add entry to the database'''
        
#         item_master = Item_Master.query.filter_by(vendor_id=ven_id).first()


# @app.route('/test')
# def test():
#         employee = Employee_master.query.filter_by(employee_id=2).first()
#         e_id = 2
#         print('######################')
#         print(employee.nature_of_job)

#         employee.staff_Fname = 'updateddddd'
#         employee.staff_Mname = 'updateddddd'
#         employee.staff_Lname = 'updateddddd'
#         employee.staff_email = 'updateddddd'
#         employee.staff_mobile_no = 'updateddddd'
#         employee.staff_alternative_mobile_no = 'updateddddd'
#         employee.staff_gender = 'updateddddd'
#         employee.nature_of_job = 'updateddddd'
#         employee.staff_category = 'updateddddd'
#         employee.staff_designatin = 'updateddddd'
#         employee.staff_house_address = 'updateddddd'
#         employee.staff_remarks = 'updateddddd'
#         print(':::::::::::::::::::::::::::')
#         data = Employee_master.query.filter_by(employee_id=e_id).first()
#         print(data)
#         # data.update({employee_master.remarks: 'updatedddd'})
#         db.session.commit()
#         return 'done'


#------------------------LOGIN---------------------------------------
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
       return redirect('/index')
    if request.method == 'POST':
        email = request.form.get('email')
        user = Users.query.filter_by(email=email).first()
        if user is not None and user.check_password(request.form.get('password')):
            login_user(user)
            return redirect('/index')
        # return render_template('/register.html')
        flash("You entered wrong Password , Please Enter right Password")
    return render_template('/register.html')        


@app.route('/register', methods=['GET','POST'])
def register():
    user=""
    if current_user.is_authenticated:
       return redirect('/')
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if Users.query.filter_by(email=email).first():
            return "Email Already Exists"
        
        user = Users(email=email,username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'thanku'
    return render_template('register.html', user=user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
    # return redirect('/register')













app.run(debug=True)




