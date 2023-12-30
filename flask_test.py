from falsk import Flask, request
import os
import time
import json


app = Flask(__name__)

@app.route("/", defaults={'path':''})
@app.route(/<path:path>, methods=['POST', 'GET'])
def default_route():
   request_data = ""
   request_args = ""
   request_form = ""

   try:
       request_data = json.dumps(request.get_json())
   except:
       pass

   try:
       request_args = json.dumps(request.args)
   except:
       pass

   try:
       request_form = json.dumps(request.form)
   except:
       pass



   data = {
      "request_data": request_data,
      "request_args": request_args,
      "reqeust_form": request_form
   }

   print( json.dumps(data), flush=True )

   return "hello", 200




if __name__ == '__main__':
   port = 80
   app.run(host='127.0.0.1', port=80)












