# -*- coding: utf-8 -*-

import time
import threading
import random

from Tools import Coder
from Tools import MD5
from Tools import TEA
from Tools import HexPacket
from Tools import Img
import Keys
from Tlv import Tlv
from RawSocket import RawSocket



class AndroidQQ:
    '''android qq'''
    def __init__(self, qqnum, qqpwd):
        self.socket = RawSocket('113.108.90.53', 8080)
        if not self.socket.connect():
            raise Exception('socket connect error!')
        #QQ
        self.qqnum = qqnum
        self.qqpwd = qqpwd
        self.vcode = ''
        self.qqHexstr = Coder.str2hexstr(qqnum)
        self.pwdMd5 = MD5.md5_hex(qqpwd)
        self.uin = Coder.qqnum2hexstr(qqnum)
        self.HEART_INTERVAL = 8*60 #心跳时间间隔 如果在手机QQ上注销/退出帐号后，一般10分钟左右您的QQ号就不会显示在线了
        self.server_time = Coder.num2hexstr(int(time.time()), 4)
        self.alive = False
        self.verify = False

        #Android
        self.seq = 1000
        self.appId = Coder.num2hexstr(537042772, 4)
        self.extBin = Coder.trim('')
        self.msgCookies = Coder.trim('F9 83 8D 80')
        self.imei = Coder.str2hexstr('864116195797922')
        self.ksid = Coder.trim('')
        self.extBin = Coder.trim('')
        self.ver = Coder.str2hexstr('|460006202217491|A5.8.0.157158')
        self.os_type = Coder.str2hexstr('android')
        self.os_version = Coder.str2hexstr('4.2.2')
        self.network_type = Coder.str2hexstr('')
        self.sim_operator_name = Coder.str2hexstr('CMCC')
        self.apn = Coder.str2hexstr('wifi')
        self.device = Coder.str2hexstr('Lenovo A820t')
        self.device_product = Coder.str2hexstr('Lenovo')
        self.package_name = Coder.str2hexstr('com.tencent.mobileqq')
        self.wifi_name = Coder.str2hexstr('OOOOOOOOO')

        #cmd
        self.loginCmd = Coder.str2hexstr('wtlogin.login')

        #Keys
        self.defaultKey = '00'*16
        self.randomKey = Coder.genBytesHexstr(16)
        self.keyId = random.randint(0, len(Keys.pubKeys)-1)
        self.pubKey = Keys.pubKeys[self.keyId]
        self.shareKey = Keys.shareKeys[self.keyId]
        self.pwdKey = Coder.hash_qqpwd_hexstr(qqnum, qqpwd)
        self.tgtKey = Coder.genBytesHexstr(16)
        self.sessionKey = ''

        #debug
        print 'uin: ', self.uin
        print 'pwdMd5: ', self.pwdMd5
        print 'randomKey: ', self.randomKey
        print 'pubKey: ', self.pubKey
        print 'shareKey: ', self.shareKey
        print 'pwdKey: ', self.pwdKey
        print 'tgtKey: ', self.tgtKey

    def __del__(self):
        pass

    def sendHeart(self):
        '''发心跳包'''
        pass
    def startHeart(self):
        '''开始心跳'''
        while True:
            time.sleep(self.HEART_INTERVAL)
            self.sendHeart()

    def login(self, verifyCode=None):
        '''登录'''
        #发送登录请求
        packet = ''
        #包头
        packet += Coder.trim('00 00 00 08 02 00 00 00 04 00')
        packet += Coder.num2hexstr(len(self.qqHexstr)/2+4, 4)
        packet += self.qqHexstr
        #TEA加密的包体
        packet += self.packSendLoginMessage(verifyCode)
        #总包长
        packet = Coder.num2hexstr(len(packet)/2+4, 4) + packet
        #发送请求
        self.socket.sendall(Coder.hexstr2str(packet))
        #接收请求
        ret = self.socket.recv()
        pack = HexPacket(Coder.str2hexstr(ret))
        #返回包头
        pack.shr(4)
        pack.shr(8)
        pack.shr(2 + len(self.qqHexstr)/2)
        #返回包体
        self.unpackRecvLoginMessage(pack.remain())

        if self.alive: #登录成功
            threading.Thread(target=self.startHeart).start() #心跳
            return True
        elif self.verify: #需要验证码
            pass
        else:
            return False
    def unpackRecvLoginMessage(self, data):
        data = TEA.detea_hexstr(data, self.defaultKey)
        pack = HexPacket(data)
        head = pack.shr(Coder.hexstr2num(pack.shr(4))-4)
        body = pack.remain(1)
        #head
        pack = HexPacket(head)
        Coder.hexstr2num(pack.shr(4)) #seq
        pack.shr(4)
        pack.shr(Coder.hexstr2num(pack.shr(4))-4)
        Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(4))-4)) #cmd
        pack.shr(Coder.hexstr2num(pack.shr(4))-4)
        #body
        pack = HexPacket(body)
        pack.shr(4 + 1 + 2 + 10 + 2)
        retCode = Coder.hexstr2num(pack.shr(1))
        if retCode == 0: #登录成功
            self.unpackRecvLoginSucceedMessage(pack.remain())
            print u'登录成功: ', self.nickname
            self.alive = True
            self.verify = False
        elif retCode == 2: #需要验证码
            self.unpackRecvLoginVerifyMessage(pack.remain())
            print self.verifyReason
            self.alive = False
            self.verify = True
            threading.Thread(target=Img.showFromHexstr, args=(self.verifyPicHexstr, )).start()
            code = raw_input(u'请输入验证码：')
            self.login(Coder.str2hexstr(code))
        else: #登录失败
            pack = HexPacket(TEA.detea_hexstr(pack.remain(), self.shareKey))
            pack.shr(2 + 1 + 4 + 2)
            pack.shr(4) #type
            title = Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(2))))
            msg = Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(2))))
            print title, ': ', msg
            self.alive = False
            self.verify = False

    def unpackRecvLoginVerifyMessage(self, data):
        data = TEA.detea_hexstr(data, self.shareKey)
        pack = HexPacket(data)
        pack.shr(3)
        tlv_num = Coder.hexstr2num(pack.shr(2))
        for i in xrange(tlv_num):
            tlv_cmd = pack.shr(2)
            tlv_data = pack.shr(Coder.hexstr2num(pack.shr(2)))
            self.decodeTlv(tlv_cmd, tlv_data)
        pass
    def unpackRecvLoginSucceedMessage(self, data):
        data = TEA.detea_hexstr(data, self.shareKey)
        pack = HexPacket(data)
        pack.shr(2 + 1 + 4)
        data = pack.shr(Coder.hexstr2num(pack.shr(2)))
        #TLV解包
        data = TEA.detea_hexstr(data, self.tgtKey)
        pack = HexPacket(data)
        tlv_num = Coder.hexstr2num(pack.shr(2))
        for i in xrange(tlv_num):
            tlv_cmd = pack.shr(2)
            tlv_data = pack.shr(Coder.hexstr2num(pack.shr(2)))
            self.decodeTlv(tlv_cmd, tlv_data)
    def decodeTlv(self, cmd, data):
        if cmd == Coder.trim('01 6A'):
            pass
        elif cmd == Coder.trim('01 06'):
            pass
        elif cmd == Coder.trim('01 0C'):
            pass
        elif cmd == Coder.trim('01 0A'):
            self.token004c = data
        elif cmd == Coder.trim('01 0D'):
            pass
        elif cmd == Coder.trim('01 14'):
            pack = HexPacket(data)
            pack.shr(6)
            self.token0058 = pack.shr(Coder.hexstr2num(pack.shr(2)))
        elif cmd == Coder.trim('01 0E'):
            self.mst1Key = data
        elif cmd == Coder.trim('01 03'):
            self.stweb = data
        elif cmd == Coder.trim('01 1F'):
            pass
        elif cmd == Coder.trim('01 38'):
            pass
        elif cmd == Coder.trim('01 1A'):
            pack = HexPacket(data)
            pack.shr(2 + 1 + 1)
            self.nickname = Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(1))))
        elif cmd == Coder.trim('01 20'):
            self.skey = data
        elif cmd == Coder.trim('01 36'):
            self.vkey = data
        elif cmd == Coder.trim('01 1A'):
            pass
        elif cmd == Coder.trim('01 20'):
            pass
        elif cmd == Coder.trim('01 36'):
            pass
        elif cmd == Coder.trim('03 05'):
            self.sessionKey = data
        elif cmd == Coder.trim('01 43'):
            self.token002c = data
        elif cmd == Coder.trim('01 64'):
            self.sid = data
        elif cmd == Coder.trim('01 18'):
            pass
        elif cmd == Coder.trim('01 63'):
            pass
        elif cmd == Coder.trim('01 30'):
            pack = HexPacket(data)
            pack.shr(2)
            self.server_time = pack.shr(4)
            self.ip = Coder.hexstr2ip(pack.shr(4))
        elif cmd == Coder.trim('01 05'):
            pack = HexPacket(data)
            self.verifyToken1 = pack.shr(Coder.hexstr2num(pack.shr(2)))
            self.verifyPicHexstr = pack.shr(Coder.hexstr2num(pack.shr(2)))
        elif cmd == Coder.trim('01 04'):
            self.verifyToken2 = data
        elif cmd == Coder.trim('01 65'):
            pack = HexPacket(data)
            pack.shr(4)
            title = Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(1))))
            msg = Coder.hexstr2str(pack.shr(Coder.hexstr2num(pack.shr(4))))
            self.verifyReason = title + ": " + msg
        elif cmd == Coder.trim('01 08'):
            self.ksid = data
        elif cmd == Coder.trim('01 6D'):
            self.superKey = data
        elif cmd == Coder.trim('01 6C'):
            self.psKey = data
        else:
            print 'unknown tlv: '
            print cmd, ': ', data
    def packSendLoginMessage(self, verifyCode=None):
        #MessageHead
        msgHeader = ''
        msgHeader += Coder.num2hexstr(self.seq+1, 4)
        msgHeader += self.appId
        msgHeader += self.appId
        msgHeader += Coder.trim('01 00 00 00 00 00 00 00 00 00 00 00')
        msgHeader += Coder.num2hexstr(len(self.extBin)/2+4, 4) + self.extBin
        msgHeader += Coder.num2hexstr(len(self.loginCmd)/2+4, 4) + self.loginCmd
        msgHeader += Coder.num2hexstr(len(self.msgCookies)/2+4, 4) + self.msgCookies
        msgHeader += Coder.num2hexstr(len(self.imei)/2+4, 4) + self.imei
        msgHeader += Coder.num2hexstr(len(self.ksid)/2+4, 4) + self.ksid
        msgHeader += Coder.num2hexstr(len(self.ver)/2+2, 2) + self.ver
        msgHeader = Coder.num2hexstr(len(msgHeader)/2+4, 4) + msgHeader
        #Message
        msg = ''
        msg += Coder.trim('1F 41')
        msg += Coder.trim('08 10 00 01')
        msg += self.uin
        msg += Coder.trim('03 07 00 00 00 00 02 00 00 00 00 00 00 00 00 01 01')
        msg += self.randomKey
        msg += Coder.trim('01 02')
        msg += Coder.num2hexstr(len(self.pubKey)/2, 2) + self.pubKey
        #TEA加密的TLV
        msg += self.packSendLoginTlv(verifyCode)

        msg += Coder.trim('03')
        msg = Coder.num2hexstr(len(msg)/2+2+1, 2) + msg
        msg = Coder.trim('02') + msg
        msg = Coder.num2hexstr(len(msg)/2+4, 4) + msg

        packet = msgHeader + msg
        packet = TEA.entea_hexstr(packet, self.defaultKey)
        return packet
    def packSendLoginTlv(self, verifyCode=None):
        if verifyCode == None:
            tlv = ''
            tlv += Coder.trim('00 09')
            tlv += Coder.trim('00 14') #tlv包个数
            #tlv组包
            tlv += Tlv.tlv18(self.uin)
            tlv += Tlv.tlv1(self.uin, self.server_time)
            tlv += Tlv.tlv106(self.uin, self.server_time, self.pwdMd5, self.tgtKey, self.imei, self.appId, self.pwdKey)
            tlv += Tlv.tlv116()
            tlv += Tlv.tlv100()
            tlv += Tlv.tlv107()
            tlv += Tlv.tlv144(self.tgtKey, self.imei, self.os_type, self.os_version, self.network_type, self.sim_operator_name, self.apn, self.device, self.device_product)
            tlv += Tlv.tlv142(self.package_name)
            tlv += Tlv.tlv145(self.imei)
            tlv += Tlv.tlv154(self.seq)
            tlv += Tlv.tlv141(self.sim_operator_name, self.network_type, self.apn)
            tlv += Tlv.tlv8()
            tlv += Tlv.tlv16b()
            tlv += Tlv.tlv147()
            tlv += Tlv.tlv177()
            tlv += Tlv.tlv187()
            tlv += Tlv.tlv188()
            tlv += Tlv.tlv191()
            tlv += Tlv.tlv194()
            tlv += Tlv.tlv202(self.wifi_name)
            tlv = TEA.entea_hexstr(tlv, self.shareKey)
            return tlv
        else:
            tlv = ''
            tlv += Coder.trim('00 02')
            tlv += Coder.trim('00 04')
            #tlv组包
            tlv += Tlv.tlv2(verifyCode, self.verifyToken1)
            tlv += Tlv.tlv8()
            tlv += Tlv.tlv104(self.verifyToken2)
            tlv += Tlv.tlv116()
            tlv = TEA.entea_hexstr(tlv, self.shareKey)
            return tlv
    def logout(self):
        '''注销'''
        pass

    def getVcode(self):
        '''获取验证码'''
        pass

def test():
    qq = AndroidQQ("qq number", "password")
    qq.login()

if __name__ == '__main__':
    test()
