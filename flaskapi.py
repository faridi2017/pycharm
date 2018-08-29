import requests
import json
from flask import Flask, jsonify

import time

app = Flask(__name__)
print('Aarif python Api running on http://192.168.1.10:5000/myapi/tasks')
#122.177.36.41
finalUrl = '192.168.1.10'
url = '122.177.36.41'
serverPort = 5000

url2 = 'http://api.victorcalls.com/api/Leads/Company?username=vedagya19&statusid=4'
urlResponse2 = requests.get(url2)
#time.sleep(5)
jData2 = json.loads(urlResponse2.content)
#time.sleep(3)
print('follow Up leads:', len(jData2))

@app.route('/myapi/tasks', methods=['GET'])
def getObjectsList():
	jTenData = 'success'
	return jsonify(jData2)


if __name__ == '__main__':
    app.run(host=finalUrl,port=serverPort,debug=True, use_reloader=False)
