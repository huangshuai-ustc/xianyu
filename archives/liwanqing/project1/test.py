from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import jieba
import re
import os
import json
from tqdm import tqdm
os.environ["CUDA_VISIBLE_DEVICES"] = "3,4,6"

# 检查CUDA支持并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 加载模型和分词器，将模型转移到设备
tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')
model = BertModel.from_pretrained('./bert-base-chinese').to(device)
model.eval()  # 设置为评估模式

# 获取文本的BERT嵌入
def get_batch_embedding(texts, model, tokenizer):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].detach()

# 读取和预处理数据
with open('documents.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
text = ''.join(data)
text = "".join(re.findall('[\u4e00-\u9fa5]+', text, re.S))

# 分词处理
words_in_long_text = list(set(jieba.cut(text)))  # 使用集合去重

# 计算相似度
def calculate_similarity(embedding1, embedding2):
    return cosine_similarity(embedding1.cpu().numpy(), embedding2.cpu().numpy())[0][0]

# 输入词语和长文本
# input_words = ["创新",'创新的','创造力','创造性的','创造','激情','热情的','效率','高效的','卓越','自豪','团队合作','合作','合作的']
input_words = ["诚信","伦理","伦理的","有责任的","责任感","信任","诚实","诚实的","诚实地","公平","责任""负责的","透明度","透明的","尊重的","才能","有才华的","员工","尊严","授权","质量","客户","客户承诺","奉献","奉献的","客户期望"]
f1 = open('2.txt','w',encoding='utf-8')
for input_word in tqdm(input_words, total=len(input_words)):
    # 为输入词语计算嵌入
    input_word_embeddings = get_batch_embedding(input_word, model, tokenizer)
    # 为长文本中的词语批量计算嵌入
    batch_size = 64  # 可根据GPU内存调整批大小
    results = {}
    for i in range(0, len(words_in_long_text), batch_size):
        batch_words = words_in_long_text[i:i+batch_size]
        batch_embeddings = get_batch_embedding(batch_words, model, tokenizer)
        for word, embedding in zip(batch_words, batch_embeddings):
            similarity = calculate_similarity(input_word_embeddings, embedding.unsqueeze(0))
            results[word] = similarity
    # 按相似度排序并输出结果
    sorted_similar_words = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # 输出结果
    result = []
    resultss = {}
    for word, sim in sorted_similar_words[:100]:
        result.append([word, str(sim)])
        resultss[str(input_word)] = result
    f1.write(json.dumps(resultss, ensure_ascii=False) + '\n')
    print(input_word,'\tdown')
print('ok')