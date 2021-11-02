import json
from datetime import datetime

def app(env, start_response):
	cur_time = datetime.now()
	data = {
		"time": str(cur_time),
		"url": env["HTTP_HOST"]
	}
	json_string = json.dumps(data)
	json_data = bytes(json_string, encoding='utf8')
	start_response('200 OK', [('Content-Type', 'application/json'),
				("Content-Length", str(len(json_data)))])
	return iter([json_data])
