

from google.appengine.ext import ndb


class Review(ndb.Model):
    """A model for representing an Amazon review."""
    product_id = ndb.StringProperty(indexed=True)
    member_id = ndb.StringProperty(indexed=True)
    review_time = ndb.DateTimeProperty(indexed=False)
    overall = ndb.FloatProperty(indexed=False)
    summary = ndb.StringProperty(indexed=False)
    text = ndb.TextProperty(indexed=False)
