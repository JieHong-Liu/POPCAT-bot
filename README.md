# POPCAT auto click script 

## 2021/8月中旬，網路上最紅的popcat meme

![](https://i.imgur.com/leg3NEE.png)

+ 新聞:
    + https://www.marieclaire.com.tw/lifestyle/whats-hot/59440/popcat?atcr=13bd3

+ 規則:
    + 若在30秒按超過800下，系統就會辨識為機器人
+ 解法:
    + 在30秒內按到800下，之後等過了30秒後，再開始下一次的輪迴

+ 使用:
    + 先下載Chrome Webdriver到clone下來的這個資料夾
        + [下載連結](https://chromedriver.storage.googleapis.com/2.38/chromedriver_win32.zip) 
    + 接著install selenium的套件
        ```shell
        $pip install selenium
        ```
    + 然後就 Do RE MI SO!
        ```shell
        $python click.py
        ```
