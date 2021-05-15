sentence = input("Enter a sentence: ")
letter_dict = {i : sentence.count(i) for i in sentence}
print(letter_dict)
