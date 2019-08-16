from flask import Flask, request, redirect, render_template


#create app and allow for active debugging
app = Flask(__name__)
app.config['DEBUG'] = True

#establish url for and display home page
@app.route('/')
def index_home():
    return render_template('home.html', title="Well Hello")

#establish url path for crocheted items list
@app.route('/crochet', methods=['GET'])
def index_crochet():
    #display pre-made_items.html
    return render_template('crochet/available_creations.html', title="Yarntastic Adventures")

#establish url for custom order form
@app.route('/crochet/custom_order_form', methods=['POST','GET'])
def index_order_form():
    if request.method == 'GET':
	#display custom_order_form.html
	    return render_template('crochet/custom_order_form.html', title="Order Form")

#establish url for rats
@app.route('/rats', methods=['GET'])
def index_rats():
    #display index.html from rat folder
    return render_template('rats/index.html', title="Rat Babies")

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
	

app.run()