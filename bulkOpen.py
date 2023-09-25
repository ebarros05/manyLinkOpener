import webbrowser

count = 0
for line in open('searches.txt'):
    print("searching for: ", line)
    line.replace(' ', '%')
    link = f'https://www.google.com/search?q={line}'
    print(f"link is: %s", link)
    webbrowser.open(link)
    count += 1
print(f"opened %d tabs successfully",count)