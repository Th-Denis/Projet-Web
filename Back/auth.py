from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from werkzeug.security \
    import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, \
    login_required, current_user
from __init__ import db

auth = Blueprint('auth', __name__)  # create a Blueprint object that
# we name 'auth'


@auth.route('/api/login', methods=['POST'])  # define login page path
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    user = User.query.filter_by(email=email).first()

    if not user:
        flash('Please sign up before!')
        return jsonify({'status': 'no user'})
    elif not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return jsonify({'status': 'wrong password'})
    
    login_user(user, remember=False)
    return jsonify({'status': 'success'})


@auth.route('/api/signup', methods=['POST']) 
def signup():  
        email = request.get_json()['email']
        name = request.get_json()['name']
        password = request.get_json()['password']
        user = User.query.filter_by(email=email).first()  
        if user: 
            flash('Email address already exists')
            return jsonify({'status': 'Email address already exists'})
        new_user = User(email=email, name=name,
                        password=generate_password_hash(password,
                                                        method='sha256')) 
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status': 'success'})


@auth.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'status': 'success'})

@auth.route('/api/status')
def userStatus():
    try: 
        current_user.id
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'fail'})