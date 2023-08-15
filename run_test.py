import os

map_of_mapping = {
    'SST-2': {'0':'terrible','1':'great'},
    'sst-5': {0:'terrible',1:'bad',2:'okay',3:'good',4:'great'},
    'mr': {0:'terrible',1:'great'},
    'cr': {0:'terrible',1:'great'},
    'subj': {0:'subjective',1:'objective'},
    'trec': {0:'Description',1:'Entity',2:'Expression',3:'Human',4:'Location',5:'Number'},
    'mpqa': {0:'terrible',1:'great'},
    'CoLA': {'0':'incorrect','1':'correct'},
    'MRPC': {'0':'No','1':'Yes'},
    'QQP': {'0':'No','1':'Yes'},
    'STS-B': {'0':'No','1':'Yes'},
    'MNLI': {'contradiction':'No','entailment':'Yes','neutral':'Maybe'},
    'SNLI': {'contradiction':'No','entailment':'Yes','neutral':'Maybe'},
    'QNLI': {'not_entailment':'No','entailment':'Yes'},
    'RTE': {'not_entailment':'No','entailment':'Yes'},
    'cb': {'0': "entailment", '1':"contradiction", '2':"neutral"},
    'multirc': {'0':'False','1':'True'},
    'boolq': {'0':'False','1':'True'},
}


task = "multirc"
print(f"Run test with {task}")

print("File open")
f = open(f"my_auto_template/{task}/16-42.txt", 'r')
templates = f.readlines()
f.close()
print("File closed")

for template in templates[66:]:
    template = template.strip() + '*mask*'
    mapping = map_of_mapping[task]
    command = f'python run.py --task_name {task} '\
              f'--data_dir data/k-shot/{task}/16-42 '\
              f'--overwrite_output_dir '\
              f'--do_train '\
              f'--do_eval '\
              f'--do_predict '\
              f'--evaluate_during_training '\
              f'--model_name_or_path roberta-large '\
              f'--few_shot_type prompt-demo '\
              f'--num_k 16 '\
              f'--max_steps 1000 '\
              f'--eval_steps 100 '\
              f'--per_device_train_batch_size 2 '\
              f'--learning_rate 1e-5 '\
              f'--num_train_epochs 0 '\
              f'--output_dir result/tmp '\
              f'--seed 42 '\
              f'--template "{template}" '\
              f'--mapping "{mapping}" '\
              f'--num_sample 16'
    print(command)
    os.system(command)
