# -*- coding: utf-8 -*-

import socket

class RawSocket:
    '''Python socket: http://blog.csdn.net/rebelqsp/article/details/22109925'''
    def __init__(self, ip, port):
        self.addr = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP

    def __del__(self):
        self.socket.close()

    def connect(self):
        return self.socket.connect_ex(self.addr) == 0

    def sendall(self, data):
        try:
            return self.socket.sendall(data) == None
        except Exception, e:
            print u'数据发送失败: ', e
        return False

    def recv(self):
        return self.socket.recv(10240) #下面的代码暂时无解 待处理
        buf = ''
        while True: #确保把包收全
            tmp = self.socket.recv(1024)
            if not len(tmp):
                break
            buf += tmp
        return buf

    def close(self):
        return self.socket.close()

if __name__ == '__main__':
    sock = RawSocket('113.108.90.53', 8080)
    print sock.connect()
    import Tools
    print sock.sendall(Coder.hexstr2str('353032353439363030'))
    print sock.recv()
    sock.close()
