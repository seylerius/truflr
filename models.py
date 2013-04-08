import datetime
from flask import url_for
from dataroomba import db


class Route(db.document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    steps = db.ListField(db.EmbeddedDocumentField('Step')
    
    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})
    
    def __unicode__(self):
        return self.title
    
    meta = {
        'allow_inheritance': True,
        'indexes': ['slug'],
        'ordering': ['slug']}