from flask import Flask,request,jsonify
import requests,json

app=Flask(__name__)

def conversion(height,weight):
 result={}
 weightinkg=weight/1000
 heightinm=height*0.31
 result["weight"]=weightinkg
 result["height"]=heightinm
 return(result)
 
@app.route('/conversion',methods=['POST'])

def bmiconversion():
 inp=request.get_json()
 name=inp['name']
 weight=inp['weight']
 height=inp['height']
 conversionresult=conversion(height,weight)
 url='http://127.0.0.1:5002/bmi'
 payload=json.dumps({"weight" : conversionresult['weight'],
                     "height" : conversionresult['height']
                     })
 headers={'content-type' : 'application/json'}
 response=requests.request("POST",url,headers=headers,data=payload)
 next_response=json.loads(response.text)
 return(jsonify({'name':name + ' your bmi is '+next_response["category"]}))
 
 
 
if __name__== ("__main__"):
 app.run(host='0.0.0.0',port=5001,debug=True)
