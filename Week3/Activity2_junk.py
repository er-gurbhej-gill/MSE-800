class FileProcessor:

    def process_file(self):
        data = open("junk.txt", "r")
        lines = data.readlines()

        print("Total lines:", len(lines))

        data.close()

        data = open("junk.txt", "w")

        for line in lines:
            data.write(line.lower())

        data.write("text file nanalyssis\n")

        data.close()


def main():
    file = FileProcessor()
    file.process_file()


if __name__ == "__main__":
    main()