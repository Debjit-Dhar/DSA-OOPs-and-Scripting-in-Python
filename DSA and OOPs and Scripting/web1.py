import webbrowser
s=input('Enter topic')
s=s.replace(' ','_')
print(s)
webbrowser.open('https://en.wikipedia.org/wiki/'+s)
