import re

class Share:
    num = 0
    cookie = None
    @classmethod
    def progress(cls):
        Share.num += 1
        print("{}/2000".format(Share.num))

pattern = "name=\"csrf\" value=\"\w*\""
repatter = re.compile(pattern)
