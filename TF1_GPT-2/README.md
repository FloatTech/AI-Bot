## 使用TF1的OpenAI官方预训练模型的实现
- [官方模型详情](https://github.com/FloatTech/AI-Bot/blob/main/TF1_GPT-2/DEVELOPERS.md)
- 模型经过改动方便使用
- [Bot.py实现](https://github.com/FloatTech/AI-Bot/blob/main/TF1_GPT-2/src/bot.py)
# 使用前准备
```
1. >> pip install tensorflow==1.15.0
2. >> pip install -r requirements.txt
3. >> python download_model.py 124M //选择模型参数大小 124M,355M,774M,1558M
      python download_model.py 355M
      python download_model.py 774M
      python download_model.py 1558M

```


# 使用时一定要注意将所下载预训练模型的路径添加到api实现文件模型参数的model_dir =中
```python

GPT.interact_model(
    model_name='124M',#所下载模型的名称
    seed=None,
    nsamples=1,
    batch_size=1,
    length=None,
    temperature=1,
    top_k=0,
    top_p=1,
    models_dir='models',#更改为自己所下载的预训练模型地址
    input_m = ''#输入文本接口可在需要调用时定义一个变量并将其索引引用示例请看解释：
)

```
# 运行官方Demo（若不成功需要进行改动生成模块）

```
1.生成随机文本
>> python src/generate_unconditional_samples.py 
2.给定开头生成文章
>> python src/interactive_conditional_samples.py --top_k 40
(查看全部:)
>> python src/interactive_conditional_samples.py -- --help

```

# 实现API
- [API实现](https://github.com/FloatTech/AI-Bot/blob/main/TF1_GPT-2/src/interactive_conditional_samples.py)
- [bot.py实现](https://github.com/FloatTech/AI-Bot/blob/main/TF1_GPT-2/src/bot.py)
- ![Image](https://github.com/FloatTech/AI-Bot/blob/main/TF1_GPT-2/%E6%8D%95%E8%8E%B7.PNG?raw=true)
- 注:API的功能为输入一段命题使GPT-2生成一篇文章，若想实现其他功能欢迎PR！！
# 使用
```
- 新建py文件
- 在py中  import  interactive_conditional_samples 
- 并  from interactive_conditional_samples import 其中的api模型
- 模型参数中有  input_m  (输入文本接口)
```
