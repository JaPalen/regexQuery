special_chars = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
output_list = []
     def gather():


        #this is the function gathers input from the user
            global special_chars
            global pattern_list

            userInput = input("Please provide the origin phrase for analysis    ")
            userInput_list = [word for word in userInput]
            pattern_list = []
            #checks for special characters {this is a placeholder}
            for listChar in userInput_list:
                if listChar in special_chars:
                    pattern_list.append(listChar)
                    print("Character {} is a special character.".format(listChar))
             #checks if the character is a digit and appends the pattern list with a \d
                elif listChar.isdigit():
                    pattern_list.append(r'\d')
                    print("Character {} is a digit.".format(listChar))
             #checks if its a letter and appends pattern list with \d
                else:
                    pattern_list.append(r'\w')
                    print("Character {} is a string.".format(listChar))
            print(pattern_list)
        gather()
        def check():
            iteration = 0
            counter = 0
            global output_list

            #code that checks if pattern characters are consecutive

            while iteration <= len(pattern_list):
                for number in range(len(pattern_list)):
                    iteration += 1
                    if iteration == len(pattern_list):

                        #this appends the output list with a quantifier if more than 2 consecutive chars detected
                        if counter > 1:
                            output_list.append(pattern_list[number][1]+"{{{}}}".format(counter+1))
                            return
                        else:
                            output_list.append(pattern_list[number][1])
                            return

                    if pattern_list[number][1] == pattern_list[number+1][1]:
                        counter += 1
                    if (pattern_list[number][1] == pattern_list[number+1][1]) == False:
                        if counter > 1:
                            output_list.append(pattern_list[number][1]+"{{{}}}".format(counter))
                            counter = 0
                        else:
                            output_list.append(pattern_list[number][1])
                break


        #issue - characters in new output_list lack '\'
