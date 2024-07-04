# task 2 
import sys 

#main library 
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#Ask the user if they would like to add a new book 
def add_book(library):
    while True:
        new_book_question = input("Would you like to add a new book?(Y/N): ")
        while new_book_question not in ["Y", "N"]:
            new_book_question = input("Press either 'Y' or 'N': ")
        if new_book_question == "N":
            break

#Get the Title and the author from the user     
        recieve_new_title = input("Title: ")
        for book in library: 
            while recieve_new_title == book[0]:
                recieve_new_title = input("Book title already listed, please try again: ")   
        recieve_new_author = input("Author:")
        new_book_tuple = (recieve_new_title, recieve_new_author)
        library.append(new_book_tuple)

#see if the user wants to add another book 
        another_book_question = input("Would you like to add another new book?(Y/N): ")
        while another_book_question not in ["Y", "N"]:
            new_book_question = input("Press either 'Y' or 'N': ")
        if another_book_question == "N":
            break 


#Run the function and then print the library with the new book(s)
add_book(library)
print(library)




