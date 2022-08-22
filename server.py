from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        data = request.form.to_dict()
        #print(data)
        flash('Message sent sucessfully!')
        return redirect('/contact.html')
    else:
        return redirect('/contact.html')

if __name__ == "__main__":
  app.run(debug=True)