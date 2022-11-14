from _2FA_SubStage import get_login2, post_login2


def second(conn, headers, params, k):
    csrf = get_login2(conn, headers)
    #print(csrf)
    params = "csrf=" + csrf

    params += "&mfa-code={:04d}".format(k)
    #print(params)
    post_login2(conn, params, headers, k)
