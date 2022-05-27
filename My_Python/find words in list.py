def find_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	

string = input("Enter your String : ")
n = int(input("Enter your threshold length : "))

print(find_words(n, string))