documents = input()
search_words =  input()

rslt = documents.replace(search_words, '')

len(documents) - len(rslt)
answer = (len(documents) - len(rslt)) // len(search_words)
print(answer)