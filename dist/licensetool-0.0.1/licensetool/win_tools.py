# -*- coding: utf-8 -*-
import wmi

c = wmi.WMI()


# 处理器
def getCpuId():
    cpus = []
    for cpu in c.Win32_Processor():
        tmpdict = {}     
        tmpdict["ID"] = cpu.ProcessorId.strip()
        cpus.append(tmpdict)
    # print(cpus)    
    return cpus


# 主板
def getBaseboardSerialnumber():
    boards = []
    for board_id in c.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg['Serial Number'] = board_id.SerialNumber  # 主板序列号
        boards.append(tmpmsg)
    # print(boards)
    return boards
