import json

import webapp2

from review import Review
from review_util import review_properties


class ReviewsForProductHandler(webapp2.RequestHandler):
    def get(self, product_id):
        pass


class ReviewsForMemberHandler(webapp2.RequestHandler):
    def get(self, member_id):
        pass


class ReviewHandler(webapp2.RequestHandler):

    def post(self, product_id, member_id):
        json_string = self.request.body
        review_props = review_properties(json_string)
        new_review = Review(
            product_id=product_id,
            member_id=member_id,
            time=review_props["time"],
            rating=review_props["rating"],
            summary=review_props["summary"],
            text=review_props["text"]
        )

        new_review.put()

        json_response_dict = new_review.to_dict()

        # This dictionary is not quite ready to serialize into JSON because JSON has no native datetime type.
        # It is common in JSON to use an ISO 8601 datetime string with Z (representing GMT/UT) as the timezone.
        # Such a datetime looks like: "2016-10-04T18:55:11Z". Therefore we make that substitution (including the
        # trailing "Z" which is not optional, but the library leaves it off because conventionally python does
        # not distinguish between offsetless datetimes and UTC datetimes (a datetime with an offset that is 0).
        json_response_dict["time"] = json_response_dict["time"].isoformat() + "Z"
        # Now we can dump into valid json.
        json_response_string = json.dumps(json_response_dict)
        # Set the response type and write the json.
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json_response_string)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/product/<product_id>/reviews', handler=ReviewsForProductHandler, name='reviews-for-product'),
    webapp2.Route(r'/member/<member_id>/reviews', handler=ReviewsForMemberHandler, name='reviews-for-member'),
    webapp2.Route(r'/product/<product_id>/member/<member_id>', handler=ReviewHandler, name='review'),
])
