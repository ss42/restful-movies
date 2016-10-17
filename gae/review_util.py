import json

from datetime import datetime


# Takes JSON reviews in the format they come in to our server and converts them to
# our dictionary format for reviews.
#
# This is the incoming format:
#
# {
#     "unixReviewTime": 1252800000,
#     "overall": 5.0,
#     "summary": "Heavenly Highway Hymns",
#     "reviewText": "I bought this for my husband who plays the piano.",
# }
#
# This is our internal format:
#
# time = ndb.DateTimeProperty(indexed=False)
# rating = ndb.FloatProperty(indexed=False)
# summary = ndb.StringProperty(indexed=False)
# text = ndb.TextProperty(indexed=False)
#
def review_properties(json_string):

    raw_props = json.loads(json_string)

    review_props = {}

    for key in raw_props.keys():

        value = raw_props[key]

        if key == "unixReviewTime":
            review_props["time"] = datetime.fromtimestamp(value)
        elif key == "overall":
            review_props["rating"] = value
        elif key == "summary":
            review_props["summary"] = value
        elif key == "reviewText":
            review_props["text"] = value
        else:
            pass

    return review_props


# Takes an array of reviews and writes them as JSON to the writable object.
def write_reviews(reviews, writable):

    first_result = True

    for review in reviews:
        if first_result:
            writable.write('{\n    "reviews" : [\n')
            first_result = False
        else:
            writable.write(',\n')

        json_response_dict = review.to_dict()
        json_response_dict["time"] = json_response_dict["time"].isoformat() + "Z"
        json_response_string = json.dumps(json_response_dict)
        writable.write('        ')
        writable.write(json_response_string)

    writable.write('\n    ]\n}\n')
