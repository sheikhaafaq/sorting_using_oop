import sorting_class
print('SELECTIN SORT')
db = [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]

#create selection object of class sorting
selection_object = sorting_class.sorting(db)

#Call insertion_sort method of class sorting
selection_object.Selection_sort()

