import torch
import jieba
import os
import numpy as np

from Dtasest import MyDataset
from Layers import Config
from Layers import utils
from Layers.Model import GPT_Model


GPT = GPT_Model#模型
GPTconfig = Config.GPTConfig#模型配置
Sample = utils.sample#示例


def save_txt(model_path:str,train_data_name:str,context:str,steps:int):
    """
    :param pre_model_path: 预训练模型的位置
    :param train_data_name: 训练用的数据
    :param context: 生成文章的标题
    :param steps: 生成文章的字数
    :return:
    """

    path_ = os.path.join('datas', train_data_name)
    f = open(path_, encoding='utf-8').read()
    aa = jieba.lcut(f)
    #print(aa)
    # 构建 GPT 模型
    train_dataset = MyDataset(aa, 20)
    mconf = GPTconfig(train_dataset.vocab_size, train_dataset.block_size, n_layer=12, n_head=12, n_embd=768)  # a GPT-1
    model = GPT(config=mconf)
    #print(model)
    #加载预训练模型
    pre_model_path = os.path.join('Pre_models', model_path)
    model.load_state_dict(torch.load(pre_model_path, map_location='cpu'))

    x = torch.tensor([train_dataset.stoi[s] for s in context], dtype=torch.long)[None, ...]
    y = Sample(model, x, steps=steps, temperature=1.0, sample=True, top_k=10)[0]
    completion = ''.join([train_dataset.itos[int(i)] for i in y])
    f = open('save.txt','w',encoding='utf-8')
    f.write(completion)
    f.close()




