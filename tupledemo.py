##create tuple
myfriend = tuple(("avi","soap","ghost","price","tokito"))
# print(myfriend)

##to access the elements using indexing
# print(myfriend[0])

##to access the elements using range
# print(myfriend[1:5])  #from index 1 to  2 (not include 3)

##to access every elements from tuple
# for i in myfriend :
#     print(i)

# print(myfriend[-2])

##update a tuple, it will give an error because tuples are immutable/unchangable.
# myfriend[4] = "tokito muichiro"
# print(myfriend)

##to update tuple using typecasting/or indirectly/using list
# toList = list(myfriend)
# toList[4] = "tokito muichiro"
# myfriend = tuple(toList)
# print(myfriend)

##to delete/modify elements in tuple we need to convert into list 
# toList = list(myfriend)
# toList.remove("avi")
# myfriend = tuple(toList)
# print(myfriend)

##to add in tuple
# toList = list(myfriend)
# toList.append("muzan")
# myfriend = tuple(toList)
# print(myfriend)

##delete the tuple
# del myfriend
# print(myfriend)

##merge two tuple
friend = ("omen","cypler","yuro","avi")
mergetuple = myfriend + friend
print(mergetuple)


