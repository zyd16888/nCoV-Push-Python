# nCoV-Push-Python

nCoV微信推送脚本，基于Server酱，数据来源于丁香园

修改自 [easychen/nCoV-push](https://github.com/easychen/nCoV-push) ,因原作使用 php 会出现爬取不成功的情况，故改为 python 实现


## 使用方法

1. 注册[Server酱](http://sc.ftqq.com/)
2. 绑定微信，拿到 `SCKEY`
3. 修改 `push.py` 中的 `SCKEY` 字段
4. 运行代码，查看效果

## 运行方法

运行环境： `python3` 以上

安装依赖

```
pip install -r requirements.txt
```

执行程序

```
python push.py
```

## 定时任务配置

```
crontab -e

# 每两分钟执行一次脚本
*/2 * * * * python3 /root/push.py >/dev/null 2>&1
```

## 注意事项

1. 在服务器运行时 `push.py` 中的  `conf.conf` 文件路径可能需要修改

![img1](https://github.com/zyd16888/nCoV-Push-Python/blob/master/image/20200125173902.png)

## 效果截图

![img2](https://github.com/zyd16888/nCoV-Push-Python/blob/master/image/20200125173927.jpg)
