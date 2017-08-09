# -*- coding: utf-8 -*-

"""
    image mapper
    ~~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from extension import db


class Image(db.Model):
    """image table"""

    __tablename__ = 'image'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    article_id = db.Column(db.SmallInteger, db.ForeignKey('article.id'))
    location = db.Column(db.Enum('in', 'out'))
    url = db.Column(db.String)
    create_timestamp = db.Column(db.TIMESTAMP)
    modify_timestamp = db.Column(db.TIMESTAMP)
