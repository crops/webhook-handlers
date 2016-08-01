#!/usr/bin/env python

import json
import os
import sys
import subprocess

hook_loc = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(sys.argv[1], "payload")) as f:
    data = json.load(f)

    branches = data["branches"]

    if "halstead/tmp" in branches:
        subprocess.call(os.path.join(hook_loc, "trigger-travis.sh"))
