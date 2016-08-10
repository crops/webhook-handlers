#!/usr/bin/env python

import json
import os
import sys
import subprocess
import urllib2

def trigger_travis(branch, committish):
    message = "API triggered build... {}:{}".format(branch, committish)

    request = {}
    request["message"] = message
    request["branch"] = "master"

    data = {}
    data["request"] = request

    url = "https://api.travis-ci.org/repo/crops%2Ftoaster-container/requests"
    token = os.environ["TOASTER_CONTAINER_TOKEN"]
    headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Travis-API-Version": "3",
                "Authorization": "token {}".format(token)
              }
    url_request = urllib2.Request(url, json.dumps(data), headers)

    print url_request
    urllib2.urlopen(url_request)


important_branches = [ "master" ]

with open(os.path.join(sys.argv[1], "payload")) as f:
    data = json.load(f)

    branches = data["branches"]

    for branch in important_branches:
        try:
            index = branches.index(branch)
        except ValueError:
            continue

        committish = data["detail"][index]
        trigger_travis(branch, committish)
        break
