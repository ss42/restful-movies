

from google.appengine.ext import ndb


class Product(ndb.Model):
    """A model for representing an Amazon product."""
    product_id = ndb.StringProperty(indexed=True)
    average_rating = ndb.FloatProperty(indexed=False)
