import os
from datasets import load_dataset

tasks = ['boolq', 'cb', 'multirc']

for task in tasks:
    if not os.path.exists(f"original/{task}"):
        os.mkdir(f"original/{task}")
    dataset = load_dataset('super_glue', task)
    dataset['train'].to_csv(f"original/{task}/train.tsv", sep='\t', index=False)
    dataset['validation'].to_csv(f"original/{task}/dev.tsv", sep='\t', index=False)
