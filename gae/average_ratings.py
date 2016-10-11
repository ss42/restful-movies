
import webapp2


class AverageRatingsHandler(webapp2.RequestHandler):

    def post(self):

        # Part I of October 18th's homework goes here.
        # What this method should do is calculate the average rating for the product
        # specified in the payload. That will involve fetching all the ratings for the product,
        # and then summing the individual ratings up and dividing by the total number.
        # Finally you will need to get the Product object from the datastore (see product.py),
        # and update the average rating (or if there is no Product object, make it first).

        # Part II of October 18th's homework is to understand what Professor Ng in his free
        # Coursera course lectured on regarding recommender systems. The URL for the first of the
        # lectures is https://www.coursera.org/learn/machine-learning/lecture/Rhg6r/problem-formulation
        #
        # We will use this theory to implement our recommender system. I have previously studied
        # the theory of latent dirichlet allocation, but I haven't watched these lectures or implemented
        # it, so I will be doing the independent study along with you.

        print("We're in the post for AverageRatingsHandler with payload " + self.request.body)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/_ah/queue/average-ratings', handler=AverageRatingsHandler, name='average-ratings-for-product'),
])
