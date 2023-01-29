from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from models import Conversation
from flask_login import login_required, current_user
from __init__ import db

exchange = Blueprint('exchange', __name__)

@exchange.route('/api/conversations', methods=['GET', 'POST'])
@login_required
def conversations():
    conversations = { convo.id : convo.name for convo in current_user.conversations}
    
    if request.method=='GET':
        return jsonify({'status': 'success', 'conversations': conversations})
    else:
        newName = request.form.get('name')  
        print(type(newName))
        if newName in current_user.conversations:
            flash("Une de vos conversations porte déjà ce nom")
            return False
        else :
            newConv = Conversation(name=newName, user_id=current_user.id)
            db.session.add(newConv)
            db.session.commit()
            return True
    
@exchange.route('/api/messages', methods=['GET'])
def messages():
    convId = request.args.get("id")
    conversation = db.session.execute(db.select(Conversation).filter_by(id=convId).order_by(Conversation.id)).scalar_one()
    if request.method=='GET':
        messages = { msg.id : msg.text for msg in conversation.messages }
        return jsonify({'status': 'success', 'messages': messages})