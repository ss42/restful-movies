
import webapp2


class AverageRatingsHandler(webapp2.RequestHandler):

    def post(self, product_id):

        # PART II of this week's homework goes here. I have added queue.yaml to the project,
        # and added code to main.py and app.yaml. All of this code has to be checked against
        # Sanderson Chapter 16 before this method is likely to work. I am unclear on how the
        # payload (is meant to be passed).
        print("we're in the post for AverageRatingsHandler with product_id " + product_id)
        print("request body is  " + self.request.body)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/_ah/queue/average-ratings', handler=AverageRatingsHandler, name='average-ratings-for-product'),
])
