# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    print('''
To use this program simply enter an integer between
1 and 200. The program will show the factors of your
chosen integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx'.
    ''')


# Main routine goes here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

print("program continues")
