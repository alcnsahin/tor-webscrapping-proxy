import time
import requests
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent

TORR_HOST = "127.0.0.1"
TORR_PORT = 9050

headers = {
    "user-agent": UserAgent().random
}


def renew_session():
    session = requests.session()
    session.proxies['http'] = 'socks5://' + TORR_HOST + ':' + str(TORR_PORT)
    session.proxies['https'] = 'socks5://' + TORR_HOST + ':' + str(TORR_PORT)
    return session


def change_ip_address():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="3.14xyz*")
        controller.signal(Signal.NEWNYM)
        time.sleep(controller.get_newnym_wait())
    print("IP changed...")


while True:
    print(renew_session().get("http://icanhazip.com/", headers=headers).text)
    change_ip_address()
    time.sleep(1)


