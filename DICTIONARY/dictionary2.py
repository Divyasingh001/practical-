#WAP to delete a key from Dictionary
fruitsDict = {
  'Apple': 100,
  'Orange': 200,
  'Banana': 400,
  'pomegranate':600
}
if 'Apple' in fruitsDict: 
    del fruitsDict['Apple']
 
print('Dict after deleting key =',fruitsDict)
