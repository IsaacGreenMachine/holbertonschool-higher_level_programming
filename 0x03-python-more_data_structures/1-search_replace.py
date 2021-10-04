def search_replace(my_list, search, replace):
    return [x if x is not search else replace for x in my_list]

''' C Way:
a = my_list.copy()
for i in range(len(a)):
if a[i] == search:
a[i] = replace
return a
'''
