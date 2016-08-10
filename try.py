#!/usr/bin/env python3

#####
#
# Title: try.py
# Author: Dan Clegg
# Copyright: 2016, Dan Clegg
# LICENSE: Apache 2.0
#
#####

import sys
from CASClient import CASClient

# Instantiate a CAS client
client = CASClient(username="danclegg")
print("The Ticket Granting Ticket is: %s" % client.tgt.value)

# Dispose of client
client.__exit__()
