from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from models import Conversation, Message
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
        newName = request.get_json()['name']
        if newName in [convo.name for convo in current_user.conversations]:
            return jsonify({'status': 'fail'})
        else :
            newConv = Conversation(name=newName, user_id=current_user.id)
            db.session.add(newConv)
            db.session.commit()
            return jsonify({'status': 'success'})
        
@exchange.route('/api/del+conversations/<id>', methods=["DELETE"])
@login_required
def delete_conv(id):
    conv = Conversation.query.get(id)
    if conv:
        db.session.delete(conv)
        db.session.commit()
        return jsonify({'status': 'success'})
    else:   
        return jsonify({'status': 'fail'})

@exchange.route('/api/messages', methods=['GET', 'POST'])
def messages():
    if request.method=='GET':
        conv = Conversation.query.get(request.args.get("id"))
        messages = { msg.id : msg.text for msg in conv.messages }
        return jsonify({'status': 'success', 'messages': messages})
    else:
        newMsg = Message(text=request.get_json()['text'], conversation_id=request.get_json()['id_conv'])
        db.session.add(newMsg)
        db.session.commit()
        return jsonify({'status': 'success'})