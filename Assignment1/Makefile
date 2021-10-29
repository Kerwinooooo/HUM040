PY = python

test:
	$(PY) test.py

train:
	$(PY) train.py

register:
	$(PY) register.py

grade:
	perl icwb2-data/scripts/score icwb2-data/gold/msr_training_words.utf8 icwb2-data/gold/msr_test_gold.utf8 output/register_msr_test.utf8 > score/register_msr_score.txt
	perl icwb2-data/scripts/score icwb2-data/gold/msr_training_words.utf8 icwb2-data/gold/msr_test_gold.utf8 output/unregister_msr_test.utf8 > score/unregister_msr_score.txt
	perl icwb2-data/scripts/score icwb2-data/gold/pku_training_words.utf8 icwb2-data/gold/pku_test_gold.utf8 output/register_pku_test.utf8 > score/register_pku_score.txt
	perl icwb2-data/scripts/score icwb2-data/gold/pku_training_words.utf8 icwb2-data/gold/pku_test_gold.utf8 output/unregister_pku_test.utf8 > score/unregister_pku_score.txt

all: train register test

clean:
	rm wordseg/* output/*
