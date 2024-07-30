#!/usr/bin/env python2
# Author: Santosh Bhandari

from fabric.api import *

env.user = 'sbhandari25-ops'
env.hosts = ['172.20.190.1']

def getHostname():
    name = run("hostname")
    print("The host name is:", name)

def installPackage(pkg='dummy'):
    cmd = 'sudo apt-get install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def removePackage(pkg=''):
    if pkg == '':
        cmd = 'sudo apt-get remove dummy -y'
    else:
        cmd = 'sudo apt-get remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def updatePackage(pkg=''):
    if pkg == '':
        cmd = 'sudo apt-get update && sudo apt-get upgrade -y'
    else:
        cmd = 'sudo apt-get install --only-upgrade ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def makeUser():
    sudo("useradd -m -s /bin/bash ops445p")
    sudo("usermod -aG sudo ops445p")
    sudo("mkdir -p /home/ops445p/.ssh")
    sudo("chown ops445p:ops445p /home/ops445p/.ssh")
    sudo("chmod 700 /home/ops445p/.ssh")
    put("~/.ssh/id_rsa.pub", "/home/ops445p/.ssh/authorized_keys", use_sudo=True)
    sudo("chown ops445p:ops445p /home/ops445p/.ssh/authorized_keys")
    sudo("chmod 600 /home/ops445p/.ssh/authorized_keys")

def getCurrentUser():
    user = run("whoami")
    print("The current user is:", user)
