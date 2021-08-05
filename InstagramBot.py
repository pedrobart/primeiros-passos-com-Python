# coding=utf-8
# !/usr/bin/env python3

from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []


def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )

    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")


def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )

        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Loading users!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Loading Proxys!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("username perfil:")
    userid = GetInput("numero do perfil:")
    useproxy = GetInput("proxy? [Yes No]:")
    if (useproxy == "Yes"):
        useproxy = True
    elif (useproxy == "No"):
        useproxy = False
    else:
        PrintFatalError(" 'Yes' or 'No'!")
        exit(0)
    usemultithread = GetInput(
        "multithreading? [Yes / No] (desligar se o pc lagar!):")

    if (usemultithread == "Yes"):
        usemultithread = True
    elif (usemultithread == "No"):
        usemultithread = False
    else:
        PrintFatalError(" 'Yes' or 'No'!")
        exit(0)

    PrintChoices()
    reasonid = GetInput("razão do report (ex: 1 = spam):")

    print("")
    PrintStatus("Starting!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                        args=(username,
                              userid,
                              user["user"],
                              user["password"],
                              None if useproxy == False else choice(PROXIES),
                              reasonid
                              )
                        )
            p.start()