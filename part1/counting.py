# part1_counting.py
# Given a list of urls, print out the top 3 frequent filenames.
# e.g.
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
# The program should print out
# a.txt 3
# b.txt 2
# c.jpg 2

import re 

pattern = r'.*\/(?P<name>.*\.\w*?)$'
file_names = {}

for url in urls:
    file = re.match(pattern, url).group("name")
    if file in file_names:
        file_names[file] += 1
    else:
        file_names[file] = 1

for file in sorted(file_names.items(), key=lambda obj: obj[1], reverse=True)[:3]:
    print("%s %s"%(file[0], file[1]))