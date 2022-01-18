def main(filename):
    with open(filename, "rb") as f:
        contents = bytearray(f.read())

    chunks = []

    chunk_size = 16

    for i in range(0, int(round(len(contents) / chunk_size))):
        chunks.append(contents[:chunk_size])
        del contents[:chunk_size]

    print(chunks)


if __name__ == "__main__":
    filename = "test"

    main(filename)
