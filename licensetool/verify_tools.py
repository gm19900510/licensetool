# -*- coding: utf-8 -*-
import datetime
import platform
import json
import base64
import rsa
import os

sysstr = platform.system()
if(sysstr == "Windows"):
    # print ("Call Windows tasks")
    tools = __import__('licensetool.win_tools', fromlist=True)
elif(sysstr == "Linux"):
    # print ("Call Linux tasks")
    tools = __import__('licensetool.linux_tools', fromlist=True)


# 生成设备指纹：读取设备信息，base64加密后写入指定文件
def writeDeviceDingerprint(dingerprintFilePath=os.path.dirname(os.path.realpath(__file__)) + os.sep, dingerprintFileFileName="sys.info"):
    with open(dingerprintFilePath + dingerprintFileFileName, 'w') as f:  # 设置文件对象
        crypto64 = base64.b64encode(bytes(json.dumps(tools.getCpuId()), encoding="utf8"))
        f.write(str(crypto64, encoding="utf8") + "\n")     
        crypto64 = base64.b64encode(bytes(json.dumps(tools.getBaseboardSerialnumber()), encoding="utf8"))
        f.write(str(crypto64, encoding="utf8"))     


# 获取两个日期间的所有日期
def getEveryDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


# license验证：验证设备指纹与有效期   
def licenseVerify(licensePath=os.path.dirname(os.path.realpath(__file__)) + os.sep, licenseFileName="sys.license", privkeyFile=os.path.dirname(os.path.realpath(__file__)) + os.sep + "private.pem"):  
    valid = False
    try:
        with open(privkeyFile, "rb") as privatefile:
            p = privatefile.read()
            privkey = rsa.PrivateKey.load_pkcs1(p)
            # print(privkey)
        # print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))      
        with open(licensePath + licenseFileName, 'r') as f1:
            lines = f1.readlines()
            
            lines[0] = lines[0].rstrip('\n')
            crypto = base64.b64decode(lines[0])
            message = rsa.decrypt(crypto, privkey)
            cpuId = str(message, encoding="utf8")
            # print(cpuId)  
    
            lines[1] = lines[1].rstrip('\n')
            crypto = base64.b64decode(lines[1])
            message = rsa.decrypt(crypto, privkey)
            baseboardSerialnumber = str(message, encoding="utf8")
            # print(baseboardSerialnumber) 
            
            lines[2] = lines[2].rstrip('\n')
            crypto = base64.b64decode(lines[2])
            message = rsa.decrypt(crypto, privkey)
            validTime = str(message, encoding="utf8")
            # print(validTime) 
        
            j_cpuId = json.loads(cpuId)
            j_baseboardSerialnumber = json.loads(baseboardSerialnumber)
            
            if j_cpuId >= tools.getCpuId() and j_baseboardSerialnumber >= tools.getBaseboardSerialnumber():
                # print("硬件信息符合")
                date_list = getEveryDay(datetime.datetime.now().strftime("%Y-%m-%d"), validTime)
                if len(date_list) > 0:
                    # print("未到有效期，剩余有效期：" , len(date_list), "天")
                    # print(len(date_list))
                    valid = True
                else:
                    # print("未到有效期")
                    # raise RuntimeError('RuntimeError')
                    valid = False    
            else:
                # print("硬件信息不符合")
                # raise RuntimeError('RuntimeError')   
                valid = False
    except: 
        valid = False                     
    return valid    


if __name__ == '__main__':
    writeDeviceDingerprint()
