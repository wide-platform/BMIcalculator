from flask import Flask,request,jsonify
import json,requests

app=Flask(__name__)

def bmi(height,weight):
 result={}
 bmi=(weight/(height**2))
 result["bmi"]=bmi
 return result
 
@app.route('/bmi',methods=['POST'])

def bmicalculation():
 inp=request.get_json()
 weight=inp['weight']
 height=inp['height']
 bmiresult=bmi(height,weight)
 url='http://127.0.0.1:5003/category'
 payload=json.dumps({"bmi":bmiresult['bmi']})
 print(payload)
 headers={'content-type':'application/json'}
 response=requests.request("POST",url,headers=headers,data=payload)
 next_response=json.loads(response.text)
 return(jsonify({"category":next_response["category"]}))
    
if (__name__)==("__main__"):
 app.run(port=5002,debug=True)
