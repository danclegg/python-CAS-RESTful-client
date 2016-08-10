#!/usr/bin/env python3

#####
#
# Title: CASClient.py
# Author: Dan Clegg
# Copyright: 2016, Dan Clegg
# LICENSE: Apache 2.0
#
#####

import requests
import string
import urllib3.contrib.pyopenssl
from parse import *
from lxml import etree
from TGT import TGT
from ST import ST

class CASClient:
    requestUrl = None
    requestBody = None
    requestMethod = None
    ticket = None
    username = None
    tgt = None
    requestST = None
    response = None
    casServiceUrl = None

    def __init__(self,username,casServiceUrl):
        self.username = username
        self.casServiceUrl = casServiceUrl
        self.tgt = TGT(username=self.username,casServiceUrl=self.casServiceUrl)

    def __enter__(self):
        return self

    def getST(self,tgt,service):
        s = ST(service=service,tgt=tgt)
        return s

    def GET(url):
        self.requestUrl = url
        self.requestST = getST(service=self.requestURL, tgt=self.tgt)
        response = requests.get('%s?ticket=%s' % (self.requestUrl,self.requestST))
        self.response = response.text

    def POST(url,body):
        self.requestUrl = url
        self.requestST = getST(service=self.requestURL, tgt=self.tgt)
        response = requests.post('%s?ticket=%s' % (self.requestUrl,self.requestST),data=body)
        self.response = response.text

    def PUT(url,body):
        self.requestUrl = url
        self.requestST = getST(service=self.requestURL, tgt=self.tgt)
        response = requests.put('%s?ticket=%s' % (self.requestUrl,self.requestST),data=body)
        self.response = response.text

    def DELETE(url,body):
        self.requestUrl = url
        self.requestST = getST(service=self.requestURL, tgt=self.tgt)
        response = requests.delete('%s?ticket=%s' % (self.requestUrl,self.requestST),data=body)
        self.response = response.text

    def DESTROY(self):
        self.requestUrl = "%s/%s" % (self.casServiceUrl,self.tgt)
        response = requests.delete(self.requestUrl)
        self.response = response.text

    def __exit__(self, exc_type, exc_value, traceback):
        self.DESTROY(self)
