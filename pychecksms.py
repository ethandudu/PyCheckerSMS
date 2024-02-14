import time
import requests
from icmplib import ping


def check_ping(host, name, maxtry, timeout):
    trycnt = 0
    for i in range(maxtry):
        print(f"Trying to ping {name} ({host}) for the {i+1} time")
        result = ping(host, count=2, timeout=2)
        if result.is_alive:
            print(f"{name} is alive")
            break
        else:
            trycnt += 1
            time.sleep(timeout)
    if trycnt == maxtry:
        print(f"{name} is dead")
        send_sms("⚠️ Le serveur '" + name + "' + (" + host + ") ne répond plus au ping après " + str(maxtry) + " essais ! ⚠️")


def check_http(host, name, maxtry, timeout):
    trycnt = 0
    for i in range(maxtry):
        print(f"Trying to reach {name} ({host}) for the {i+1} time")
        try:
            r = requests.get(host, timeout=3)
            if r.status_code == 200:
                print(f"{name} is alive")
                break
            else:
                trycnt += 1
                time.sleep(timeout)
        except requests.exceptions.RequestException as e:
            trycnt += 1

    if trycnt == maxtry:
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


def send_sms(cfg, msg):
    link = cfg.SMS['api_link'] + "?user=" + cfg.SMS['user'] + "&pass=" + cfg.SMS['pass'] + "&msg=" + msg
    response = requests.get(link)
    responsechecksms(response.status_code)
