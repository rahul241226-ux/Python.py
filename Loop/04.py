#Problem: Reverse a string using a loop.


input_string="rahul"
reverse_strinng=""


for rev in input_string:
    print(rev)
    #reverse_strinng = reverse_strinng+ rev
    reverse_strinng = rev + reverse_strinng

print(reverse_strinng)