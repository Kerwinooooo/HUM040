import os
import pkuseg


def test(filepath):
    with open(filepath, encoding="utf-8") as fin:
        content = fin.readlines()

        seg = pkuseg.pkuseg(model_name="./model", user_dict="dict/dict.txt")
        with open("output/unregister_" + os.path.split(filepath)[1], mode="w", encoding="utf-8") as fout:
            for line in content:
                text = seg.cut(line)
                fout.write("  ".join(text) + "\n")

        seg = pkuseg.pkuseg(model_name="./model", user_dict="dict/wordseg.txt")
        with open("output/register_" + os.path.split(filepath)[1], mode="w", encoding="utf-8") as fout:
            for line in content:
                text = seg.cut(line)
                fout.write("  ".join(text) + "\n")
    print("test", filepath)
        

if __name__ == '__main__':
    test("icwb2-data/testing/msr_test.utf8")
    test("icwb2-data/testing/pku_test.utf8")
