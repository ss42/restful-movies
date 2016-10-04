
import json

import urllib2

DATA_FILE = "./amazon/Movies_and_TV_5-FIRST-10000.json"

URL_BASE = "http://localhost:8080/"

with open(DATA_FILE) as f:
    for json_line in f:
        raw_props = json.loads(json_line)
        product_id = raw_props["asin"]
        member_id = raw_props["reviewerID"]
        request_props = {
            "unixReviewTime": raw_props["unixReviewTime"],
            "overall": raw_props["overall"],
            "summary": raw_props["summary"],
            "reviewText": raw_props["reviewText"]
        }
        url = URL_BASE + "product/" + product_id + "/member/" + member_id
        req = urllib2.Request(url, data=json.dumps(request_props))
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req)
        response_data = response.read()
        print("response is " + response_data)
