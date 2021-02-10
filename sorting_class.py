class sorting:
    
    #Initialize object
    def __init__(self,array):
        self.arr = array


    #____________________Bubble Sort_______________________________
    
    def Bubble_sort(self):
        
        isswap = False
        for f in range(len(self.arr) -1 ):
            for s in range(len(self.arr) -1 -f ):
                if self.arr[s] > self.arr[s+1]:
                    self.arr[s],self.arr[s+1] = self.arr[s+1],self.arr[s]
                    isswap = True
            if not(isswap):
                return "alreadly sorted.."
        
        return self.arr
    

    #________________________Insertion Sort__________________________
    
    def Insertion_sort(self):

        for i in range(1,len(self.arr)):
            position = i
            currentValue = self.arr[i]

            #shift value right side
            while position > 0 and self.arr[position-1] > currentValue:
                self.arr[position] = self.arr[position-1]
                position = position-1

            #Inserting : insertin sort
            self.arr[position] = currentValue
        
        return self.arr
    
    
    #________________________Selection Sort__________________________
    
    def Selection_sort(self):
        
        for j in range(len(self.arr)):
            min_value = j
            for k in range( j+1, len(self.arr) ):
                if self.arr[ min_value ] > self.arr[k]:
                    min_value = k
            self.arr[j], self.arr[ min_value ] = self.arr[min_value], self.arr[j]
        
        return self.arr