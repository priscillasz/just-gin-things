# app.py

from flask import Flask, render_template

app = Flask(__name__)

# show list
# just testing
@app.route('/')
def show_list():
    items = [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
        'Item 5',
        'Item 6',
        'Item 7',
        'Item 8',
        'Item 9',
        'Item 10'
    ]
    return render_template('list.html', items=items)

if __name__ == '__main__':
    app.run()
