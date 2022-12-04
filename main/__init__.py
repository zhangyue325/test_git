import os
import sys

pwd = os.path.abspath(__file__)
print(pwd)
sys.path.append(pwd.split("main")[0])
print(sys.path)