# exercise 1 

#main tuple for name and itenerary 
tuple_itenerary = (("John", "Denver", "New York"),("Steve", "Tuscon", "Des Moines"))

#function that recieves the tupple prints out each itenerary  
def list_itenerary(tuple_itenerary):
    for i, itenerary in enumerate(tuple_itenerary, 1):
        iten_name = itenerary[0]
        iten_origin = itenerary[1]
        iten_dest = itenerary[2]
        iten_num_str = str(i)
        print(f"Itinerary {iten_num_str}: {iten_name} - From {iten_origin} to {iten_dest}")

#call the function and recieve the tulple_itenerary tuple 
list_itenerary(tuple_itenerary)



