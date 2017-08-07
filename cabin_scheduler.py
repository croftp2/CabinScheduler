#!/usr/bin/python

#Paul Croft
#August 6, 2017

from bottle import get, post, redirect, request, run, static_file, template

from pprint import pformat, pprint
from sqlite3 import connect
from time import strftime, localtime, time

conn = connect("reservations.db")
c = conn.cursor()

@get("/ink/<filename:path>")
def css_files(filename):

    return static_file(filename, root="ink/")

@get("/")
def main_page():
    today_seconds = time()
    next_twelve_months = [strftime("%b %Y", localtime(today_seconds + i * 86400)) for i in range(370) ]
#    print next_twelve_months
    reducer = []
    while len(reducer) < 12:
        temp = next_twelve_months.pop(0)
        if temp not in reducer:
            reducer.append(temp)
    print reducer
    return template("welcome.html")

def main():
    c.execute("CREATE TABLE IF NOT EXISTS reservations (user TEXT, start TEXT, finish TEXT)")
    run(host="0.0.0.0", port=31245, debug=True)

if __name__ == '__main__':
    exit(main())