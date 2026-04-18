#              0      1        2         3         4     #index
fruitlist = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']
print("Number of elements in fruitlist: ", len(fruitlist))
print("Length: ", len(fruitlist))
print("First Element:", fruitlist[0])
fruitlist.append('Papaya')
print("Updated List: ", fruitlist)
fruitlist.sort()
print("Sorted List: ", fruitlist)
fruitlist.remove('Guava')
print("Updated List: ", fruitlist)
fruitlist.reverse()
print("Reversed List: ", fruitlist)
slicedfruitlist = fruitlist[1:4]
print("Sliced List: ", slicedfruitlist)
