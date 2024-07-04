class Book:
    def __init__(self,name,year,authors,keyword):
        self.name = name
        self.year = year
        self.authors = authors
        self.keyword = keyword

class Library:
    def __init__(self,id,name):
        self.id = id
        self.name = name 
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        self.books.remove(book)

    def edit_book(self,oldbook,newbook):
        index = self.books.index(oldbook) 
        self.books[index] = newbook
        

class Librarymanagement:
    def __init__(self):
        self.libraries = []
    def save_information(self):
         with open("University_libraries.txt", "w") as librariesfile:
            for library in self.libraries:
                librariesfile.write(f"{library.id}|{library.name}\n")
                with open(f"{library.id}-{library.name}.txt", "w") as bookfile:
                    for book in library.books:
                        authors_str = ",".join(book.authors)
                        bookfile.write(f"{book.name}|{book.year}|{authors_str}|{book.keyword}\n") 

    def load_information(self):   
        try:
            with open("University_libraries.txt", "r") as librariesfile:
                listlib = librariesfile.readlines()
                for line in listlib:
                    line = line.strip().split("|")
                    library = Library(line[0], line[1])
                    self.libraries.append(library)
                    try:
                        with open(f"{line[0]}-{line[1]}.txt", "r") as booksfile:
                            listbooks = booksfile.readlines()
                            for bookline in listbooks:
                                bookline = bookline.strip().split("|")
                                authors_list = bookline[2].split(",")
                                book = Book(bookline[0], bookline[1], authors_list, bookline[3])
                                library.add_book(book)
                    except FileNotFoundError:
                        pass
        except FileNotFoundError:
            pass

    def runprogram(self):
        self.load_information()
        while True:
            print("1 : add new library\n2 : add new book to the library\n3 : remove library\n4 : remove book to the library\n5 : Edit book to the library\n6 : print information\n7 : save and exit")
            input_number = int(input("Enter the number : "))
            if input_number == 1:   
                input_library_id = input("enter library id : ")
                input_library_name = input("library name : ")
                new_library = Library(input_library_id,input_library_name)
                self.libraries.append(new_library)

            if input_number == 2 :
                find_library_id = input("Enter id library : ")
                for library in self.libraries:
                    if library.id == find_library_id:
                        name_book = input("name book : ")
                        year_book = input("year of publication : ")
                        keyword_book = input("keyword book : ")
                        authors_book = input("authors book (separated => ,) : ").split(",")
                        new_book = Book(name_book,year_book,authors_book,keyword_book)
                        library.add_book(new_book)

            if input_number == 3 :
                remove_library_id1 = input("Enter library id to remove : ")
                for library in self.libraries:
                    if library.id == remove_library_id1:
                        self.libraries.remove(library)

            if input_number == 4:
                remove_library_id2 = input("Enter library id to remove book : ")
                remove_book = input("name book to remove : ")
                for library in self.libraries:
                    if library.id == remove_library_id2:
                        for book in library.books:
                            if book.name == remove_book:
                                library.remove_book(book)
                                
            if input_number == 5:
                change_input = input("Enter library id to change book : ")
                old_book = input("name book to change : ")
                new_book = input("new name for book : ")
                for library in self.libraries:
                    if library.id == change_input:
                        for book in library.books:
                            if book.name == old_book:
                                library.edit_book(book,Book(new_book,book.year,book.authors,book.keyword))             
            if input_number == 6:
                list_of_books = []
                for library in self.libraries:
                    if len(library.books) != 0 :  
                        for book in library.books:
                            list_of_books.append([f"name book = {book.name}  ,  year of publication = {book.year} ,  authors = {book.authors} ,  keyword = {book.keyword}"])
                    print(f"name , id library = ({library.name} , {library.id}) and Books =  {list_of_books}") 
                    list_of_books = []
            if input_number == 7:
                self.save_information()
                break        
obj1 = Librarymanagement()
obj1.runprogram()  
                          
            
            


                               
