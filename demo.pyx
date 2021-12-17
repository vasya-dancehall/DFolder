from requests import get
import json

cdef public char * open(char * url):
    content=get(url).json()
    return content