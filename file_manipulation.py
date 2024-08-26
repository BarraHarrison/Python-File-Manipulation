import os

print(os.listdir())

# creating a new file
with open( 'some_file.txt', 'w') as file:
    data = "test file"
    file.write(data)
    print(data)
    print(type(data))


# Prints directory (Python folders) in the terminal
for entry in os.listdir():
    if os.path.isdir(entry):
        print(type(entry))
        print(entry)

try:
    os.mkdir('example folder')
except Exception as e:
    print("The rest of my code")



