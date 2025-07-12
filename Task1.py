try:
    r1=open('sample.txt','r')
    print_file=r1.read()
    print(print_file)
    r1.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

