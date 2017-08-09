# -*- coding: utf-8 -*-

"""
    exceptions
    ~~~~~~~~~~
    copyright: (c) 2017 Beijing ShiJingShan Government. All Rights Reserved
"""


errors = {
    '10001': 'missing request parameter {}'
}


class InvalidUsage(Exception):
    def __init__(self, code, msg):
        super().__init__(self)

        self.code = code
        self.msg = msg

    def to_dict(self):
        rv = dict(code=self.code, msg=self.msg)
        return rv
