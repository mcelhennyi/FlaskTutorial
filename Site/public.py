from flask import Blueprint, render_template, request

from Database import db
from Database.list_entry import ListEntry

mod = Blueprint('public', __name__, template_folder='templates')

data = "Paragraph text"


# Index
@mod.route('/')
def index():
    global data
    temp_data = request.args.get('new_text')
    if temp_data:
        data = temp_data
    return render_template('home.html', show_data=data)


@mod.route('/list')
def list_route():

    temp_data = request.args.get('item_name')
    if temp_data:
        title = str(temp_data).strip()
        existing = db.session.query(ListEntry).filter(ListEntry.title == title).first()
        if existing:
            db.session.delete(existing)
        else:
            new_item = ListEntry(title=title)
            db.session.add(new_item)

        db.session.commit()

    # query for items
    items = db.session.query(ListEntry).all()

    return render_template('list_view.html', list_items=items)
