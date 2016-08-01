#!/usr/bin/env python

import json
import os
import sys
import subprocess


with open(os.path.join(sys.argv[1], "payload")) as f:
    data = json.load(f)

    branches = data["branches"]

    if "halstead/tmp" in branches:
        subprocess.call("toaster-container-hook/trigger-travis.sh")
