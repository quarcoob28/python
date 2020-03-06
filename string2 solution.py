#D.verbing
'''
def verbing(s):
   if len(s) < 3:
     return s
   elif (s[-3:] =='ing'):
     return s + 'ly'
   else:
     return s + 'ing'
print(verbing('singing'))
'''
'''
#E.Not bad
def not_bad(s):
  notV = s.find('not')
  badV = s.find('bad')
  if (badV > notV):
     return s[:notV] + 'good' + s[(badV+3):]
  return s
print(not_bad('This dinner is not bad!'))
 '''
#F.front back
def front_bad(a,b):
   alength = len(a)
   blength = len(b)

  if alength % 2 == 0:
    aindex = alength // 2
  else:
    aindex = (alength // 2) + 1

  if blength % 2 == 0:
    bindex = blength // 2
  else:
    bindex = (blength // 2) + 1

  afront = a[0:aindex]
  aback = a[aindex:]
  bfront = b[0:bindex]
  bback = b[bindex:]
      return afront + bfront + aback + bback
