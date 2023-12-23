from flask import Flask,render_template

app= Flask(__name__)

JOBS=[
  {
  'id': 1,
  'title':'Data Analyst',
  'location':'Bengaluru,India',
  'salary':"Rs. 10,00,000"  
  }, 
  {
    'id': 2,
    'title':'Data Scientist',
    'location':'Delhi,India'
   

  },
{
  'id': 1,
  'title':'Frontend developer',
  'location':'Remote',
   'salary':"Rs. 12,00,000"

},
{
  'id': 1,
  'title':'Backend developer',
  'location':'San Francisco',
   'salary':"$120,000"

},
  
]


@app.route("/")

def hello():
  return render_template("home.html",jobs=JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  
  