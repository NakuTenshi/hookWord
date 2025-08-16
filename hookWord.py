import random 
import argparse
import os 


parser = argparse.ArgumentParser(
    description="hookWord: a tool for generating hook wordlists to improve fuzzing accuracy"
)
parser.add_argument("-w", required=True, help="Specify the main word for the hook wordlist")

args = parser.parse_args()

word = args.w 
  
misc_numbers = [str(i*10) for i in range(50)]
for i in range(2):
    misc_numbers.append(word)
random.shuffle(misc_numbers)

with open("hook.txt" , "w")as f:
    f.write("\n".join(misc_numbers))
    os.system("clear")
    print("result saved at: ./hook.txt")

