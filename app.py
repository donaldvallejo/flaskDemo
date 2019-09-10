from flask import Flask, request, render_template
from random import choice
from random import sample
app = Flask(__name__)


compliments = ['great', 'fantabulous', 'stellar', 'awesome', 'amazing']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')


@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments') == 'on'
    print('show_compliments:', show_compliments)
    num_compliments = int(request.args.get('num_compliments'))
    debug_str = ' '.join(map(str, ['num_compliments:', num_compliments, 'type:', type(num_compliments)]))
    print(debug_str)
    compliments_to_show = sample(compliments, num_compliments)
    print(compliments_to_show)

    return render_template(
        'compliments.html', 
        name=name, 
        show_compliments=show_compliments, 
        compliments=compliments_to_show)   