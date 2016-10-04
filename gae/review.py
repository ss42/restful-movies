

from google.appengine.ext import ndb


class Review(ndb.Model):
    """A model for representing an Amazon review."""
    product_id = ndb.StringProperty(indexed=True)
    member_id = ndb.StringProperty(indexed=True)
    time = ndb.DateTimeProperty(indexed=False)
    rating = ndb.FloatProperty(indexed=False)
    summary = ndb.StringProperty(indexed=False)
    text = ndb.TextProperty(indexed=False)
