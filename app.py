from flask import Flask, render_template,request
import scapper

app=Flask("My Application")

@app.route('/', methods=['GET','POST'])
def index():
    products=[]
    m=[]
    if request.method=="POST":
        query=request.form['query']
        products=scapper.scrap(query)
    return render_template('index.html',products=products)
if __name__=="__main__":
    app.run(port=8081, debug= True)

