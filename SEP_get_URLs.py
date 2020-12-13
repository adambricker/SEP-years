#This is what I wrote to get all the SEP URLs and write them into a .txt file.
#It's rough because it worked right away, and I didn't need it after that.

import requests

link = 'https://plato.stanford.edu/contents.html'

outFile = 'SEP_URLs.txt'

file = requests.get(link)
text = file.text

#print(text)

#print(isinstance(text, str))
#print(len(text))

print(text.count('<li> <a href="'))




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
