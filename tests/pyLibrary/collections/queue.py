
# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Kyle Lahnakoski (kyle@lahnakoski.com)
#

from __future__ import unicode_literals
from __future__ import division


class Queue(object):
    """
    A SET WITH ADDED ORDER MAINTAINED

    +------------+---------+----------+
    | Uniqueness | Ordered | Type     |
    +------------+---------+----------+
    |     Yes    |   Yes   | Queue    |
    |     Yes    |   No    | Set      |
    |     No     |   Yes   | List     |
    |     No     |   No    | Multiset |
    +------------+---------+----------+
    """
    def __init__(self):
        self.list = []

    def __nonzero__(self):
        return len(self.list) > 0

    def __len__(self):
        return self.list.__len__()

    def add(self, value):
        if value in self.list:
            return self
        self.list.append(value)

    def extend(self, values):
        for v in values:
            self.add(v)

    def pop(self):
        if len(self.list) == 0:
            return None

        output = self.list.pop(0)
        return output

