# chatgpt
​		

​		chatgpt开放api国内无法访问？没有梯子可以代理？本项目借用华为云香港或海外局点的FunctionGraph云服务搭建代理访问chatgpt api，每月免费调用100万次。



### 准备

1、登录华为云控制台选择香港或海外局点，搜索FunctionGraph；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/1.png)

2、函数列表中创建函数，选择创建空白函数，运行时选择Python 3.6；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/2.png)

![image](https://github.com/sixs/chatgpt/blob/main/imgs/3.png)

3、打开函数编辑页面，将本工程中functiongraph.py文件内容粘贴至index.py，ctrl + s即可保存部署；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/4.png)

4、部署完成后，点击设置将执行超时时间改为100秒；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/5.png)

5、准备工作完成后可以进行测试，测试事件内容可以复制项目中 functiongraph测试事件.json 文件内容，其中sk-xxx改为自己的openai key；创建后选择对应测试事件进行测试；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/6.png)

![image](https://github.com/sixs/chatgpt/blob/main/imgs/7.png)

6、测试ok后，点击右上角复制函数URN备用；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/8.png)

7、点击右上角我的凭证进入凭证管理，复制API凭证中对应局点的项目备用，如 ap-southeast-1；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/9.png)

8、点击访问秘钥，新增访问秘钥并下载备用，属于账号信息注意妥善保存；

![image](https://github.com/sixs/chatgpt/blob/main/imgs/10.png)



至此，准备工作完成，获取信息：步骤6中的函数URN（function_urn）、步骤7中的项目（region）、项目8中的访问秘钥（ak、sk）。



### 运行

1、下载工程

```shell
> git clone https://github.com/sixs/chatgpt.git
```

2、修改config.py文件中的配置信息

```Python
# 华为云账号配置
class FunctionGraphConfig:
    ak = "***"
    sk = "***"
    region = "***"
    function_urn = "***"


# flask配置
class FlaskConfig:
    port = 5235
    debug = True
```

3、安装python依赖

```shell
> pip install flask
> pip install huaweicloudsdkfunctiongraph
```

4、运行nginx.py，curl命令测试

```shell
> python nginx.py
# 或者后台运行
> nohup python nginx.py &> nginx.log &
> curl http://ip:5235/v1/chat/completions -H "Authorization: Bearer sk-xxx" -H "Content-Type: application/json" -d '{"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": "What is the OpenAI mission?"}]}'
```

