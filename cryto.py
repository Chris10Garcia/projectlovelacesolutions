def break_caesar_cipher(hidden_text, word):

    # hidden_text = hidden_text.lower()
    hidden_text_split = hidden_text.split()
    word = word.upper()

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = list(alpha)
    key = len(alpha)
    a_to_num = {}
    num_to_a ={}

    z = 0
    
    #creates 2 dictionaries: from letter to number and from number to letter
    for a in alpha:
        a_to_num[a] = z
        num_to_a[z] = alpha[z]

        z+=1

    # this for loop brute fources each shift in the alpha bet

    for shift in range(0,key):
        
        new_word = list()

        # this for loop determins the new given word with the shift
        for w in word:
            new_word_index = a_to_num[w] - shift

            # if index is past 26, starts back from first index
            if new_word_index < 0 :
                new_word_index += key
            new_word.append(num_to_a[new_word_index])
    
        new_word = "".join(new_word)

        # checks if the shifted given word is in hidden phrase
#        next(new_word for new_word in hidden_text.split())
        # if len(set(new_word).intersection(hidden_text))>0:

        for u in hidden_text_split:

            if new_word == u:

                #write code that converts hidden word into phrase based on - shift
                #seperate string into list
                #then go through the list
                    #letter : value, then value - shift, then new value : #hidden_letter
                    #fill single variable from itterations of #hidden_letter

                hidden_text = list(hidden_text)
                new_hidden_word = list()

                for h in hidden_text:
                    if h == " " or h == ",":
                        new_hidden_word.append(h)
                    else:
                        new_hidden_text_index = a_to_num[h] + shift
                    
                        if new_hidden_text_index > key -1:
                            new_hidden_text_index -= key
                        new_hidden_word.append(num_to_a[new_hidden_text_index])
                    
                new_hidden_word = "".join(new_hidden_word)

                break
            
            else:
                new_hidden_word = False
        
        if new_hidden_word is not False:
            break
        

        

        # print(new_word + "inside of loop")
        #end of brute force iteration
    
    # print(new_hidden_word)
    #end of function
    return new_hidden_word.lower()

    
    


print(break_caesar_cipher('OMXX YQ UETYMQX EAYQ KQMDE MSA ZQHQD YUZP TAI XAZS BDQOUEQXK TMHUZS XUFFXQ AD ZA YAZQK UZ YK BGDEQ MZP ZAFTUZS BMDFUOGXMD FA UZFQDQEF YQ AZ ETADQ U FTAGSTF U IAGXP EMUX MNAGF M XUFFXQ MZP EQQ FTQ IMFQDK BMDF AR FTQ IADXP', 'I'))


