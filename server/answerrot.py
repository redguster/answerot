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

'''
1 冲顶大会
2 今日。百万英雄
3 百度。好看视频
4 优酷。疯狂夺金
5 知乎。头脑王者
6 UC。 疯狂夺金
7 蘑菇街.大富翁
8 掌阅.百万文豪
9 映客.芝士超人
10 斗鱼.百万勇者
'''
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
        [], #0 xx
        [(300*sy)/1920, img_size[1]/2-100], #1 冲顶大会
        [(300*sy)/1920, h], #2 2 今日。百万英雄
        [(250*sy)/1920, h], #3 百度。好看视频
        [(400*sy)/1920, h], #4 优酷。疯狂夺金
        [(610*sy)/1920, (1110*sy)/1920], #5 知乎。头脑王者
        [404*sy/1920, 885*sy/1920], #6 UC。 疯狂夺金 
        [600*sy/1920, 686*sy/1920], #7 蘑菇街.大富翁 
        [450*sy/1920, 750*sy/1920], #8 掌阅.百万文豪
        [345*sy/1920, 825*sy/1920], #9 映客.芝士超人 
        [336*sy/1920, 864*sy/1920], #10 斗鱼.百万勇者  
    ]

    y = crop[atype][0]
    h = crop[atype][1]

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
    f = file(path, 'w')
    f.write(data)
    f.close()

def ocr(path, htmlpath, atype, stype, ci, ck, sx, sy, crop=True):
    if os.path.exists(htmlpath):
        os.remove(htmlpath)
    dst = os.path.join(os.path.dirname(path), 'r.jpg')
    #本地支持，不用crop
    if crop == True:
        crop_img(path, dst, atype, sx, sy)
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
                ans.append(result[i]['words'])

            question = re.sub(re.compile('^[\d\.]*'), '', question, count=1)
            return search(question, ans, htmlpath, atype, stype)
    
    write_html_file(htmlpath, cont1)
    return ["识别图片失败", "请查看错误信息", "", ""]
        
def search(q, ans, path, atype, stype=1):
    ans1 = []
    if atype == 4 or atype == 6: #youku uc
        for a in ans:
            ans1.append(a[2:])
    else:
        ans1 = ans

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

    pattern = re.compile('<script.+?</script>', re.MULTILINE|re.DOTALL)
    content = re.sub(pattern, '', content)
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
    