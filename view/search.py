# -*- coding: utf-8 -*-

"""
    search view
    ~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from flask import request, jsonify, Blueprint

from model import Article
from util.exceptions import errors, InvalidUsage


search = Blueprint('search', __name__)


@search.route('/', methods=['GET'])
def search_articles():
    """
    search articles in title or keywords
    """

    keyword = request.args.get('keyword', '')
    if not keyword:
        raise InvalidUsage(10001, errors['10001'].format(keyword))

    matches = Article.query.filter(
        Article.title.like(u'%{}%'.format(keyword))
    ).order_by(Article.modify_timestamp.desc()).all()

    if not matches:
        matches = Article.query.filter(
            Article.keyword.like(u'%{}%'.format(keyword))
        ).order_by(Article.modify_timestamp.desc()).all()

    resp = [dict(id=m.id,
                 title=m.title,
                 url=m.url,
                 page=m.page,
                 body=m.body,
                 images=[i.url for i in m.images if i.location == 'out'])
            for m in matches]

    return jsonify(code=0, data=resp)


@search.errorhandler(InvalidUsage)
def invalidhandler(error):
    return jsonify(error.to_dict())
