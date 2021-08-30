import os
import shutil

"""Create directory """
# os.mkdir("krishna2\\sai.txt")
"""rename directory"""

# os.renames("C:\\Users\\sy21249\\PycharmProjects\\sai\\Automative_python\\krishna3", "krishna4")

"""Delete directories"""
# os.rmdir("krishna2\\sai.txt")

"""move directory """
src = (r"C:\Users\sy21249\PycharmProjects\sai\Automative_python\krishna2")
tar = (r"C:\Users\sy21249\PycharmProjects\sai\krishna2")

shutil.move(src, tar)
# print(os.listdir("C:\\Users\\sy21249\\PycharmProjects\\sai\\Automative_python"))