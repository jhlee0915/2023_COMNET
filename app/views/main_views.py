from flask import Blueprint, request, render_template, url_for
from werkzeug.utils import redirect
from .. import db
from ..models import User
from app.forms import LoginForm


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form =form)



@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()

    if request.method == 'POST':#  and form.validate_on_submit():
        user = User(username=form.UserId.data, password=form.UserPassword.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(''))
    if request.method == 'GET':
        return render_template('register.html', form = form)


@bp.route('/')
def index():
    return 'index'
