import datetime
from flask import url_for
from truflr import db


class Route(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    steps = db.ListField(db.EmbeddedDocumentField('Step')
    variables = db.ListField(db.EmbeddedDocumentField('Variable')

    meta = {
        'allow_inheritance': True,
        'indexes': ['slug'],
        'ordering': ['slug']}

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

class Step(db.EmbeddedDocument):
    meta = {
        'allow_inheritance': True,
        }

class ForStep(Step):
    variables = db.ListField(db.EmbeddedDocumentField('Variable'))
    steps = db.ListField(db.EmbeddedDocumentField('Step'))

    def __unicode__(self):
        return u'For each {variables}:'.format(variables=', '.join(variables)[:-2])

class URLStep(Step):
    url = db.StringField(required=True)

    def __unicode__(self):
        return u'Goto \'{url}\''.format(url=url)

class Variable(db.EmbeddedDocument):
    meta = {'allow_inheritance': True}
