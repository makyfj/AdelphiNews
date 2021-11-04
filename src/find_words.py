words = "I was going to the museum two days ago!"

word = "I was going to"

new_word = ""

for i in range(len(word)):
    # print(i)
    if i <= 10:
        new_word += word[i]


if new_word in words:
     print(new_word)
     print(words)
