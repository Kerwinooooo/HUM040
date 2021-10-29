import pkuseg

if __name__ == "__main__":
    pkuseg.train("icwb2-data/training/pku_training.utf8",
                 "icwb2-data/testing/pku_test.utf8", "model", train_iter=20)
