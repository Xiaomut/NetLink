## 1. 环境需求

- pip install requests
- pip install selenium
- 谷歌浏览器（火狐也可，但是得改部分代码，网上也很容易查到）
- webdriver
    - 自己查看谷歌版本并下载版本对应文件，解压后复制到py运行环境的 Scripts 文件夹下，也可在代码中手动设置路径，`executable_path` 那部分加上绝对路径
    - 这里给出谷歌对应的版本[连接](http://npm.taobao.org/mirrors/chromedriver/)

## 2. 使用方法

输入账户和密码，运行即可

## 3. 放入服务器中设置定时任务

可以放在crontab下进行定时启动

我将脚本传到服务器上后，设置为每天运行一次，在早上8点0分运行。

```sh
crontab -e
```

```sh
0 8 */1 * * /绝对路径/python /绝对路径/run.py
```

保存后重启服务，再查看一下定时任务

```sh
service cron restart
crontab -l
```

**可能会报错，如果总是报找不到webdriver的错误，那就把这个webdriver的绝对路径放到webdriver.Chrome(chrome_options=chrome_options) 这句话里。**

---

---

有好的想法和改进措施可以联系我 </br>

author：王帅 20120015 </br>

email：20120015@bjtu.edu.cn </br>