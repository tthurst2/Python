import re

inFile = 'Files/userlist.txt'
outFile = 'Files/userOutput.txt'
pattern = r'.*?         (\d{2,4})\s+([A-Z]\S*)\n.*?Full Name: ([\w]+.*?)\n.*?Last Login: (.*?) Password Expires: (.*?) Multiple Login: (.*?)\n.*?Groups: (.*?\n)'
new_file =[]
f = open(inFile, "r")
text = f.read()
#print text


outputFile=  re.findall(pattern, text, re.DOTALL)
f = open(outFile, "w")
#print outputFile
f.write("ID" + "|" +  "USERNAME" + "|" + "FULL NAME" + "|" + "LAST LOGIN" + "|" + "M. LOGIN" + "|" + "GROUPS" + "\n")
for output in outputFile:
  f.write(output[0]+ "|" +  output[1].strip() + "|" + output[2].strip() + "|" +  output[3].strip() + "|" +  output[4].strip() + "|" +  output[5].strip() + "|" + output[6].replace('|', ','))