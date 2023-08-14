for seed in 42
do
    for bs in 8
    do
        for lr in 1e-5 2e-5 5e-5
        do
            TAG=exp \
            TYPE=prompt-demo \
            TASK=multirc \
            BS=$bs \
            LR=$lr \
            SEED=$seed \
            MODEL=roberta-large \
            bash run_experiment.sh
        done
    done
done