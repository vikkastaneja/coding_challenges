import sys

def word_count_switch(args):
    def option_c():
        filename = sys.argv[2]
        size = 0
        with open(filename, "rb") as f:
            f.seek(0, 2)
            size = f.tell()

        print(f"{size} {filename}")
        return size

    def option_w():
        filename = sys.argv[2]
        size = 0
        with open(filename, "r") as f:
            size = len(f.read().split())

        print(f"{size} {filename}")
        return size

    def option_l():
        filename = sys.argv[2]
        size = 0
        with open(filename, "r") as f:
            size = len(f.readlines())

        print(f"{size} {filename}")
        return size
    
    def default_case():
        print("Invalid option")
        return -1

    switch = {
        "-c": option_c,
        "-w": option_w,
        "-l": option_l
    }

    return switch.get(args[1], default_case)()

def word_count(args):
    if len(sys.argv) != 3:
        print("Usage: python ccwc.py <options> <filename>")
        print("Options:\n\t-c\tCount the number of bytes in the file\n\t-w\tCount the number of words in the file\n\t-l\tCount the number of lines in the file")
        sys.exit(1)

    return word_count_switch(args)

if __name__ == "__main__":
    word_count(sys.argv)
