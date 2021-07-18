from flask import Flask,request,jsonify

app=Flask(__name__)

def category(bmi):
 result={}
 if bmi<18:
  result['category']='lean'
 elif bmi>18 and bmi<25:
  result['category']='normal'
 else:
  result['category']='obese'
 return(result)
	 

@app.route("/category",methods=['POST'])

def bmicategory():
	inp=request.get_json()
	bmi=inp["bmi"]
	bmicategory=category(bmi) 
	return (jsonify({"category":bmicategory['category']}))
	
	
if __name__==('__main__'):
 app.run(port=5003,debug=True)
