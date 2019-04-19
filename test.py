#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import wmi
import json
import base64
import rsa 
import os
verify_tools = __import__('licensetool.verify_tools', fromlist=True)
encrypt_tools = __import__('licensetool.encrypt_tools', fromlist=True)

# 先生成一对密钥，然后保存.pem格式文件
'''
(pubkey, privkey) = rsa.newkeys(1024)

pub = pubkey.save_pkcs1()
pubfile = open('public.pem', 'wb')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private.pem', 'wb')
prifile.write(pri)
prifile.close()
'''

def main():
    verify_tools.writeDeviceDingerprint()  # 获取设备指纹信息
    encrypt_tools.fingerprintEncryptWriteLicense( validTime='2019-04-15',publicKeyFile='public.pem')  # 根据设备指纹信息和有效期生成license
    valid = verify_tools.licenseVerify()  # license验证
    #verify_tools.writeDeviceDingerprint(dingerprintFilePath='',dingerprintFileFileName="sys.info")  # 获取设备指纹信息
    #encrypt_tools.fingerprintEncryptWriteLicense(fingerprintFilePath='',fingerprintFileName='sys.info', validTime='2019-04-15',publicKeyFile='public.pem',licenseFilePath='',licenseFileName="sys.license")  # 根据设备指纹信息和有效期生成license
    #valid = verify_tools.licenseVerify(licensePath='',licenseFileName='sys.license')  # license验证
    print('验证结果：', valid)

      
if __name__ == '__main__':
    main()
