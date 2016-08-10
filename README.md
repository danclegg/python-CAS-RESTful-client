## Purpose
This project is an example of a python client for a CAS-secured web service.

## Common Variables
* _casServiceUrl_ -- the url to the JASIG CAS service, i.e. _https://someDomain/cas/_


See [try.py](https://github.com/danclegg/python-CAS-RESTful-client/blob/master/try.py) for examples

_Note:_ As stated in each class file, the urllib3.contrib.pyopenssl import was necessary to get around Python3-specific errors encountered when calling an SSL endpoint. (Kudos to all who contributed to [requests](https://github.com/kennethreitz/requests) [Issue 3006](https://github.com/kennethreitz/requests/issues/3006))
