from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def create_user():
   print "Got Post Info"  
   print request.form
   name = request.form['name']
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) 