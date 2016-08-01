#!/usr/bin/env python

import json
import os
import sys
import subprocess

hook_loc = os.path.dirname(os.path.realpath(__file__))

important_branches = [ "halstead/tmp", "halstead/tmp2" ]

with open(os.path.join(sys.argv[1], "payload")) as f:
    data = json.load(f)

    branches = data["branches"]

    for branch in important_branches:
        if branch in branches:
            subprocess.call(os.path.join(hook_loc, "trigger-travis.sh"))
            break
