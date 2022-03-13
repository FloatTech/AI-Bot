## 基于西瓜酱酱的TF2_GPT-2接入Bot实现
### TF2_GPT的地址[TF2_GPT-2](https://github.com/starxsky/tf2_gpt-2)
## 使用注意
  - 使用前需要先克隆下[TF2_GPT-2](https://github.com/starxsky/tf2_gpt-2的仓库
  - 使用前需要下载对应的[go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases) 可执行文件
  - 本仓库（指的是本仓库的TF2_GPT-2）中的Api.py  和  bot.py  必须在 TF2_GPT-2 的目录下！！！！
   ## 目录图:![image](https://github.com/FloatTech/AI-Bot/blob/main/TF2_GPT-2/%E6%8D%95%E8%8E%B7.PNG)
## 使用方法
     
     1. >> git clone https://github.com/starxsky/tf2_gpt-2
     2. >> python pre_process.py
     3. >> python train_gpt2.py
     4. windows==> go-cqhttp.exe
        Linunx===> ./go-cqhttp
     5. >> python bot.py

# Bot.py中的API配置
```python
     GPT.sequence_gen(
            model_path = "C:\\Users\\xbj0916\\Desktop\\TF2_GPT-2\\TF2_GPT\\model\\",#只有运行完pre_process.py&train_gpt2.py才能看到
            model_param = "C:\\Users\\xbj0916\\Desktop\\TF2_GPT-2\\TF2_GPT\\model\\model_par.json",#只有运行完pre_process.py&train_gpt2.py才能看到
            vocab = "C:\\Users\\xbj0916\\Desktop\\TF2_GPT-2\\TF2_GPT\\data\\bpe_model.model",#只有运行完pre_process.py&train_gpt2.py才能看到
            seq_len = 512,
            temperature = 1,
            top_k = 8,
            top_p = 0.9,
            nucleus_sampling = False, 
            context = "sample context")#文章开头标题
```
- 配置完成后在QQ只需一句“生成文章”即可
## 有关TF2_GPT-2详细信息与使用请移步至[Watermelon's TF2_GPT-2](https://github.com/starxsky/tf2_gpt-2)

## 训练
    1. >> python pre_process.py
    2. >> python train_gpt2.py
# 直接生成文章
    1. >> python sequence_generator.py
    


