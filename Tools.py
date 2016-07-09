# -*- coding: utf-8 -*-

import random
import md5
import socket
import struct
import unittest
import cStringIO
from PIL import Image

class MD5():
    @staticmethod
    def md5_hex(data):
        hash = md5.md5()
        hash.update(data)
        hash.digest()
        return hash.hexdigest()

class TestCaseMD5(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_md5_hex(self):
        self.assertEqual(MD5.md5_hex('12345678'), '25d55ad283aa400af464c76d713c07ad')

class TEA():
    '''百度百科：http://baike.baidu.com/view/6064828.htm
        http://blog.chinaunix.net/uid-324919-id-135731.html
        http://abcn.cneu.eu/crypto/tea/tea.c
    '''
    @staticmethod
    def xor(a, b):
        op = 0xffffffffL
        a1,a2 = struct.unpack('>LL', a[0:8])
        b1,b2 = struct.unpack('>LL', b[0:8])
        return struct.pack('>LL', ( a1 ^ b1) & op, ( a2 ^ b2) & op)
    @staticmethod
    def code(v, k):
        n=16
        op = 0xffffffffL
        delta = 0x9e3779b9L
        k = struct.unpack('>LLLL', k[0:16])
        y, z = struct.unpack('>LL', v[0:8])
        s = 0
        for i in xrange(n):
            s += delta
            y += (op &(z<<4))+ k[0] ^ z+ s ^ (op&(z>>5)) + k[1]
            y &= op
            z += (op &(y<<4))+ k[2] ^ y+ s ^ (op&(y>>5)) + k[3]
            z &= op
        r = struct.pack('>LL',y,z)
        return r
    @staticmethod
    def encrypt(v, key):
        END_CHAR = '\0'
        FILL_N_OR = 0xF8
        vl = len(v)
        filln = (8-(vl+2))%8 + 2
        fills = ''
        for i in xrange(filln):
            fills = fills + chr(random.randint(0, 255))
        v = ( chr((filln -2)|FILL_N_OR)
              + fills
              + v
              + END_CHAR * 7)
        tr = '\0'*8
        to = '\0'*8
        r = ''
        o = '\0' * 8
        for i in xrange(0, len(v), 8):
            o = TEA.xor(v[i:i+8], tr)
            tr = TEA.xor(TEA.code(o, key), to)
            to = o
            r += tr
        return r
    @staticmethod
    def decipher(v, k):
        n = 16
        op = 0xffffffffL
        y, z = struct.unpack('>LL', v[0:8])
        a, b, c, d = struct.unpack('>LLLL', k[0:16])
        delta = 0x9E3779B9L
        s = (delta << 4)&op
        for i in xrange(n):
            z -= ((y<<4)+c) ^ (y+s) ^ ((y>>5) + d)
            z &= op
            y -= ((z<<4)+a) ^ (z+s) ^ ((z>>5) + b)
            y &= op
            s -= delta
            s &= op
        return struct.pack('>LL', y, z)
    @staticmethod
    def decrypt(v, key):
        l = len(v)
        prePlain = TEA.decipher(v, key)
        pos = (ord(prePlain[0]) & 0x07L) +2
        r = prePlain
        preCrypt = v[0:8]
        for i in xrange(8, l, 8):
            x = TEA.xor(TEA.decipher(TEA.xor(v[i:i+8], prePlain),key ), preCrypt)
            prePlain = TEA.xor(x, preCrypt)
            preCrypt = v[i:i+8]
            r += x
        if r[-7:] != '\0'*7:
            return None
        return r[pos+1:-7]

    @staticmethod
    def entea_hexstr(data, key):
        return TEA.encrypt(data.decode('hex'), key.decode('hex')).encode('hex')

    @staticmethod
    def detea_hexstr(data, key):
        return TEA.decrypt(data.decode('hex'), key.decode('hex')).encode('hex')

class TestCaseTEA(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_tea(self):
        hexstr = '12345678'
        key = '00000000000000000000000000000000'
        self.assertEqual(TEA.detea_hexstr(TEA.entea_hexstr(hexstr, key), key), hexstr)

class Coder():
    @staticmethod
    def trim(data):
        return data.replace(' ', '').lower()
    @staticmethod
    def num2hexstr(data, n=1):
        data = hex(data).replace('0x', '').replace('L', '')
        return '0'*(2*n-len(data)) + data
    @staticmethod
    def numlist2hexstr(data, n=1):
        return ''.join([Coder.num2hexstr(li, n) for li in data])
    @staticmethod
    def str2hexstr(data):
        return data.encode('hex')
    @staticmethod
    def hexstr2str(data):
        return data.decode('hex')
    @staticmethod
    def hexstr2num(data):
        return long(data, 16)
    @staticmethod
    def hexstr2hexlist(data):
        return [data[i]+data[i+1] for i in range(0, len(data), 2)]
    @staticmethod
    def hexstr2hexstream(data):
        return bytearray.fromhex(data)
    @staticmethod
    def genBytesHexstr(n):
        return Coder.numlist2hexstr([random.randint(0, 255) for i in range(n)])
    @staticmethod
    def qqnum2hexstr(qqnum):
        data = hex(long(qqnum)).replace('0x', '').replace('L', '')
        return '0'*(8-len(data)) + data
    @staticmethod
    def hash_qqpwd_hexstr(qqnum, qqpwd):
        return MD5.md5_hex(MD5.md5_hex(qqpwd).decode('hex') + '00000000'.decode('hex') + Coder.qqnum2hexstr(qqnum).decode('hex'))
    @staticmethod
    def ip2long(ip):
        packedIP = socket.inet_aton(ip)
        return struct.unpack("!L", packedIP)[0]
    @staticmethod
    def long2ip(num):
        return socket.inet_ntoa(struct.pack('!L', num))
    @staticmethod
    def ip2hexstr(ip):
        return Coder.num2hexstr(Coder.ip2long(ip))
    @staticmethod
    def hexstr2ip(data):
        return Coder.long2ip(Coder.hexstr2num(data))

class TestCaseCoder(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_trim(self):
        self.assertEqual(Coder.trim('   t e  s t '), 'test')
    def test_num2hexstr(self):
        self.assertEqual(Coder.num2hexstr(4), '04')
        self.assertEqual(Coder.num2hexstr(4, 2), '0004')
        self.assertEqual(Coder.num2hexstr(255, 2), '00ff')
    def test_numlist2hexstr(self):
        self.assertEqual(Coder.numlist2hexstr([1, 2, 3, 4, 5, 255], 1), '0102030405ff')
    def test_str2hexstr(self):
        self.assertEqual(Coder.str2hexstr('502549600'), '353032353439363030')
    def test_hexstr2str(self):
        self.assertEqual(Coder.hexstr2str('353032353439363030'), '502549600')
    def test_hexstr2num(self):
        self.assertEqual(Coder.hexstr2num('00'), 0)
        self.assertEqual(Coder.hexstr2num('04'), 4)
        self.assertEqual(Coder.hexstr2num('00ff'), 255)
        self.assertEqual(Coder.hexstr2num('ffff'), 65535)
    def test_hexstr2hexlist(self):
        self.assertEqual(Coder.hexstr2hexlist('353032353439363030'), ['35','30','32','35','34','39','36','30','30'])
    def test_hexstr2hexstream(self):
        self.assertEqual(Coder.hexstr2hexstream('353032353439363030'), '\x35\x30\x32\x35\x34\x39\x36\x30\x30')

    def test_qq2hexstr(self):
        self.assertEqual(Coder.qqnum2hexstr('502549600'), '1df44c60')
        self.assertEqual(Coder.qqnum2hexstr('5201314'), '004f5da2')
        self.assertEqual(Coder.qqnum2hexstr('2147483648'), '80000000')
    def test_hash_qqpwd_hexstr(self):
        self.assertEqual(Coder.hash_qqpwd_hexstr('502549600', '12345678'), '2c73cc3539d282b14172505f1e6e2a50')
    def test_ip2long(self):
        self.assertEqual(Coder.ip2long('45.112.249.58'), Coder.hexstr2num('2D70F93A'))
    def test_long2ip(self):
        self.assertEqual(Coder.long2ip(Coder.hexstr2num('2D70F93A')), '45.112.249.58')
    def test_ip2hexstr(self):
        self.assertEqual(Coder.ip2hexstr('45.112.249.58'), '2d70f93a')
    def test_hexstr2ip(self):
        self.assertEqual(Coder.hexstr2ip('2d70f93a'), '45.112.249.58')

class HexPacket:
    def __init__(self, data):
        self.cur = 0
        self.data = data
        self.len = len(data)
    def shl(self, n):
        n *= 2
        if (n > self.cur):
            n = self.cur
        old = self.cur
        self.cur -= n
        return self.data[self.cur:old]
    def shr(self, n):
        n *= 2
        if (n+self.cur > self.len):
            n = self.len - self.cur
        old = self.cur
        self.cur += n
        return self.data[old:self.cur]
    def remain_n(self):
        return (self.len - self.cur) / 2
    def remain(self, rn=0):
        return self.shr(self.remain_n()-rn)
    def len(self):
        return self.len
    def cur_byte(self):
        return self.data[self.cur:self.cur+2]

class TestCaseHexPacket(unittest.TestCase):
    def setUp(self):
        self.pack = HexPacket('12345678')
    def tearDown(self):
        pass
    def test_all(self):
        self.assertEqual(self.pack.shl(10), '')
        self.assertEqual(self.pack.shr(1), '12')
        self.assertEqual(self.pack.cur_byte(), '34')
        self.assertEqual(self.pack.shr(1), '34')
        self.assertEqual(self.pack.shl(1), '34')
        self.assertEqual(self.pack.shr(3), '345678')
        self.assertEqual(self.pack.remain_n(), 0)
        self.assertEqual(self.pack.shl(5), '12345678')
        self.assertEqual(self.pack.shr(3), '123456')
        self.assertEqual(self.pack.cur_byte(), '78')
        self.assertEqual(self.pack.remain(), '78')
        self.assertEqual(self.pack.remain(1), '')

class Img:
    def __init__(self):
        pass
    def __del__(self):
        pass
    @staticmethod
    def showFromHexstr(data):
        f = cStringIO.StringIO(data.decode('hex'))
        img = Image.open(f)
        img.show()
    @staticmethod
    def saveFromHexstr(data, filename):
        with open(filename, 'wb') as f:
            f.write(data.decode('hex'))

if __name__ == '__main__':
    unittest.main()
    print Coder.hash_qqpwd_hexstr('123456', '12345678')
    print MD5.md5_hex('12345678')

