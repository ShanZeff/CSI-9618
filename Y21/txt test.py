import os

# "/PycharmProjects/CSI-9618/Y21/DataToAdd.txt"
# "/PycharmProjects/CSI-9618/Y21/"
# C:/Users/shnaya/Desktop/Practical 21/original copy/DataToAdd.txt

# Path = "C:/Users/shnaya/PycharmProjects/CSI-9618/Y21/" + input("Enter a filename: ")
# FileName = os.path.isfile(Path)
# print(FileName)

# Path = "C:/Users/shnaya/PycharmProjects/CSI-9618/Y21/" + input("Enter a filename: ")
# FileName = os.path.isfile(Path)

# /Users/shnaya/PycharmProjects/CSI-9618/Y21
# /Users/shnaya/PycharmProjects/CSI-9618/
# os.chdir("/Users/shnaya/PycharmProjects/CSI-9618/")
# 'DataToAdd.txt', 'SecondData.txt',
# DataToAdd.txt

# print(os.getcwd())
# print(os.listdir())

FileName = input("Enter a filename: ")
with open(FileName, "r") as f:
    f_contents = f.read()
    print(f_contents)
