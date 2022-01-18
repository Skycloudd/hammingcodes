import random


def flip_random(filecontents):
    bytes_filecontents = bytearray(filecontents)

    byteindex = random.randint(0, len(bytes_filecontents) - 1)
    bitindex = random.randint(0, 7)

    bytes_filecontents[byteindex] ^= 1 << bitindex

    return bytes(bytes_filecontents)


def main():
    filename = "test"

    with open(filename, "rb") as f:
        filecontents = f.read()

    filecontents = flip_random(filecontents)

    print(filecontents)

    with open(filename, "wb") as f:
        f.write(filecontents)


if __name__ == "__main__":
    main()
