def display_menu():
    print("MOVIE LIST MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def list(movie_list):
    i = 1
    for movie in movie_list:
        print(str(i) + "- " + movie)
        i += 1
    print()

def add(movie_list): #mutable list
    movie = input("Name: ")
    movie_list.append(movie)
    print(movie + " was added. \n")

def delete(movie_list):

    number = int(input("Enter Movie Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie num. \n")
    else:
        movie = movie_list.pop(number-1)
        print(movie + " was deleted. \n")

def main():
    movie_list = ["Month Python",
                  "Lord of the Rings",
                  "Titanic"]
    command_list = ["list", "add", "del", "exit"]
    display_menu()
    # code to process each choice made


    #for i in range (5):
    m_command = input("Enter a valid movie list menu option: ")
    while m_command in command_list:

        if m_command == "list":
            list(movie_list)
        elif m_command == "add":
            add(movie_list)
        elif m_command == "del":
            delete(movie_list)
        elif m_command == "exit":
            break
        else:
            print("Not a valid movie list command. Try again.\n")
        m_command = input("Enter a valid movie list menu option: ")
    print("Movie List program ended.")

main()