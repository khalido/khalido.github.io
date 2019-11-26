"""reads and parses markdown files
"""

import os, re
from pathlib import Path
from ruamel.yaml import YAML

content = Path("content")
posts = content / "posts"

def get_file_list(path = posts):
    """takes in a pathlib path and returns list of all markdown files"""
    files = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                       for name in files
                           if name.endswith((".md"))]
    return files

def parse_file(filename):
    """takes a filename and returns yaml front matter in a dict and rendered html"""
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()
    
    # find the text b/w the --- strings
    pattern = re.compile(r"^---(.|\n)*?---")
    front = pattern.match(data)
    
    yaml=YAML(typ="safe")
    # remove the --- from start and end else yaml library fails
    front_matter = yaml.load(front[0][3:-3])
    post_md = data[front.end():]
    
    #html = CommonMark.commonmark(data[front.end():])
    return front_matter, post_md


def get_file_content(filename: str = "README.md"):
    """takes in a filename and returns the contents"""
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()
    return data


def get_files(path = posts):
    text = dict()
    frontmatter = dict()

    for file in get_file_list(path):
        filename = file.split("\\")[-1][:-3]
        front_matter, post_md = parse_file(file)
        text[filename] = post_md
        frontmatter[filename] = front_matter
                       
    return text, front_matter

def get_posts(path=posts):
    filelist = get_file_list(path)

    text = dict()
    tags = dict()

    for file in get_file_list(path):
        filename = file.split("\\")[-1][:-3]
        text[filename] = get_file_content(file)
                       
    return text, tags
