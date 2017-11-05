import string
low = list(string.ascii_lowercase)
high = list(string.ascii_uppercase)

with open("test.txt", "r") as para:  
    
    words_dict = {}
    content = para.read()
    num = 0
    avg_sent = 0
    letters = 0
    line = "--------------------------"

    words = content.split(" ")
    sentences = content.split(". ")
    word_count = len(words)
    sentence_count = len(sentences)


    for lines in sentences:
        #print(lines + '\n')
        words_dict[num] = len(lines.split(" "))
        num = num + 1

    for k,v in words_dict.items():
        avg_sent = avg_sent + int(v)

    avg_words = float(avg_sent/len(words_dict))
 
    new = list(content)

    for all in new:
        if all in low or all in high:
            letters = letters + 1
    avg_letters = letters/word_count

print(
    line + "\n" + "Paragraph Analysis" + "\n" + line + "\n" +
    "Approximate Word Count: " + str(word_count) + "\n" +
    "Approximate Sentence Count: " + str(sentence_count) + "\n" +
    "Average Letter Count: " + str(avg_letters) + "\n" +
    "Average Sentence Length: " + str(avg_words))

