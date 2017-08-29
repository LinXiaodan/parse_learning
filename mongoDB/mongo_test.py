#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-24
# Author: LXD

import pymongo

import logging
logging.basicConfig(level=logging.INFO)

conn = pymongo.MongoClient(host='localhost', port=27017)

coll = conn.mongo_learning.table1
coll.drop()

coll.insert([{'id': '001', 'name': 'test1'}, {'id': '002', 'name': 'test3'}, {'id': '003', 'name': 'test2'}])

for i in coll.find():
    logging.info(i)

coll.ensure_index([('name', pymongo.ASCENDING)], unique=True)

for i in coll.find():
    logging.info(i)