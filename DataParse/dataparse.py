import re

inFile = 'Files/userlist.txt'
outFile = 'Files/userOutput.txt'
pattern = r'^         (\d{2,4})\s+([A-Z]\S*)\n.*Full Name: ([\w]+.*)\n.*Last Login: (.*) Password Expires: (.*) Multiple Login: (.*)\n\n.*Groups: (.*?)\n'
new_file =[]
f = open(inFile, "r")
text = f.read()
#print text


outputFile=  re.findall(pattern, text, re.DOTALL)
print outputFile
for output in outputFile:
  print output[0]+ ", " +  output[1].strip() + ", " + output[2].strip() + ", " +  output[3].strip() + ", " +  output[4].strip() + ", " +  output[5].strip() + ", " + output[6]  
  print "hello"
