from flask import Flask
# WSGI
app=Flask(__name__)

@app.route("/")
def home():
    return "welcome to the world"

if __name__=='__main__':
    app.run(debug=True)
    
          