class university_config:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def set_config(self, university_name, academic_year, semester):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester

    def display_config(self):
        print("university_name:", self.university_name)
        print("academic_year:", self.academic_year)
        print("semester:", self.semester)


# create three objects
config_1 = university_config()
config_2 = university_config()
config_3 = university_config()


# set configuration using config_1
config_1.set_config(
    "yoobee_college",
    "2026",
    "semester_2"
)


# display configuration using config_2
config_2.display_config()


# check if all objects are the same
print("config_1 is config_2:", config_1 is config_2)
print("config_2 is config_3:", config_2 is config_3)
print("config_1 is config_3:", config_1 is config_3)