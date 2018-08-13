import requests
import os
import random
import string
import json
import time
#import scam1

chars = string.ascii_letters + string.digits + '!@#$%^&*'
random.seed = (os.urandom(1024))

url = 'http://fenqxing.com/connectID.php'

decision = 0
passwd = 'qwerty123'
usern = 'admin'
xname = '01'
# admin01 - qwery123


names = json.loads(open('someNames.json').read())
passwds = json.loads(open('passwd.json').read())
theE = json.loads(open('emails.json').read())

def buildName(daName,daNum):
    pass

def buildExtra(daExtras,daNum):
    if (daNum < 5):
        daExtras = str(random.randint(0,9999))
    elif (daNum < 15):
        daExtras = str(random.randint(-100,0))
    elif (daNum < 40):
        daExtras = '_' + random.choice(names)
    elif (daNum < 60):
        daExtras = ''.join(random.choice(string.ascii_letters).lower() for i in range(random.randint(1,5)))
    else:
        daExtras = str(random.randint(10,999))

    return daExtras

def buildPass(daPass,daNum):
    if (daNum < 10):
        daPass = random.choice(passwds) + random.choice(names)
    elif (daNum < 20):
        daPass = random.choice(passwds) + ''.join(random.choice(chars) for i in range(3))
    else:
        daPass = random.choice(passwds) + ''.join(random.choice(string.digits) for i in range(2))

    return daPass



for name in names:
    #name_extra = ''.join(random.choice(string.digits)) + ''.join(random.choice(string.digits))

    # build a name
    decision = random.randint(0,100)
    #usern = buildName(name,decision).lower

    # build extras
    decision = random.randint(0,100)
    xname = buildExtra(xname,decision)

    # build a Password
    decision = random.randint(0,100)
    passwd = buildPass(passwd,decision)


    random_provider = random.choice(theE)

    username = name.lower() + xname + '@' + random_provider
    password = passwd # random.choice(passwds) + random.choice(names) #''.join(random.choice(string.digits) for i in range(2))
    # password = ''.join(random.choice(chars) for i in range(12))

    requests.post(url, allow_redirects=False, data={
        'username': username,
        'password': password
    })

    # print ('%s --  %s' % (username, password))

    # Beautiful, Clean output
    print('{0:25} @ {1:25} > {2:10}'.format(name.lower() + xname,random_provider, password))
