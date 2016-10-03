# A review comes to us in this form:

# {
#     "reviewerID": "A2SUAM1J3GNN3B",
#     "asin": "0000013714",
#     "reviewerName": "J. McDonald",
#     "helpful": [2, 3],
#     "reviewText": "I bought this for my husband who plays the piano.",
#     "overall": 5.0,
#     "summary": "Heavenly Highway Hymns",
#     "unixReviewTime": 1252800000,
#     "reviewTime": "09 13, 2009"
# }

# From this, we will store (or update) the following properties:

# member_id = ndb.KeyProperty(indexed=False)
# product_id = ndb.KeyProperty(indexed=False)
# review_time = ndb.DateTimeProperty(indexed=False)
# rating = ndb.FloatProperty(indexed=False)
# summary = ndb.StringProperty(indexed=False)
# text = ndb.TextProperty(indexed=False)

import json

from datetime import datetime


def review_properties(json_string):

    raw_props = json.loads(json_string)

    review_props = {}

    for key in raw_props.keys():

        value = raw_props[key]

        if key == "unixReviewTime":
            review_props["review_time"] = datetime.fromtimestamp(value)
        elif key == "overall":
            review_props["rating"] = value
        elif key == "summary":
            review_props["summary"] = value
        elif key == "reviewText":
            review_props["text"] = value
        else:
            pass

    return review_props
