#!/usr/bin/python3

import os
import time
import psutil
import subprocess

env = os.environ.copy()
env["DISPLAY"] = ":0.0"
pid = subprocess.Popen(["scratch3"],env=env).pid

while True:
    current_process = psutil.Process(pid)
    mem = current_process.memory_full_info().rss
    for child in current_process.children(recursive=True):
        mem += child.memory_full_info().rss
    print(mem/1024/1024)
    time.sleep(1)
