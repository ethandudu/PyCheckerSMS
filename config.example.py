# https://mobile.free.fr/account/mes-options/notifications-sms
SMS = {
    'api_link' : 'https://smsapi.free-mobile.fr/sendmsg',
    'user' : '00000000',
    'pass' : 'XXXXXX',
}

# Ping check
PING = [
    {
        'host' : '8.8.8.8',
        'name' : 'Google'
    },
    {
        'host' : '1.1.1.1',
        'name' : 'Cloudflare'
    }
]

# HTTP check
HTTP = [
    {
        'host' : 'https://google.com',
        'name' : 'Google'
    }
]