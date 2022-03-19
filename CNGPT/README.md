 # 基于StarxSky的CNGPT中文GPT-2接入Bot的实现

 ## 使用方法（和以前一样先上目录图） 
 ![im](https://github.com/FloatTech/AI-Bot/edit/main/CNGPT/READ/t.png)
 - Steps 1 :
 - 使用前需要先git clone 克隆下来[GPT-2](https://github.com/StarxSky/GPT-2)的仓库
 - 并在其中找到```CNGPT```文件，进入
 - 在```CNGPT```目录下执行```pip install -r requirments.txt```安装所需的包
 - 将此仓库的```API.py```和```bot.py```移动到```CNGPT```目录下
 ### 您需要修改```bot.py```的以下代码：
 - 将您下载的或者通过```CNGPT```训练的模型填写到对应的位置
 - 将```CNGPT```目录下的```datas```中的```train.text```填写到对应的位置
 - 注意！！您用哪种文本语料训练的```CNGPT```您就需要把您的语料路径填写进去！！(默认的语料库是```datas```中的```train.text```)
 - 如果还有问题或者详细的如何训练CNGPT语言模型请[点击这里查看CNGPT的详情](https://github.com/StarxSky/GPT-2/blob/main/CNGPT/README.md)
 ```python
 
 # GPT-2生成文章插件
class GeneratePlugin(Plugin):
    def match(self):
        return self.on_full_match('生成文章')

    def handle(self):
        GPT.save_txt(context='你好！', # 文章题目
                     steps='20', # 生成文章的字数
                     model_path='', #模型存放的路径
                     train_data_name='' #训练数据的文件名字
                     )

        f = open('save.txt', encoding='utf-8').read()
        self.send_msg(text('哒哒哒~~~生成完成：{}'.format(f)))
```
