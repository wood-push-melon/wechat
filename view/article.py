# -*- coding: utf-8 -*-

"""
    article view
    ~~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""

from flask import request, jsonify, Blueprint

from model import Article


article = Blueprint('article', __name__)


@article.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """ return details of one article """

    article = Article.query.filter(Article.id == article_id).one()

    resp = dict(id=article.id,
                title=article.title,
                url=article.url,
                page=article.page,
                body=article.html.replace('\\n', '\n').replace('\\"', '"'),
                images=[i.url for i in article.images],
                num_img=len(article.images))

    return jsonify(code=0, data=resp)


@article.route('/list', methods=['GET'])
def get_article_list():
    """ return list of articles """

    args = request.args
    page = int(args.get('page', 0))
    size = int(args.get('size', 10))
    category = args.get('key', '')

    if category:
        articles = Article.query.filter(
            Article.category == category
        ).order_by(Article.modify_timestamp.desc())
    else:
        articles = Article.query.order_by(
            Article.modify_timestamp.desc()).offset(page*size).limit(size)

    resp = [dict(id=n.id,
                 title=n.title,
                 url=n.url,
                 images=[i.url for i in n.images if i.location == 'out'],
                 num_img=len(n.images))
            for n in articles]

    return jsonify(code=0, data=resp)
