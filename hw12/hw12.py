# with open (r'C:\Users\phuon\HDT-CSB12\hw12\text.txt')as file1:
#     print('List of name: ',file1.read())

# a= input('input file path: ')
# with open(a)as f1:
#     print('file content: ', f1.read())

with open (r'C:\Users\phuon\HDT-CSB12\hw12\userinput.txt','w')as file1:
    user_input = input("input file content:\n")
    while user_input != "":
        file1.write(user_input + "\n")
        user_input = input()
print("== Input file content below ==")
with open (r'C:\Users\phuon\HDT-CSB12\hw12\userinput.txt','r')as file2:
    print(file2.read())

print("== Input recorded in", file2, "==")