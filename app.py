import os
from flask import Flask, request, redirect, render_template

#create app and allow for active debugging
app = Flask(__name__)
app.config['DEBUG'] = True

#establish url for and display home page
@app.route('/')
def index_home():
    return render_template('home.html', title="Well Hello")

#establish url path for line art
@app.route('/line_art', methods=['GET'])
def index_line_art():
    #display index.html from line_art folder
    return render_template('line_art/index.html', title="Line Art")

#establish url path for crocheted items list
@app.route('/yarntastic_adventures', methods=['GET'])
def index_crochet():
    #display available_creations.html
    return render_template('crochet/available_creations.html', title="Yarntastic Adventures")

#establish url path for Pride-O-Pusses
@app.route('/yarntastic_adventures/pride-o-pusses', methods=['GET'])
def index_prideopusses():
    #display pride-o-pusses.html
    return render_template('crochet/pride-o-pusses.html', title="Pride-O-Pusses")

#establish url path for Mini-Pusses
@app.route('/yarntastic_adventures/mini-pusses', methods=['GET'])
def index_minipusses():
    #display mini-pusses.html
    return render_template('crochet/mini-pusses.html', title="Mini-Pusses")

#establish url path for hats
@app.route('/yarntastic_adventures/hats', methods=['GET'])
def index_hats():
    #display hats.html
    return render_template('crochet/hats.html', title="Hats")

#establish url path for toys
@app.route('/yarntastic_adventures/toys', methods=['GET'])
def index_toys():
    #display toys.html
    return render_template('crochet/toys.html', title="Toys")

#establish url for custom order form
@app.route('/yarntastic_adventures/custom_order_form', methods=['POST','GET'])
def index_order_form():
    if request.method == 'GET':
	#display custom_order_form.html
	    return render_template('crochet/custom_order_form.html', title="Order Form")

#establish url for rats
@app.route('/rats', methods=['GET'])
def index_rats():
    #display index.html from rat folder
    return render_template('rats/index.html', title="Rat Babies")

#establish url for origin story of having rats
@app.route('/rats/origin_story', methods=['GET'])
def index_origin_story():
    if request.method == 'GET':
        #display origin_story.html
        return render_template('rats/origin_story.html', title="Origin Story")

#establish url for blog homepage
@app.route('/blogs', methods=['GET'])
def index_blog():
    #display blog_home.html
    return render_template('blog/blog_home.html', title="Blog Bonanza")

#establish url for religion blogs
@app.route('/blogs/religious_practices', methods=['GET'])
def index_blog_religion():
    #display 'blog_religion.html'
    return render_template('blog/blog_religion.html', title="Religious Explorations")

#establish url for origins blogs
@app.route('/blogs/origins', methods=['GET'])
def index_blog_origins():
    #display 'blog_origins.html'
    return render_template('blog/blog_origins.html', title="From Where?")

#establish url for terror blogs
@app.route('/blogs/terror', methods=['POST'])
def index_blog_terror():
    #display 'blog_terror.html'
    return render_template('/blog/blog_terror.html', title="RUN")

#establish url for about me section
@app.route('/about_me', methods=['GET'])
def index_about_me():
    #display 'about_me.html'
    return render_template('about_me/index.html', title="About Me")

	
if __name__ == '__main__':
    server_port = os.environ.get('PORT')
    if server_port is None:
        print("error: PORT environment variable not set")
        exit(1)

    app.run(debug=False, port=server_port, host='127.0.0.1')