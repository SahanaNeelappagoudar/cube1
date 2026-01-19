import sys

def cube(num):
    return num ** 3

def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = int(input("Enter a number: "))
    print("Cube:", cube(num))

if __name__ == "__main__":
    main()