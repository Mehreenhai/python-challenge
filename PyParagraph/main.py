
with open("passage.txt", "r") as para:  
    

    content = para.read()
    print("START", content, "END")
    words = content.split()
    sentences = content.split(". ")
    print("Approximate word count: ", len(words), " words.")
    print("Approximate sentence count: ", len(sentences), " sentences.")
    
    for lines in sentences:
        print(sentences)
   