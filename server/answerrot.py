#! /usr/bin/env python
#coding=utf8

import urllib, urllib2, sys
import base64, ssl, time, re, os
import json
import access_token
from PIL import Image

def get_ocr(img, ci, ck):
    try:
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token.get_access_token(ci, ck)
        headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        params = {
            'image': img,
            'language_type': 'CHN_ENG',
            'detect_language': 'false',
            'probability': 'false'
        }
        params = urllib.urlencode(params)
        request = urllib2.Request(url=url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        return [True, content]
    except Exception as e:
        return [False, e]

def get_img(path):
    f = file(path, 'rb')
    d = f.read()
    f.close()
    return base64.b64encode(d)

#unused
def crop_img0(path, dst, atype, sx, sy):
    im = Image.open(path)
    img_size = im.size
    # 用于本地功能，也可以再没有配置分辨率时使用
    if sx == 0 or sy == 0:
        sx = img_size[0]
        sy = img_size[1]

    x = 0
    y = (250*sx)/1080
    h = img_size[1]/2 - 40
    w = img_size[0]
    if atype == 1 or atype == 3:
        y = (250*sx)/1080 #chongding # baidu
    elif atype == 2:
        y = (300*sx)/1080 #xigua # youku
    elif atype == 4:
        y = (400*sx)/1080
    elif atype == 5: # zhihu
        y = (610*sx)/1080
        h = sy-(200*sx/1080)-y
    region = im.crop((x, y, x+w, y+h))
    region.save(dst)

def get_atype(atype):
    atypes = [
        '',
        '冲顶大会',#1
        '今日.百万英雄', #2
        '百度.好看视频', #3
        '优酷.疯狂夺金', #4
        '知乎.头脑王者', #5
        'UC.疯狂夺金', #6
        '蘑菇街.大富翁',#7
        '掌阅.百万文豪',#8
        '映客.芝士超人',#9
        '斗鱼.百万勇者',#10
        'UC.红包赛',#11
        '必要.抢钱冲顶',#12
        '波波视频',#13
        '京东直播',#14
        '百万给你花',#15
        '腾讯视频',#16
        '微博',#17
        '千帆',#18
        ]
    return atypes[atype].decode("utf8")

def crop_img(path, dst, atype, sx, sy):
    im = Image.open(path)
    img_size = im.size
    # 用于本地功能，也可以再没有配置分辨率时使用
    if sx == 0 or sy == 0:
        sx = img_size[0]
        sy = img_size[1]

    x = 0
    y = (250*sx)/1080
    h = img_size[1]/2 - 40
    w = img_size[0]

    crop = [
        [x, w, y, h], #0 xx
        [x, w, (300*sx)/1080, 800*sx/1080],#1 冲顶大会 (1100-300)
        [x, w, (300*sx)/1080, 920*sx/1080],#2 今日。百万英雄 920*sx/1080
        [x, w, (250*sx)/1080, 920*sx/1080],#3 百度。好看视频
        [x, w, (400*sx)/1080, 920*sx/1080],#4 优酷。疯狂夺金
        [x, w, (610*sx)/1080, (1110*sx)/1080], #5 知乎。头脑王者
        [x, w, 404*sx/1080, 885*sx/1080], #6 UC。 疯狂夺金 
        [x, w, 600*sx/1080, 690*sx/1080], #7 蘑菇街.大富翁
        [x, w, 450*sx/1080, 750*sx/1080], #8 掌阅.百万文豪 
        [x, w, 345*sx/1080, 825*sx/1080], #9 映客.芝士超人
        [x, w, 336*sx/1080, 864*sx/1080], #10 斗鱼.百万勇者
        [x, w, 800*sx/1080, 800*sx/1080], #11 UC.红包赛
        [50*sx/1080, w-2*50*sx/1080, 730*sx/1080, 790*sx/1080], #12 必要.抢钱冲顶  4行题目有问题
        [x, w, 390*sx/1080, 880*sx/1080], #13 波波视频
        [60*sx/1080, w-2*60*sx/1080, 320*sx/1080, 912*sx/1080], #14 京东直播
        [88*sx/1080, w-2*88*sx/1080, 885*sx/1080, 825*sx/1080], #15 百万给你花
        [100*sx/1080, w-2*100*sx/1080, 470*sx/1080, 940*sx/1080], #16 腾讯视频 1410-470
        [100*sx/1080, w-2*100*sx/1080, 400*sx/1080, 990*sx/1080], #17 微博 1390-400
        [140*sx/1080, w-2*140*sx/1080, 340*sx/1080, 840*sx/1080], #18 千帆 1180-340
    ]

    x = crop[atype][0]
    w = crop[atype][1]
    y = crop[atype][2]
    h = crop[atype][3]

    region = im.crop((x, y, x+w, y+h))
    region.save(dst)

def write_html_file(path, data):
    f = file(path, 'w')
    f.write('<!DOCTYPE html>')
    f.write('<html>')
    f.write('<body>')
    data = data.replace('<', '&lt;')
    data = data.replace('<', '&gt;')
    f.write(data)
    f.write('</body>')
    f.write('</html>')
    f.close()

def write_file(path, data):
    f = file(path, 'wb')
    f.write(data)
    f.close()

def get_file(path):
    f = file(path, 'rb')
    b = f.read()
    f.close()
    return b

def backup_file(path, atype):
    try:
        dir = "./server"#os.path.dirname(path)
        dst = os.path.join(dir, "backup")
        if not os.path.exists(dst):
            os.mkdir(dst)
        name = '%s_%s.jpg' % (get_atype(atype), time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
        dst = os.path.join(dst, name)
        write_file(dst, get_file(path))
    except:
        pass

def ocr(path, htmlpath, atype, stype, delno, addans, backup, ci, ck, sx, sy, crop=True):
    if os.path.exists(htmlpath):
        os.remove(htmlpath)
    if backup == '1':
        backup_file(path, atype)

    dst = os.path.join(os.path.dirname(path), 'r.jpg')
    #本地支持，不用crop
    if crop == True:
        crop_img(path, dst, atype, sx, sy)
    else:
        dst = path #直接使用1.jpg
    cont = get_ocr(get_img(dst), ci, ck)
    if cont[0] == False:
        write_html_file(htmlpath, str(cont[1]))
        return [cont[1], '请检查网络','','']
    cont1 = cont[1]
    cont = json.loads(cont1)

    ans_count = 3
    if atype == 5:
        ans_count = 4

    if cont.has_key('words_result_num'):
        num = cont['words_result_num']
        if num >= ans_count+1:
            result = cont['words_result']
            question = ''
            maxcnt = num-ans_count
            if atype == 5:
                maxcnt = maxcnt - 2 #去除两处分数
            for i in range(0, maxcnt):
                question = question + result[i]['words']
            ans = []
            for i in range(num-ans_count, num):
                if atype == 4 or atype == 6 or atype==11 or atype==12: #youku uc uchongbao biyao
                    ans.append(result[i]['words'][2:])
                else:
                    ans.append(result[i]['words'])
            
            question = re.sub(re.compile('^\d*[\. ]*'), '', question, count=1)
            if delno == '1':
                question = question.replace("不".decode("utf8"), "")
                question = question.replace("没".decode("utf8"), "")
            addans_key = ["下列", "以下"]
            if addans == '1':
                for key in addans_key:
                    if question.find(key.decode("utf8"))!= -1:
                        for a in ans:
                            question = question + ' ' + a
                        break

            return search(question, ans, htmlpath, stype)
    
    write_html_file(htmlpath, cont1)
    return ["识别图片失败", "请查看错误信息", "", ""]
        
def search(q, ans1, path, stype=1):
    q1 = q
    url = 'http://www.baidu.com/s?wd='+urllib.quote(q1.encode('gbk'))
    if stype == 1:
        url = 'http://www.baidu.com/s?wd='+urllib.quote(q1.encode('gbk'))
    elif stype == 2:
        url = 'https://m.baidu.com/s?word='+urllib.quote(q1.encode('gbk'))
    elif stype == 3:
        url = 'https://www.sogou.com/sgo?query='+urllib.quote(q1.encode('gbk'))
    elif stype == 4:
        url = 'https://www.google.com/search?q='+urllib.quote(q1.encode('gbk'))
    elif stype == 5:
        url = 'http://cn.bing.com/search?go=搜索&qs=ds&form=QBRE&q='+urllib.quote(q1.encode('utf8'))
    elif stype == 6:
        url = 'https://www.so.com/s?q='+urllib.quote(q1.encode('gbk'))
    
    content = ''
    try:
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request)
        content = response.read()
    except Exception as e:
        content = e

    #pattern = re.compile('<script.+?</script>', re.MULTILINE|re.DOTALL)
    #content = re.sub(pattern, '', content)
    content = content.replace('<em>', "<span style='font-size:22px;'><em>")
    content = content.replace('</em>', "</em></span>")
    for a in ans1:
        content = content.replace(a.encode('utf8'), "<span style='font-weight:bold;font-size:32px'><em>"+a.encode('utf8')+"</em></span>")
    
    write_file(path, content)
    
    answ = {}
    i = 0
    for a in ans1:
        answ[i] = {a: str(content.count(a.encode('utf8')))}
        i += 1

    return [q, answ]

if __name__ == '__main__':
    pass
    