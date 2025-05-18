from flask import Blueprint
from flask import render_template,url_for,flash,redirect,request
from ManageSubscriptions import db,limiter
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.security import generate_password_hash,check_password_hash
from .forms import SupportForm,CustomPlan
from ManageSubscriptions.models import SupportMessages

forms_bp = Blueprint('forms', __name__)

@forms_bp.route('/support', methods=["GET","POST"])
@limiter.limit('3 per 60 minutes', methods="POST")
def support():
    form = SupportForm()
    if form.validate_on_submit():
        email = form.email.data
        full_name = form.full_name.data
        message = form.message.data
        new_message = SupportMessages(email=email,full_name=full_name,message=message,status=0)
        try:
            db.session.add(new_message)
            db.session.commit()
            flash('We recieved your message, and we\'ll reply ASAP.', 'success')
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('Failed to deliver your message, please try again!.', 'error')
        return redirect(url_for('forms.support'))
    return render_template('support.html', title='Subly - Support', form=form)

@forms_bp.route('/custom-plan', methods=["GET","POST"])
@limiter.limit('3 per 60 minutes', methods="POST")
@login_required
def custom_plan():
    form = CustomPlan()
    if form.validate_on_submit():
        requests = form.requests.data
        subscribers = form.subscribers.data
        try:
            int(requests)
            int(subscribers)
        except:
            flash('Values should be a numbers', 'error')
            return redirect(url_for('forms.custom_plan'))
        message = f'requests required : {requests}, subscribers required : {subscribers}'
        new_message = SupportMessages(email=current_user.email,full_name=current_user.name,message=message,status=0)
        flash('Your request reached us and we will reply within some hours.', 'success')
        return redirect(url_for('dashboards.dashboard'))
    return render_template('custom_plan.html', title='Subly - Custom Plan', form=form)
