#!/usr/bin/env python3

import json
import os
import sys
import subprocess
from urllib.request import Request, urlopen

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
    url_request = Request(url, json.dumps(data).encode(), headers)

    urlopen(url_request)


important_branches = [ "master", "toaster-next", "krogoth" ]

with open(os.path.join(sys.argv[1], "payload")) as f:
    data = json.load(f)

    branches = data["branches"]

    for branch in important_branches:
        try:
            index = branches.index(branch)
        except ValueError:
            continue

        committish = data["detail"][index][1]
        trigger_travis(branch, committish)
        break
