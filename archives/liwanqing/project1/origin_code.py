from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import jieba
import re
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3,6"

# 检查CUDA支持并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 加载模型和分词器，将模型转移到设备
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-chinese').to(device)
model.eval()  # 设置为评估模式

# 获取文本的BERT嵌入
def get_batch_embedding(texts, model, tokenizer):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].detach()

# 读取和预处理数据
with open('documents.txt', 'r', encoding='ansi') as f:
    data = f.readlines()
text = ''.join(data)
text = "".join(re.findall('[\u4e00-\u9fa5]+', text, re.S))

# 分词处理
words_in_long_text = list(set(jieba.cut(text)))  # 使用集合去重

# 计算相似度
def calculate_similarity(embedding1, embedding2):
    return cosine_similarity(embedding1.cpu().numpy(), embedding2.cpu().numpy())[0][0]

# 输入词语和长文本
input_words = ["创新"]

# 为输入词语计算嵌入
input_word_embeddings = get_batch_embedding(input_words, model, tokenizer)

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
for word, sim in sorted_similar_words[:10]:  # 输出前10个最相似的词
    print(f"Word: {word}, Similarity: {sim}")
