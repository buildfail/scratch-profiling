# scratch-profiling

Scripts for profiling scratch memory usage etc.

Makes use of python + psutil to obtain memory usage recursively for a particular spawned process.

# Usage

To examine memory usage:

```
sudo apt install python3-matplotlib
./memory.py --cmd scratch3 --out graph.png
```

To examine files from the ASAR:

```
npx asar extract app.asar unpacked
./asar_investigate.py --in unpacked/1.bundle.js
```

# Examples

I believe now that USS gives a more accurate measure of memory utilised when summed for child processes than RSS, as 
I ran 'free -m' while Scratch was running and after, and the difference was around 350MB, which is much closer to the USS value.

## Scratch3 Raspbian Version

![scratch3 memory](images/memory-scratch3.png)


## Scratch3 New Version

![scratch3 memory](images/memory-scratch3new.png)

# To Do

* Investigate ASAR contents
* Profile memory usage
