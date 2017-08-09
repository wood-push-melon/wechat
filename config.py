# -*- coding: utf-8 -*-

"""
    configuration
    ~~~~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


class Config(object):
    DEBUG = True
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_PORT = 5000


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/wechat?charset=utf8'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ('mysql://root@127.0.0.1:3306/wechat?'
                               'charset=utf8')


configs = dict(dev=DevConfig, prod=ProdConfig)
