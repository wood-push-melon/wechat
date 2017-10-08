# -*- coding: utf-8 -*-

"""
    search view
    ~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from flask import request, jsonify, Blueprint
from sqlalchemy import or_

from model import Article
from util.exceptions import errors, InvalidUsage


search = Blueprint('search', __name__)


@search.route('', methods=['GET'])
def search_articles():
    """
    search articles in title or body
    """

    keyword = request.args.get('keyword', '')
    if not keyword:
        raise InvalidUsage(10001, errors['10001'].format(keyword))

    cond = u'%{}%'.format(keyword)
    matches = Article.query.filter(
        or_(Article.title.like(cond), Article.body.like(cond))
    ).order_by(Article.modify_timestamp.desc()).all()

    formatted_keyword = '<p><em1>' + keyword + '</em1></p>'
    for m in matches:
        idx = m.body.find(keyword) if m.body else -1
        m.match = m.body[max(0, idx-20):idx+20].replace('\r\n', '') + '...' \
            if idx > 0 else ''

    resp = [dict(id=m.id,
                 title=m.title,
                 url=m.url,
                 match = m.match,
                 images=[i.url for i in m.images if i.location == 'out'],
                 num_img=len(m.images))
            for m in matches]

    return jsonify(code=0, data=resp)


@search.errorhandler(InvalidUsage)
def invalidhandler(error):
    return jsonify(error.to_dict())
