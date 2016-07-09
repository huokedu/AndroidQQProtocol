# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:37:26 2016
@author: Alost
"""

import struct


if __name__ == '__main__':

    stream = '''ff d8 ff e0 00 10 4a
        46 49 46 00 01 01 00 00 01 00 01 00 00 ff fe 00
        22 35 62 31 36 30 65 31 31 00 bf 9f 60 ff 7f 00
        00 0c bf 9f 60 ff 7f 00 00 ff 05 42 00 00 00 00
        00 ff db 00 43 00 10 0b 0c 0e 0c 0a 10 0e 0d 0e
        12 11 10 13 18 28 1a 18 16 16 18 31 23 25 1d 28
        3a 33 3d 3c 39 33 38 37 40 48 5c 4e 40 44 57 45
        37 38 50 6d 51 57 5f 62 67 68 67 3e 4d 71 79 70
        64 78 5c 65 67 63 ff db 00 43 01 11 12 12 18 15
        18 2f 1a 1a 2f 63 42 38 42 63 63 63 63 63 63 63
        63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63
        63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63
        63 63 63 63 63 63 63 63 63 63 63 ff c0 00 11 08
        00 35 00 82 03 01 22 00 02 11 01 03 11 01 ff c4
        00 1f 00 00 01 05 01 01 01 01 01 01 00 00 00 00
        00 00 00 00 01 02 03 04 05 06 07 08 09 0a 0b ff
        c4 00 b5 10 00 02 01 03 03 02 04 03 05 05 04 04
        00 00 01 7d 01 02 03 00 04 11 05 12 21 31 41 06
        13 51 61 07 22 71 14 32 81 91 a1 08 23 42 b1 c1
        15 52 d1 f0 24 33 62 72 82 09 0a 16 17 18 19 1a
        25 26 27 28 29 2a 34 35 36 37 38 39 3a 43 44 45
        46 47 48 49 4a 53 54 55 56 57 58 59 5a 63 64 65
        66 67 68 69 6a 73 74 75 76 77 78 79 7a 83 84 85
        86 87 88 89 8a 92 93 94 95 96 97 98 99 9a a2 a3
        a4 a5 a6 a7 a8 a9 aa b2 b3 b4 b5 b6 b7 b8 b9 ba
        c2 c3 c4 c5 c6 c7 c8 c9 ca d2 d3 d4 d5 d6 d7 d8
        d9 da e1 e2 e3 e4 e5 e6 e7 e8 e9 ea f1 f2 f3 f4
        f5 f6 f7 f8 f9 fa ff c4 00 1f 01 00 03 01 01 01
        01 01 01 01 01 01 00 00 00 00 00 00 01 02 03 04
        05 06 07 08 09 0a 0b ff c4 00 b5 11 00 02 01 02
        04 04 03 04 07 05 04 04 00 01 02 77 00 01 02 03
        11 04 05 21 31 06 12 41 51 07 61 71 13 22 32 81
        08 14 42 91 a1 b1 c1 09 23 33 52 f0 15 62 72 d1
        0a 16 24 34 e1 25 f1 17 18 19 1a 26 27 28 29 2a
        35 36 37 38 39 3a 43 44 45 46 47 48 49 4a 53 54
        55 56 57 58 59 5a 63 64 65 66 67 68 69 6a 73 74
        75 76 77 78 79 7a 82 83 84 85 86 87 88 89 8a 92
        93 94 95 96 97 98 99 9a a2 a3 a4 a5 a6 a7 a8 a9
        aa b2 b3 b4 b5 b6 b7 b8 b9 ba c2 c3 c4 c5 c6 c7
        c8 c9 ca d2 d3 d4 d5 d6 d7 d8 d9 da e2 e3 e4 e5
        e6 e7 e8 e9 ea f2 f3 f4 f5 f6 f7 f8 f9 fa ff da
        00 0c 03 01 00 02 11 03 11 00 3f 00 ee e8 a2 b9
        89 f5 3d 4e ef 5d bc 86 c2 e6 dd 2d b4 f2 99 46
        00 19 d9 bf 80 b1 e9 c8 23 23 d7 bd 00 74 f4 57
        3a 3c 54 b6 97 3f 67 d6 ac df 4f 72 09 46 dd e6
        2b 0f a8 1f d2 a7 b0 f1 56 9b 7d 72 b0 c6 65 8f
        cc 6d b1 3c 88 55 65 3f ec 9f c3 bd 00 6d d1 51
        cf 32 5b c1 24 d2 1c 24 6a 59 8f b0 ac 78 3c 53
        61 2c 88 b2 47 71 02 c8 32 b2 4a 80 29 fc 73 57
        1a 73 9a bc 51 2e 49 6e 6e 51 54 17 5a d3 1b a5
        f4 1f f7 d8 a5 be d4 e1 b4 b5 13 2f ef 8b 30 55
        54 23 92 68 f6 73 bd ac 1c c8 bb 4c 9e 78 ad a1
        69 66 70 88 bd 49 fe 5e e7 da b0 f5 08 99 e0 6b
        fd 6e 21 e5 42 3f 77 04 2c 78 27 82 49 ef db e9
        55 c3 44 ba 3d af db 6f e4 f2 a7 22 54 89 93 73
        b6 08 3b 41 fc 87 e3 5a c6 8a 76 77 fe bc 89 73
        37 6d b5 2b 5b ab 87 b7 8a 46 f3 91 77 32 3c 6c
        84 0f 5e 40 ab 55 85 1c 96 5a 96 a6 26 36 b7 81
        fc bd ac d2 83 1a 2a 8e 73 f9 ff 00 3a 77 87 df
        79 bf bb 05 85 a3 49 88 83 31 38 55 ce 4f 3f e7
        8a 53 a4 92 6d 02 91 b9 45 72 76 f3 5d 4b 68 35
        29 f5 a7 b6 f3 64 68 e3 05 41 42 01 e3 8e 83 a1
        e6 a5 b8 bb d6 e3 d4 2d 2c 3e d7 6e 5a 61 b8 49
        1a 64 e3 d4 83 f9 fe 15 5f 56 77 b5 d7 e3 d3 e4
        1e d3 c8 e9 e8 ac 38 af b5 1b 61 89 96 2d 45 41
        c3 35 a9 1b 93 ea 3a 73 f8 74 ab d6 1a a5 b5 fb
        34 71 16 59 94 65 a2 75 c3 0f c2 b2 95 29 47 5d
        d1 4a 49 97 a8 a2 8a cc a0 ae 26 27 37 2f e2 2b
        d7 85 ee 0b c8 2d 98 46 54 34 71 01 f3 10 dd 32
        07 6e 79 03 35 d0 f8 9a fa 6d 37 41 ba bb b7 c0
        95 02 80 48 c8 19 60 09 fc 8d 71 2f 74 f0 5d e9
        da 3e 8b 7a 44 9e 60 96 6b 82 76 f9 b2 37 38 3e
        bc 71 83 d7 38 a0 0e 8c 43 6b 1c 8f 37 98 ee 6c
        ed a3 48 99 90 4d 23 a1 04 96 23 ab 2f cc bd 3b
        a9 c1 19 39 a1 35 a5 bd dd 8d 95 a5 bd d0 b8 92
        cc b4 af 1a 83 0c d8 3c 8d 88 78 dc 3a 8c f3 c0
        e7 93 45 a3 2d f7 8c ee f5 08 4a cc f6 f9 85 21
        47 da f8 00 02 fc f1 81 9c 63 fc 2a d6 a5 a8 4d
        e1 f4 68 43 5d 6a 33 19 93 cb 6b 98 c6 d4 52 79
        1e 60 1d 7b 7b 64 71 c5 00 63 d9 dc 6a 1a 96 ac
        da 74 97 97 11 21 dd 08 13 a8 32 04 c6 7e 60 30
        09 e2 b4 b5 5b 37 b9 d1 ac 63 49 51 56 de 19 1c
        e7 a3 2a e0 67 3e a7 23 8f 7e b5 5e ca ca e7 4f
        f1 2c 17 3a a4 d1 45 2d ce e9 a4 23 01 57 39 1b
        73 d3 a7 7f 7a d0 bd bb 87 4a 9e ce 18 57 cf 59
        60 28 a4 8c 8d 85 c1 5e 3b e0 67 eb c5 7a 54 dc
        92 82 8f 6b fe 67 34 92 d6 e5 97 82 09 6d ad 25
        fb 25 bf 95 24 48 c1 1a d9 9c 8c 8e 85 c1 fd 71
        58 9a ad 95 bc 3a fc 36 56 6f f6 75 7d a5 f0 49
        11 b1 39 cf 27 d3 1e 95 d0 4b fd 9e 2e 44 6c 2c
        53 6b 11 c3 f9 4e ab b7 e5 1d 8e 73 fa 57 3f af
        c1 6a ba 85 b4 51 e6 3b b7 da 67 2d 29 91 54 9e
        9c 9e 4f f8 55 50 6f 9a da ec 13 5a 1b d6 96 b6
        5f d8 d7 71 cf 7a d7 f0 97 32 4a ea 4e 73 81 e8
        7d a9 9a 6b fd a6 78 e4 8a da 09 34 e8 40 58 27
        9c 61 d7 18 ce 32 3d 7f 97 5a 97 4a 68 ac 67 7d
        32 d0 f9 89 6d 09 79 a4 27 39 90 91 81 fc ea 9e
        99 77 0d f8 92 ef 6b c7 39 f9 a4 0b 91 14 20 0c
        6f e4 60 9c 7d 7f 99 ac 6c fd e7 d3 fc fc 8a d3
        42 c6 a0 9a a5 e6 ae 6d 4c be 4e 9c c8 77 3c 63
        39 03 a8 27 1c 1a 6e 89 74 2c f4 ab ff 00 2c 79
        cb 6d 23 15 7c 63 cc 1d 72 4f 42 7a d4 b3 6a d6
        90 e9 70 19 60 7f b3 5c bb 47 82 7e 62 98 39 73
        fe 7b d6 2e a3 72 6c 02 e9 96 d7 c1 f4 f9 c0 2c
        db 72 d1 29 ed 9e fc 55 42 0e 71 e4 6a df f0 37
        f9 89 b4 9d ee 5e d2 13 cf b6 5b 1b bb 45 7b 6b
        a5 7b 84 74 63 f3 90 c0 e0 e3 18 ea 3a d5 68 af
        0c fe 2b b5 32 43 2d b4 16 eb b1 55 81 1b 38 20
        67 ea 48 1e f9 ad 28 6f 34 d2 db ad 75 38 92 44
        b6 f2 22 df f2 aa 9e bb b0 7e 83 f2 aa d6 37 a2
        3d e6 e3 5b 56 95 e4 39 d9 10 62 d8 c0 1d bf 2a
        a4 df bc ed bf af 5f 97 61 76 d4 d3 8a 06 4b fc
        3c 29 1b b3 17 f3 6d 3e 50 47 a4 83 be 7b 75 ef
        d2 ab e9 03 ed 9a fd fe a2 bc 44 a3 c8 5f f6 b1
        8c 9f d0 54 ec a2 fa 44 69 99 ed 2e 58 ff 00 a3
        94 6c 48 17 ae 58 74 20 e0 f0 6a b7 87 03 da df
        de d8 ef 49 d5 08 76 9c 03 b9 98 f6 3c d6 3f 62
        4f ad bf 52 fa a3 a1 a2 8a 2b 8c d8 6c 88 92 c6
        d1 c8 aa e8 c3 0c ac 32 08 ac 9b df 0e 58 dc 5b
        47 1d bc 6b 6a f0 bf 99 13 c4 a0 15 7f 5f 7e 95
        b1 45 00 72 49 a5 6a fa 64 16 e2 4f 2b 56 8a 09
        15 a3 85 57 63 46 c3 3f 38 24 f3 df 83 eb 59 ba
        a2 cb ad c9 15 ad ac 7a 92 dc 35 c0 96 58 2e b2
        63 83 03 83 9c 70 0f 20 60 fa d7 7f 45 00 73 5e
        31 4f 32 d2 c9 24 50 5d a5 0a 58 60 63 d7 04 f4
        fc 78 ac fb 88 26 d4 b5 01 75 a6 cb 0a 5a d8 85
        89 24 91 f0 3e 51 cf ff 00 ac d7 5b 7b 65 6f 7f
        01 86 e6 30 e8 79 c7 a1 f5 ac a7 f0 96 98 f3 99
        36 c8 aa 47 fa b5 6e 33 eb 5d b4 6b c2 30 49 ee
        af e7 b9 84 e0 db ba 27 4b 95 98 4f 3c 37 4b 79
        b2 2f 9a d5 0a b8 dd 8e c7 15 85 a0 59 c3 aa 5d
        6a 02 f2 03 14 87 1f bb 54 08 23 e7 f9 fe 15 ab
        75 e1 b4 42 93 69 32 fd 8e e1 06 32 32 43 0f 7a
        bb a3 69 49 a6 42 f9 90 cb 3c a7 74 92 9f e2 34
        7b 48 42 0f 91 ea fe f1 f2 b6 d5 cc 08 1d 74 7d
        4b 50 b3 b6 86 59 27 99 51 62 56 19 2d d7 2c 48
        ed ce 7f c2 9d 26 97 ae 47 a4 1b 15 28 d1 46 e0
        61 1b e6 95 49 e9 93 d0 0a eb 69 6a 3e b4 ef 7b
        6b a6 fe 43 f6 7e 66 2e 9f 6b 2d dd c0 b9 bd b7
        f2 a3 85 4c 76 f0 b0 1c 02 39 62 3d 7b 56 85 be
        9d 67 6d 1c 91 c5 6f 18 59 3e f8 c6 43 7d 6a d5
        15 84 aa 4a 5e 45 a8 a4 53 6d 2f 4f 6e b6 36 d9
        f5 f2 97 fc 2b 07 ec fa 8e 83 69 71 2c 2b 6f e4
        ab ef 63 b4 92 e0 90 3a 0e 98 cf e9 5d 55 27 5e
        b5 50 ad 28 e8 f5 42 70 4f 63 98 86 f2 39 6e d9
        34 a8 e4 ba bb 98 10 d7 92 f4 8c 11 cf 6e dc 71
        5b 5a 56 9d 1e 9b 6b e5 2b 79 92 31 dd 24 84 60
        b9 f5 35 71 11 23 50 a8 aa aa 3a 05 18 14 ea 2a
        55 e6 56 5b 04 63 6d 58 51 45 15 91 61 45 14 50
        01 45 14 50 01 45 14 50 01 45 14 50 01 45 14 50
        01 45 14 50 01 45 14 50 01 45 14 50 01 45 14 50
        07 ff d9
        '''.replace(' ', '').replace('\n', '')
    stream = stream.decode('hex')
    verifyCodePicName = 'verifyCode.png'
    from PIL import Image
    with open(verifyCodePicName, 'wb') as f:
        f.write(stream)

    import cStringIO
    f = cStringIO.StringIO(stream)
    img = Image.open(f)
#    img.show()

    s = raw_input(u'请输入验证码：')
