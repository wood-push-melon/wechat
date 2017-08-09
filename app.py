#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    application
    ~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


from flask import Flask

from view import article, search
from config import configs
from extension import db


app = Flask(__name__)
conf = configs.get('dev')
app.config.from_object(conf)

app.register_blueprint(article.article, url_prefix='/article')
app.register_blueprint(search.search, url_prefix='/search')

# extension
db.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=conf.SERVER_PORT)
