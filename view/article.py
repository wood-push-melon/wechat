# -*- coding: utf-8 -*-

"""
    article view
    ~~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from flask import request, jsonify, Blueprint

# from model.article import Article
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
                body=article.body,
                images=[i.url for i in article.images])

    return jsonify(code=0, data=resp)


@article.route('/list', methods=['GET'])
def get_article_list():
    """ return list of news """

    top = request.args.get('top', 5)

    news = Article.query.filter(
        Article.category == 'news'
    ).order_by(Article.modify_timestamp.desc()).limit(top)

    resp = [dict(id=n.id,
                 title=n.title,
                 url=n.url,
                 page=n.page,
                 images=[i.url for i in n.images if i.location == 'out'])
            for n in news]

    return jsonify(code=0, data=resp)
