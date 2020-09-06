def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    sentence2=sentence.swapcase()
    test=list(sentence2.split())
    test[0],test[-1]=test[-1],test[0]
    print(test)
    final_sentence=" "
    final_sentence=final_sentence.join(test)
    print( final_sentence)
        
reverse_words_order_and_swap_cases("aWESOME is cODING")
