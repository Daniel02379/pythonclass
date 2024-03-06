# This program reads and displays the contents
# of the philosophers.txt file.
from pathlib import Path

def main():
    Path('python', 'names.txt')
    #infile = open('C:\\python\\names.txt', 'r')
    #infile = open(r'C:\python\names.txt', 'r')
    infile = open('C:/python/names.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(file_contents)

# Call the main function.
if __name__ == '__main__':
    main()
