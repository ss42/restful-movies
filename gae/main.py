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
            review_time=review_props["review_time"],
            overall=review_props["overall"],
            summary=review_props["summary"],
            text=review_props["text"]
        )

        new_review.put()

        json_response_dict = new_review.to_dict()
        json_response_string = json.dumps(json_response_dict)
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json_response_string)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/product/<product_id>/reviews', handler=ReviewsForProductHandler, name='reviews-for-product'),
    webapp2.Route(r'/member/<reviewer_id>/reviews', handler=ReviewsForMemberHandler, name='reviews-for-member'),
    webapp2.Route(r'/review/<product_id>/member/<reviewer_id>', handler=ReviewHandler, name='review'),
])
