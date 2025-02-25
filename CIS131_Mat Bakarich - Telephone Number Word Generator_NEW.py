
def main():

    # import deque
    from collections import deque
    
    # initalize words as a string
    words = "" 

    def phonewords():
        # intialize number as an integer
        number =0
    
        # initialize words_list as a string
        words_list = ""
        # initialize prefix as a string
        prefix =""
        # initialize phone as a list with letters mapped to indices that correspond with the number on the keypad.
        phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "prs", "tuv", "wxy"]
        # initialize result as a list for temporary storage
        result = []

        # get user input for phone number
        number = input("Please enter your phone number.\n")

        # remove 0 and 1 from input number
        number = number.strip('01')

    

        # store the combinations
        words_list = deque()

        # Start with an empty string
        words_list.append("")

        # loop to create possible words
        while words_list:
        
            # Get the first string from the queue
            prefix = words_list.popleft()

            # compare length of strings
            if len(prefix) == len(number):
               result.append(prefix)
            else:
                # Get the corresponding digit
                digit = number[len(prefix)]

        

                # Add all possible letters for this digit
                for letter in phone[(int(digit))]:
                    words_list.append(prefix + letter)

        return result 


    # call phonewords and assign the result to "words".
    words = phonewords()

    
    # print the list of words to the user
    print(" ".join(words))


    # output words to wordslist.txt
    with open('wordslist.txt', mode='w') as wordslist:
        for word in words:
            print(word,file=wordslist)


# call to main
main()