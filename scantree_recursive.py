#!/usr/bin/env pipenv-shebang

from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/scantree/")
def scantree_wrapper():
    result = scan_path("d:/")
    # print(result)
    return render_template('scantree.html', result=result)


try:
    from os import scandir
except ImportError:
    from scandir import scandir  # use scandir PyPI module on Python < 3.5

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

def scan_path(path, limit=None):
    videos = []
    i=0
    try:
        for entry in scantree(path):
            if entry.name.endswith("mp4"): 
                videos.append(entry.path)
                if limit is not None:
                    print(f"I is {i}")
                    if i < limit: i += 1
                    else: break
    except OSError as e:
        print(e)
    return videos


if __name__ == '__main__':
    for i in scan_path((sys.argv[1] if len(sys.argv) > 1 else '.')):
        print(i)