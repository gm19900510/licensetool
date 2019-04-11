# -*- coding: utf-8 -*-

import subprocess

def getCpuId():
    p = subprocess.Popen(["sudo dmidecode -t 4 | grep ID"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    data = p.stdout
    lines = []
    while True:
        line = str(data.readline(), encoding="utf-8")
        if line == '\n':
            break
        if line:
            d = dict([line.strip().split(': ')])
            lines.append(d)
        else:
            break    
    return lines


def getBaseboardSerialnumber ():
    p = subprocess.Popen(["sudo dmidecode -t 2 | grep Serial"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    data = p.stdout
    lines = []
    while True:
        line = str(data.readline(), encoding="utf-8")
        if line == '\n':
            break
        if line:
            d = dict([line.strip().split(': ')])
            lines.append(d)
        else:
            break    
    return lines
