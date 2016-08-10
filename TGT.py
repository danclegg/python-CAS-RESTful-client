#!/usr/bin/env python3

#####
#
# Title: TGT.py
# Author: Dan Clegg
# Copyright: 2016, Dan Clegg
# LICENSE: Apache 2.0
#
#####

import getpass
import requests
import string
import urllib3.contrib.pyopenssl # Necessary to get around Python 3 ssl errors when calling an https endpoint
from parse import *
from lxml import etree

def POST(url,body):
	response = requests.post('%s' % url,data=body)
	data = response.text
	return data

class TGT:
    value = None
    username=None
    password=None
    casServiceUrl=None

    def __init__(self,username,casServiceUrl):
        print("Please enter your password:")
        self.password = getpass.getpass()
        self.username = username
        d = POST('%s/tickets' % casServiceUrl,'username=%s&password=%s' % (self.username,self.password))
        data = etree.HTML(d)
        self.value="TGT"+data.xpath("substring-after(/html/body/form/@action,'TGT')")
