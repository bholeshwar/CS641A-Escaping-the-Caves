# This code has been reused from previous year's

import requests
import json
import urllib3
from tqdm import tqdm
f2 = open("generated_outputs.txt","w")

with open("actual_inputs.txt","r") as f:
	for x in tqdm(f):
		x = x.rstrip()
		if not x:
			continue
		headers = {
			'Origin': 'https://172.27.26.181:9996',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
			'Content-Type': 'text/plain',
			'Accept': '*/*',
			'Referer': 'https://172.27.26.163:9999/game/caves.swf',
			'X-Requested-With': 'ShockwaveFlash/32.0.0.142',
			'Connection': 'keep-alive',
		}
		data = '{"password":"9ed6d0d0a21f329deee082d56fc58b40","teamname":"Sherlocked","plaintext":"'+str(x)+'"}'
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		response = requests.post('https://172.27.26.181:9996/des', headers=headers, data=data, verify=False)
		json_data = json.loads(response.content)
		f2.write(json_data["ciphertext"])
		f2.write("\n")
f.close()
