# -*- coding: utf-8 -*-
import base64
import rsa

with open('public.pem', "rb") as publickfile:
    p = publickfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p)
    # print(pubkey)

    
# 读取系统信息文件，写入截至时间，生成加密之后的license   
def sysInfoEncrypt(sysInfoFile, validTime):        
    with open(sysInfoFile, 'r') as f1:
        lines = f1.readlines()
        
        lines[0] = lines[0].rstrip('\n')
        crypto = base64.b64decode(lines[0])
        cpuId = str(crypto, encoding="utf8")
        # print(cpuId)  

        lines[1] = lines[1].rstrip('\n')
        crypto = base64.b64decode(lines[1])
        baseboardSerialnumber = str(crypto, encoding="utf8")
        # print(baseboardSerialnumber) 
    with open('sys.license', 'w') as f:
        crypto = rsa.encrypt(cpuId.encode('utf-8'), pubkey)
        crypto64 = base64.b64encode(crypto)
        f.write(str(crypto64, encoding="utf8") + "\n")       
        crypto = rsa.encrypt(baseboardSerialnumber.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n") 
        crypto = rsa.encrypt(validTime.encode('utf-8'), pubkey)  
        crypto64 = base64.b64encode(crypto)       
        f.write(str(crypto64, encoding="utf8") + "\n")
             
