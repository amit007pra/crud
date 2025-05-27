from flask import Blueprint, request, render_template, redirect
from .models import db, Item

main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@main.route('/add', methods=['POST'])
def add():
    new_item = Item(name=request.form['name'])
    db.session.add(new_item)
    db.session.commit()
    return redirect('/')
