import pychecksms

HTTP = [
    {
        'host': 'https://google.com',
        'name': 'Google',
        'maxtry': 3,
        'timeout': 10
    }
]

PING = [
    {
        'host': '1.1.1.1',
        'name': 'Cloudflare DNS',
        'maxtry': 3,
        'timeout': 10
    }
]

cfg = {
    'api_link': 'https://smsapi.free-mobile.fr/sendmsg',
    'user': '00000',
    'pass': 'PASSWORD',
}


def main():
    for i in PING:
        pychecksms.check_ping(i['host'], i['name'], i['maxtry'], i['timeout'])
    for i in HTTP:
        pychecksms.check_http(i['host'], i['name'], i['maxtry'], i['timeout'])


if __name__ == "__main__":
    main()
