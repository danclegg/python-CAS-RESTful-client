#!/usr/bin/env python3

#####
#
# Title: ST.py
# Author: Dan Clegg
# Copyright: 2016, Dan Clegg
# LICENSE: Apache 2.0
#
#####

import requests
import string
import urllib3.contrib.pyopenssl # Necessary to get around Python 3 ssl errors when calling an https endpoint
from parse import *
from lxml import etree

def POST(url,body):
	response = requests.post('%s' % url,data=body)
	data = response.text
	return data

class ST:
    service = None
    tgt = None
    value = None
    casServiceUrl=None

    def __init__(self,service,tgt,casServiceUrl):
        self.casServiceUrl = casServiceUrl
        self.service = service
        self.tgt = tgt
        self.value = POST('%s/tickets/%s' % (self.casServiceUrl,self.tgt),'service=%s' % self.service)
