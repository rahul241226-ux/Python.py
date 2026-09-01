file = open('youtube.txt', 'w')



try:
    file.write('rahul and code')
finally:
    file.close()


with open('youtube.txt', 'w') as file:
    file.write('rahul aur python')