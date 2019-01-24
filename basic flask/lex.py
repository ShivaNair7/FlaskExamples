from flask import Flask,render_template
app = Flask (__name__)
@app.route('/')
def index():
    subject=['maths','c','java']
    marks=['80', '70' , '60']
    
    return render_template('tmp.html', subject = subject , marks = marks)
     
if __name__ == "__main__":
    app.run()    
            
