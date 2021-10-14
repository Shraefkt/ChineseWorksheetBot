import scraper
import random
import argparse

parser = argparse.ArgumentParser(description="Converts a text file of words into a worksheet")
parser.add_argument('File',metavar='file',type=str,help="file of words to convert")

args = parser.parse_args()
filename = args.File

sentences = scraper.scrape(filename)

text = ""
answers = ""

words = list(sentences.keys())
random.shuffle(words)

text += "_" * 70 + "\n"

for i in range(len(words)):
    text += words[i]
    text += "   |   "
    if i%5 == 4:
        text+= "\n" + "_" * 70 + "\n"
text+="\n"
random.shuffle(words)

for i in range(len(words)):
    sentence = sentences[words[i]].replace(words[i],"_______")
    text += f"{i+1}. {sentence}\n\n"
    answers += f"{i+1}. {words[i]}\n\n"

text += "\n\n\n"
text += answers

with open("worksheet.txt","w",encoding="utf-8") as f:
    f.write(text)
