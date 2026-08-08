class sort:
    def __init__(self):
        self.name = ["alex", "young", "kane", "fred", "Mary"]
        self.student_ids = [2, 1, 5, 4, 3]
        self.age = [28, 32, 31, 20, 24]
        self.used_letters = set()

    def sorting_studentids(self):
        size = len(self.student_ids)

        for i in range(size):
            for j in range(0, size - i - 1):
                if self.student_ids[j] > self.student_ids[j + 1]:

                    # Swap student IDs
                    self.student_ids[j], self.student_ids[j + 1] = (
                        self.student_ids[j + 1],
                        self.student_ids[j]
                    )

                    # Swap names
                    self.name[j], self.name[j + 1] = (
                        self.name[j + 1],
                        self.name[j]
                    )

                    # Swap ages
                    self.age[j], self.age[j + 1] = (
                        self.age[j + 1],
                        self.age[j]
                    )

    def sorted_student_ids(self):
        print("Sorted Student Records")
        print("----------------------")
        print("Id  Name   Age")

        for i in range(len(self.student_ids)):
            print(self.student_ids[i], self.name[i], self.age[i])


if __name__ == "__main__":
    s = sort()
    s.sorting_studentids()
    s.sorted_student_ids()