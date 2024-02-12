from bs4 import BeautifulSoup
import requests
import config as cfg
from icmplib import ping


def check_ping():
    for p in cfg.PING:
        host = p['host']
        name = p['name']
        result = ping(host, count=2, timeout=2)
        if result.is_alive:
            print(f"{name} is alive")
        else:
            print(f"{name} is dead")
            send_sms("⚠️ Le serveur '" + name + "' + "+ (host) +" ne répond plus au ping ! ⚠️")


def check_http():
    for p in cfg.HTTP:
        host = p['host']
        name = p['name']
        try:
            r = requests.get(host, timeout=3)
            if r.status_code == 200:
                print(f"{name} is alive")
            else:
                print(f"{name} is dead")
                send_sms("⚠️ Le serveur '" + name + "' + "+ (host) +" ne répond plus au HTTP ! ⚠️")
        except requests.exceptions.RequestException as e:
            print(f"{name} is dead")
            send_sms("⚠️ Le serveur '" + name + "' + "+ (host) +" ne répond plus au HTTP ! ⚠️")


def responsechecksms(responsecode):
    match responsecode:
        case 200:
            print("SMS sent")
        case 400:
            print("A mandatory parameter is missing")
        case 402:
            print("Too much SMS have been sent in a short period of time")
        case 403:
            print("Service not enabled")
        case 500:
            print("Server error")
        case _:
            print("Error sending SMS")


def send_sms(msg):
    link = cfg.SMS['api_link'] + "?user=" + cfg.SMS['user'] + "&pass=" + cfg.SMS['pass'] + "&msg=" + msg
    response = requests.get(link)
    responsechecksms(response.status_code)


check_ping()
check_http()