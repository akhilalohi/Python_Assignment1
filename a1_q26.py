string = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

if string.startswith(prefix):
    print("The string starts with ",prefix)
else:
    print("The string does not start with ",prefix)

if string.endswith(suffix):
    print("The string ends with ",suffix)
else:
    print("The string does not end with ",suffix)
