# -*- coding: utf-8 -*-
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

   
# 设备指纹加密生成  License文件
def fingerprintEncryptWriteLicense(validTime,
                                   fingerprintFilePath=os.path.dirname(os.path.realpath(__file__)) + os.sep,
                                   fingerprintFileName="sys.info",
                                   publicKeyFile=os.path.dirname(os.path.realpath(__file__)) + os.sep +"public.pem",
                                   licenseFilePath=os.path.dirname(os.path.realpath(__file__)) + os.sep,
                                   licenseFileName="sys.license"):   
    
    with open(publicKeyFile, "rb") as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
        # print(pubkey)
    
    writeDeviceDingerprint(fingerprintFilePath + fingerprintFileName)
         
    with open(fingerprintFilePath + fingerprintFileName, 'r') as f1:
        lines = f1.readlines()
        
        lines[0] = lines[0].rstrip('\n')
        crypto = base64.b64decode(lines[0])
        cpuId = str(crypto, encoding="utf8")
        # print(cpuId)  

        lines[1] = lines[1].rstrip('\n')
        crypto = base64.b64decode(lines[1])
        baseboardSerialnumber = str(crypto, encoding="utf8")
        # print(baseboardSerialnumber) 
    with open(licenseFilePath + licenseFileName, 'w') as f:
        crypto = rsa.encrypt(cpuId.encode('utf-8'), pubkey)
        crypto64 = base64.b64encode(crypto)
        f.write(str(crypto64, encoding="utf8") + "\n")       
        crypto = rsa.encrypt(baseboardSerialnumber.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n") 
        crypto = rsa.encrypt(validTime.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n")

             
def writeLicense(validTime,
                           fingerprintFilePath=os.path.dirname(os.path.realpath(__file__)) + "\\",
                           fingerprintFileName="sys.info",
                           publicKeyFile=os.path.dirname(os.path.realpath(__file__)) + "\public.pem",
                           licenseFilePath=os.path.dirname(os.path.realpath(__file__)) + "\\",
                           licenseFileName="sys.license"):   
        
    with open(publicKeyFile, "rb") as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
        # print(pubkey)
         
    with open(fingerprintFilePath + fingerprintFileName, 'r') as f1:
        lines = f1.readlines()
        
        lines[0] = lines[0].rstrip('\n')
        crypto = base64.b64decode(lines[0])
        cpuId = str(crypto, encoding="utf8")
        # print(cpuId)  

        lines[1] = lines[1].rstrip('\n')
        crypto = base64.b64decode(lines[1])
        baseboardSerialnumber = str(crypto, encoding="utf8")
        # print(baseboardSerialnumber) 
    with open(licenseFilePath + licenseFileName, 'w') as f:
        crypto = rsa.encrypt(cpuId.encode('utf-8'), pubkey)
        crypto64 = base64.b64encode(crypto)
        f.write(str(crypto64, encoding="utf8") + "\n")       
        crypto = rsa.encrypt(baseboardSerialnumber.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n") 
        crypto = rsa.encrypt(validTime.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n")
