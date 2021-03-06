#!/usr/bin/python3

import os
import time
import psutil
import signal
import argparse
import subprocess
import matplotlib
import matplotlib.pyplot as plt

runtime = 60 * 4

def run_scratch(cmd):

    rssusage = []
    ussusage = []
    pssusage = []

    env = os.environ.copy()
    env["DISPLAY"] = ":0.0"
    pid = subprocess.Popen([cmd],env=env).pid
    timecounter = 0 
    
    while True:
        current_process = psutil.Process(pid)

        rss = current_process.memory_full_info().rss
        uss = current_process.memory_full_info().uss
        pss = current_process.memory_full_info().pss

        for child in current_process.children(recursive=True):
            rss += child.memory_full_info().rss
            uss += child.memory_full_info().uss
            pss += child.memory_full_info().pss

        rssusage.append(rss/1024/1024)
        ussusage.append(uss/1024/1024)
        pssusage.append(pss/1024/1024)
        
        print("Memory ",pss/1024/1024,"MB")

        time.sleep(1)
        timecounter += 1

        if timecounter > runtime:
            break

    os.kill(pid, signal.SIGSTOP)
    return (rssusage,ussusage,pssusage)

if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description="Profile scratch")
    parser.add_argument(
        "--cmd",
        dest="cmd",
        type=str,
        help="Command to run",
        required=True,
    )
    parser.add_argument(
        "--out",
        dest="out",
        type=str,
        help="Filename to output graph",
        required=True,
    )

    args = parser.parse_args()
    rss,uss,pss = run_scratch(args.cmd)

    fig, ax = plt.subplots()
    ax.plot(range(len(rss)), rss, label="RSS")
    ax.plot(range(len(uss)), uss, label="USS")
    ax.plot(range(len(pss)), pss, label="PSS")

    ax.set(xlabel='time (s)', ylabel='Memory (MB)',
       title='Memory usage of scratch')
    ax.grid()
    ax.legend()

    fig.savefig(args.out)

    print("Peak PSS %fMB" % (max(pss)))
