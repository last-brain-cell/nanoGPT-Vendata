import os
import requests
import tiktoken
import numpy as np

# download the tiny shakespeare dataset
input_file_path = os.path.join(os.path.dirname(__file__), '/kaggle/working/nanoGPT-Vendata/data/shakespeare/input.txt')
# if not os.path.exists(input_file_path):
#     data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
with open(input_file_path, 'w', encoding='utf-8') as f:  # Specify UTF-8 encoding
    with open("/kaggle/working/nanoGPT-Vendata/data/shakespeare/data.txt", "r", encoding="utf-8") as f1:
        f.write(f1.read())

with open(input_file_path, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding
    data = f.read()
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))


# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
