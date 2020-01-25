import json
import requests
import re
import configparser
import datetime

SCKEY = "SCU21432T3b2370a9ad026d7d1736ede92fcc176c5a782ec3913s7"

def main():
    push_time()
    news = get_nCov_news()
    last_id = id_get()
    new_id = news['id']
    title = str(new_id) + " . " + news['title']
    message = '❗{}❗\r\n\r\n----\r\n\r\n ⚠️{} \r\n\r\n 👁‍🗨[消息源:{}] ({})\r\n\r\n💊 [丁香园疫情页] (https://3g.dxy.cn/newh5/view/pneumonia)'.format(news['title'], news['summary'], news['infoSource'], news['sourceUrl'])
    print(title)

    if new_id != last_id:
        id_set(str(new_id))
        push_wechat(title, message, SCKEY)
    else:
        print('与上条消息相同')
        print(news)
        pass


def id_get():
    conf = configparser.ConfigParser()
    conf.read('conf.conf')
    last_id = conf.getint('db', 'last_id')
    return last_id


def id_set(new_id):
    conf = configparser.ConfigParser()
    conf.read('conf.conf')
    conf.set('db', 'last_id', new_id)
    conf.write(open('conf.conf', 'w'))


def get_nCov_news():
    dxy_url = 'https://3g.dxy.cn/newh5/view/pneumonia'
    reg = r'<script id="getTimelineService">.+?window.getTimelineService\s=\s(\[.+?\])\}catch\(e\)\{\}</script>'
    content = requests.get(dxy_url).content.decode('utf-8')
    # print(content)
    result = re.search(reg, content)
    if result == None:
        return False
    else:
        result = result.group(1)
        result = json.loads(result)[0]
        # print(result)
        return result

def push_time():
    now_time = int(datetime.datetime.now().strftime('%H'))
    # print(now_time)
    if (now_time < 7 or now_time > 23):
        print("夜间停止推送")
        exit()

def push_wechat(title, message, SCKEY):
    ur = 'https://sc.ftqq.com/{}.send'
    url = ur.format(SCKEY)
    data = {"text": title,
            "desp": message}
    r = requests.post(url, data)
    print(r.text)

if __name__ == "__main__":
    main()