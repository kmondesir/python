import os
import re

home = os.environ.get('HOME')
OneDrive = 'OneDrive'
directory = os.path.join(home, OneDrive)
chars = '[' + re.escape('~"#%&*:<>?/\{|}+!=') + ']' + '+'
c = 0
d = 0
print(directory)
print(chars)


def matchSpecialChars(value):
  pattern = re.compile(chars)
  if pattern.search(value) == None:
    return False
  else:
    return True


def replaceSpecialCharsWithUnderScores(value):
  replacement = re.sub(chars,'_',value)
  return replacement.strip() #remove spaces from the beginning and ending of string

for root, folders, items in os.walk(directory, topdown=True):
  for folder in folders:
    if matchSpecialChars(folder) == True:
      current = os.path.join(root,folder)
      new = os.path.join(root,replaceSpecialCharsWithUnderScores(folder))
      print(current)
      print(new)
      print('')
      c = c + 1
  #os.rename(current, new)
  for item in items:
    if matchSpecialChars(item) == True:
      current = os.path.join(root,item)
      new = os.path.join(root,replaceSpecialCharsWithUnderScores(item))
      print(current)
      print(new)
      print('')
      d = d + 1
#os.rename(current,new)

print('folders:' + str(c))
print('files:' + str(d))