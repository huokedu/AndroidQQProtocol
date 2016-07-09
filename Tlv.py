# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:52:04 2016
@author: Alost
"""
from Tools import Coder
from Tools import TEA

class Tlv:
    def __init__(self):
        pass
    def __del__(self):
        pass
    @staticmethod
    def tlv18(uin):
        tlv = ''
        tlv += Coder.trim('00 01')
        tlv += Coder.trim('00 00 06 00')
        tlv += Coder.trim('00 00 00 10')
        tlv += Coder.trim('00 00 00 00')
        tlv += uin
        tlv += Coder.trim('00 00 00 00')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('00 18') + tlv
        return tlv
    @staticmethod
    def tlv1(uin, server_time):
        tlv = ''
        tlv += Coder.trim('00 01')
        tlv += Coder.genBytesHexstr(4)
        tlv += uin
        tlv += server_time
        tlv += Coder.trim('00 00 00 00')
        tlv += Coder.trim('00 00')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('00 01') + tlv
        return tlv
    @staticmethod
    def tlv106(uin, server_time, pwdMd5, tgtKey, imei, appId, pwdKey):
        tlv = ''
        tlv += Coder.trim('00 03')
        tlv += Coder.genBytesHexstr(4)
        tlv += Coder.trim('00 00 00 05 00 00 00 10 00 00 00 00 00 00 00 00')
        tlv += uin
        tlv += server_time
        tlv += Coder.trim('00 00 00 00 01')
        tlv += pwdMd5
        tlv += tgtKey
        tlv += Coder.trim('00 00 00 00 01')
        tlv += imei
        tlv += appId
        tlv += Coder.trim('00 00 00 01')
        tlv += Coder.trim('00 00')
        tlv = TEA.entea_hexstr(tlv, pwdKey)
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 06') + tlv
        return tlv
    @staticmethod
    def tlv116():
        tlv = ''
        tlv += Coder.trim('00')
        tlv += Coder.trim('00 01 FF 7C')
        tlv += Coder.trim('00 01 04 00')
        tlv += Coder.trim('00')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 16') + tlv
        return tlv
    @staticmethod
    def tlv100():
        tlv = ''
        tlv += Coder.trim('00 01')
        tlv += Coder.trim('00 00 00 05')
        tlv += Coder.trim('00 00 00 10')
        tlv += Coder.trim('20 02 9F 54')
        tlv += Coder.trim('00 00 00 00')
        tlv += Coder.trim('02 1E 10 E0')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 00') + tlv
        return tlv
    @staticmethod
    def tlv107():
        tlv = ''
        tlv += Coder.trim('00 00')
        tlv += Coder.trim('00 00 00 01')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 07') + tlv
        return tlv
    @staticmethod
    def tlv144(tgtKey, imei, os_type, os_version, network_type, sim_operator_name, apn, device, device_product):
        tlv = ''
        tlv += Coder.trim('00 04')
        tlv += Tlv.tlv109(imei)
        tlv += Tlv.tlv124(os_type, os_version, network_type, sim_operator_name, apn)
        tlv += Tlv.tlv128(device, imei, device_product)
        tlv += Tlv.tlv16e(device)
        tlv = TEA.entea_hexstr(tlv, tgtKey)
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 44') + tlv
        return tlv
    @staticmethod
    def tlv109(imei):
        tlv = ''
        tlv += Coder.num2hexstr(len(imei)/2, 2) + imei
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 09') + tlv
        return tlv
    @staticmethod
    def tlv124(os_type, os_version, network_type, sim_operator_name, apn):
        tlv = ''
        tlv += Coder.num2hexstr(len(os_type)/2, 2) + os_type
        tlv += Coder.num2hexstr(len(os_version)/2, 2) + os_version
        tlv += Coder.num2hexstr(len(network_type)/2, 2) + network_type
        tlv += Coder.num2hexstr(len(sim_operator_name)/2, 2) + sim_operator_name
        tlv += Coder.trim('00 00')
        tlv += Coder.num2hexstr(len(apn)/2, 2) + apn
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 24') + tlv
        return tlv
    @staticmethod
    def tlv128(device, imei, device_product):
        tlv = ''
        tlv += Coder.trim('00 00')
        tlv += Coder.trim('01')
        tlv += Coder.trim('01')
        tlv += Coder.trim('00')
        tlv += Coder.trim('11 00 00 00')
        tlv += Coder.num2hexstr(len(device)/2, 2) + device
        tlv += Coder.num2hexstr(len(imei)/2, 2) + imei
        tlv += Coder.num2hexstr(len(device_product)/2, 2) + device_product
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 28') + tlv
        return tlv
    @staticmethod
    def tlv16e(device):
        tlv = ''
        tlv += Coder.num2hexstr(len(device)/2, 2) + device
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 6E') + tlv
        return tlv
    @staticmethod
    def tlv142(package_name):
        tlv = ''
        tlv += Coder.num2hexstr(len(package_name)/2, 4) + package_name
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 42') + tlv
        return tlv
    @staticmethod
    def tlv145(imei):
        tlv = ''
        tlv += imei
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 45') + tlv
        return tlv
    @staticmethod
    def tlv154(seq):
        tlv = ''
        tlv += Coder.num2hexstr(seq, 4)
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 54') + tlv
        return tlv
    @staticmethod
    def tlv141(sim_operator_name, network_type, apn):
        tlv = ''
        tlv += Coder.trim('00 01')
        tlv += Coder.num2hexstr(len(sim_operator_name)/2, 2) + sim_operator_name
        tlv += Coder.num2hexstr(len(network_type)/2, 2) + network_type
        tlv += Coder.num2hexstr(len(apn)/2, 2) + apn
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 41') + tlv
        return tlv
    @staticmethod
    def tlv8():
        tlv = ''
        tlv += Coder.trim('00 00')
        tlv += Coder.trim('00 00 08 04') #request_global._local_id
        tlv += Coder.trim('00 00')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('00 08') + tlv
        return tlv
    @staticmethod
    def tlv16b():
        tlv = ''
        tlv += Coder.trim('00 02')
        tlv += Coder.trim('00 0B')
        tlv += Coder.trim('67 61 6D 65 2E 71 71 2E 63 6F 6D') #game.qq.com
        tlv += Coder.trim('00 0B')
        tlv += Coder.trim('67 61 6D 65 2E 71 71 2E 63 6F 6D')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 6B') + tlv
        return tlv
    @staticmethod
    def tlv147():
        tlv = ''
        tlv += Coder.trim('00 00 00 10')
        tlv += Coder.trim('00 05')
        tlv += Coder.trim('35 2E 38 2E 30') #request_global._apk_v = 5.8.0
        tlv += Coder.trim('00 10')
        tlv += Coder.trim('A6 B7 45 BF 24 A2 C2 77 52 77 16 F6 F3 6E B6 8D') #request_global._apk_sig
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 47') + tlv
        return tlv
    @staticmethod
    def tlv177():
        tlv = ''
        tlv += Coder.trim('01')
        tlv += Coder.trim('55 A3 23 2E')
        tlv += Coder.trim('00 07')
        tlv += Coder.trim('35 2E 34 2E 30 2E 37') #5.4.0.7
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 77') + tlv
        return tlv
    @staticmethod
    def tlv187():
        tlv = ''
        tlv += Coder.trim('F9 03 BA FF 80 D5 BA AC DC EA 9C 16 49 6F 53 83')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 87') + tlv
        return tlv
    @staticmethod
    def tlv188():
        tlv = ''
        tlv += Coder.trim('3F D1 F5 BA 24 67 56 F3 97 87 49 AE 1D 67 76 EE')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 88') + tlv
        return tlv
    @staticmethod
    def tlv191():
        tlv = ''
        tlv += Coder.trim('01')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 91') + tlv
        return tlv
    @staticmethod
    def tlv194():
        tlv = ''
        tlv += Coder.trim('65 68 D4 A4 FA CA 6E 78 B3 6B 07 40 C2 71 A8 6E')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 94') + tlv
        return tlv
    @staticmethod
    def tlv202(wifi_name):
        tlv = ''
        tlv += Coder.trim('00 10')
        tlv += Coder.trim('F5 AC 6C 03 0C 31 AE 5C 26 2E BE 49 86 23 65 1E')
        tlv += Coder.num2hexstr(len(wifi_name)/2, 2) + wifi_name
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('02 02') + tlv
        return tlv

    @staticmethod
    def tlv2(verifyCode, verifyToken1):
        tlv = ''
        tlv += Coder.num2hexstr(len(verifyCode)/2, 4) + verifyCode
        tlv += Coder.num2hexstr(len(verifyToken1)/2, 2) + verifyToken1
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('00 02') + tlv
        return tlv
    '''
    @staticmethod
    def tlv8():
        tlv = ''
        tlv += Coder.trim('00 00')
        tlv += Coder.trim('00 00 08 04')
        tlv += Coder.trim('00 00 ')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('00 08') + tlv
        return tlv
    '''
    @staticmethod
    def tlv104(verifyToken2):
        tlv = ''
        tlv += verifyToken2
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 04') + tlv
        return tlv
    '''
    @staticmethod
    def tlv116():
        tlv = ''
        tlv += Coder.trim('00')
        tlv += Coder.trim('00 01 FF 7C')
        tlv += Coder.trim('00 01 04 00')
        tlv += Coder.trim('00')
        tlv = Coder.num2hexstr(len(tlv)/2, 2) + tlv
        tlv = Coder.trim('01 16') + tlv
        return tlv
    '''

if __name__ == '__main__':
    pass

