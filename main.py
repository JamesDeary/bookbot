# define main function
def main():
    #path defined in "" as the file is a string
    path_to_file = "/home/jd/workspace/github.com/JamesDeary/bookbot/book/frankenstein.txt"
    #i think with is like while?
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

#call main function
main()