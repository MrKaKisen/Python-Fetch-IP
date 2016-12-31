# Made by Vilhelm Prytz 2016 (31st december!)
# Copyright 2016

print("IP fetch - Python - By Vilhelm Prytz (https://mrkakisen.se)")

from sys import version_info
py3 = version_info[0] > 2
if py3:
    import urllib.request
    req = urllib.request.Request("https://ip-api.mrkakisen.net/api/v1/plainText")
    ipFetch = urllib.request.urlopen(req)
    if ipFetch == None or ipFetch.getcode() != 200:
        print("Error! No connection to internet.")
    else:
        print("Your IP is: " + str(ipFetch.read()))
else:
    import urllib
    ipFetch = urllib.urlopen("https://ip-api.mrkakisen.net/api/v1/plainText")
    if ipFetch == None or ipFetch.getcode() != 200:
        print("Error! No connection to internet.")
    else:
        print("Your IP is: " + str(ipFetch.read()))
