import requests

link = 'https://plato.stanford.edu/contents.html'

outFile = 'SEP_URLs.txt'

file = requests.get(link)
text = file.text

#print(text)

#print(isinstance(text, str))
#print(len(text))

print(text.count('<li> <a href="'))


#ok, so to make this happen, you're going to need to make something that looks
#through snippets of this string to find the bit of code that precedes the
#links you're looking for, then once it finds it pulls out the bit of URL
#from behind it, adds the rest, and saves it to a CSV or something


#maybe the process is: (1) get indexs of each of these occurances, (2) go back
#and check for the right URL at each of them, (3) output what you find

l =[]
with open(outFile, "w") as f:
    for i in range(0, len(text)):
        if text[i:i+14] == '<li> <a href="':
            #taking slices ahead of this bad boy
            j = i + 14
            path = 'https://plato.stanford.edu/'
            while text[j] != '"':
                path += text[j]
                j +=1
            l.append(path)
            #write the stuff
            f.write(path)
            f.write("\n")


#print(l)
print(len(l))

#hey that works! So then use something like that
