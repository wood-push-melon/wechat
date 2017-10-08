# -*- coding: utf-8 -*-

"""
    article mapper
    ~~~~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from extension import db
from image import Image


class Article(db.Model):
    """article table"""

    __tablename__ = 'article'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    keyword = db.Column(db.String)
    category = db.Column(db.Enum('plan', 'project', 'qiaomengyuan', 'olympics',
                                 'dispersal', 'policy', 'assistant', 'finance',
                                 'history', 'campus'))
    url = db.Column(db.String)
    page = db.Column(db.SmallInteger)
    html = db.Column(db.Text)
    body = db.Column(db.Text)
    create_timestamp = db.Column(db.TIMESTAMP)
    modify_timestamp = db.Column(db.TIMESTAMP)

    images = db.relationship('Image', backref='article', lazy='joined')
