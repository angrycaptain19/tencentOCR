# tencentOCR
tencentOCR api for image detection


简介：
=====
这是腾讯OCR服务端 基于python flask框架 api 实现。 

注意：
=====
更多信息请查看腾讯官方文档：https://cloud.tencent.com/document/product/866/33526

此api 使用的是 **通用印刷体识别**, 可以在文档中选择其他更适合的 api



腾讯 python SDK :  https://github.com/TencentCloud/tencentcloud-sdk-python 已在Lib 中

在 generalOCR.py 请使用自己的 SecretID and SecretKey  [generalOCR.py](https://github.com/JieruiWangDev/tencentOCR/blob/master/generalOCR.py)


**客户端接入文档** 在官方文档同一页面下


返回格式：Json 文件   [respond.json](https://github.com/JieruiWangDev/tencentOCR/blob/master/static/respondJson/respond.json)  

启动：
=====
运行 app.py<br>
使用postman 工具:  <br>
>>>通过POST请求url: http://127.0.0.1:5000/OCR/images <br>
>>>在 **Body->form-data** 设置 **KEY=images** (选择**file**格式) **VALUE** 插入检测图片    
>>>点击 **Send** 获取json文件
