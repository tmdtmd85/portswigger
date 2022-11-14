import urllib.parse
from _2FA_SubStage import get_login, post_login


def first(conn, headers, params):

    csrf, cookie = get_login(conn, headers)

    params["csrf"] = csrf
    params = urllib.parse.urlencode(params)
    #print(params)

    headers["Cookie"] = cookie
    #print(headers)

    cookie = post_login(conn, params, headers)

    #print(cookie)

    return cookie
