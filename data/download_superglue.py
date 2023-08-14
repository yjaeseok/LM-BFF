from datasets import load_dataset

tasks = ['boolq', 'cb', 'multirc']

for task in tasks:
    dataset = load_dataset('super_glue', 'rte')
    dataset['train'].to_csv(f"original/{task}/train.tsv", sep='\t', index=False)
    dataset['dev'].to_csv(f"original/{task}/dev.tsv", sep='\t', index=False)