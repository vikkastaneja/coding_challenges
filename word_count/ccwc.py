import sys

def word_count(file_path):
    if len(sys.argv) != 3:
        print("Usage: python ccwc.py -c <filename>")
        sys.exit(1)

    if sys.argv[1] != "-c":
        print("Usage: python ccwc.py -c <filename>")
        sys.exit(1)

    filename = sys.argv[2]
    size = 0
    with open(filename, "rb") as f:
        f.seek(0, 2)
        size = f.tell()

    print(f"{size} {filename}")
    return size

if __name__ == "__main__":

    word_count(sys.argv)
