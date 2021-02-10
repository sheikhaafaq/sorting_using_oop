#main.py

#import modules
import sorting_class

def menu():
    
    
    board = '''\n\t\t Press 1: INPUT ARRAY
    \t\t Press 2: BUBBLE SORT
    \t\t Press 3: INSERTION SORT
    \t\t Press 4: SELECTION SORT
    \t\t Press q: EXIT
    \n\t\t->>'''
    return input(board)

def setup():
    array = []
    while True:
        
        
        option = menu()  
        if option == '1':
            array = list(map(int,input('\n\t\tARRAY ELEMENTS(space separated.)\n\t\t->>').split()))
        
        elif option == '2':
    
            print("\n\t\t BUBBLE SORT")

            #create bubble object of class sorting
            bubble_object = sorting_class.sorting(array)

            #Call Bubble_sort method of class sorting
            print("\t\t",bubble_object.Bubble_sort())

        elif option == '3':
            
            print('\n\t\t INSERTION SORT')

            #create insertion object of class sorting
            insertion_object = sorting_class.sorting(array)

            #Call insertion_sort method of class sorting
            print("\t\t",insertion_object.Insertion_sort())


        elif option == '4':
            
            print(' \n\t\t SELECTION SORT')

            #create selection object of class sorting
            selection_object = sorting_class.sorting(array)

            #Call insertion_sort method of class sorting
            print("\t\t",selection_object.Selection_sort())


        elif option == 'q':
            break
        input('\npress any key to continue...')
        


setup()

    
