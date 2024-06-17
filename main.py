# define main function
def main():
    # path defined in "" as the file is a string
    path_to_file = "/home/jd/workspace/github.com/JamesDeary/bookbot/book/frankenstein.txt"

    # open the file and name f, so file can be read and print its contents
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)

    # call function word count
    total_words = word_count(file_contents)
    #print(f"The number of words in this document = {total_words}")

    # call character count function
    total_characters = character_count(file_contents)
    #print(f"The character count is as follows: {total_characters}")

    # call convert_dict
    converted_dict = convert_dict(total_characters)
    #print(converted_dict)

    # sort newly converted dictionary
    converted_dict.sort(reverse=True, key=sort_on)
    #print(converted_dict)

    # begin printing report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document")
    print("")
    for a in converted_dict:
        for key, value in a.items():
            print(f"The character {key} was found {value} times.")

    print("--- End report ---")

# define a function to count words in file
def word_count(file_contents):
    words = file_contents.split()
    return(len(words))

# define a function to count characters in file
def character_count(file_contents):

    # convert file_contents to lowercase
    lowered_string = file_contents.lower()
    new_dict = {}

    # split lowered words into list of lowered words
    lowered_words = lowered_string.split()
    new_list = list()

    # get list of words into list of characters
    for a in lowered_words:
        new_list+=a

    # iterate over list of characters and store character as key and value as total number of them
    for a in new_list:
        if a.isalpha(): 
            if a in new_dict:
                new_dict[a] +=1
            elif a not in new_dict:
                new_dict[a] = 1
    return (new_dict)


# define a function to convert single dictionary into list of dicts, not tuples - iteration matters
def convert_dict(total_characters):
    new_list = list({key: value} for key, value in total_characters.items())
    return (new_list)

# define a function to sort on       
def sort_on(converted_dict):
    return list(converted_dict.values())[0]



# call main function
main()