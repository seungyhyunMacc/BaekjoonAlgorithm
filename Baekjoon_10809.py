from string import ascii_lowercase

input_word=list(input())
alpha_list = list(ascii_lowercase)

for i in alpha_list:
    if i in input_word:
        print(input_word.index(i), end=' ')
    else:
        print(-1, end=' ')