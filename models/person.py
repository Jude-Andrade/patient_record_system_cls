from datetime import datetime, date

class Person:
    def __init__(self, name=None, birthdate=None, sex=None, phone_number=None, address=None):
        if name:
            self.set_name(name)
        if birthdate:
            self.set_birthdate(birthdate)
        if sex:
            self.set_sex(sex)
        if phone_number:
            self.set_phone_number(phone_number)
        if address:
            self.set_address(address)

    def get_name(self):
        return self.__name

    def get_birthdate(self):
        return self.__birthdate

    def get_sex(self):
        return self.__sex

    def get_phone_number(self):
        return self.__phone_number

    def get_address(self):
        return self.__address

    def set_name(self, name):
        name_validation = [
            all(char == "." or char.isalpha() or char.isspace() for char in name),
            len(name) >= 2 and len(name) <= 50,
        ]

        if not all(name_validation):
            raise ValueError("Input should be letters, minimum of 2 and maximum of 50 characters!")

        self.__name = name.title()

    def set_birthdate(self, birthdate):
        cleaned_input = birthdate.replace("/", "-")

        try:
            valid_birthdate = datetime.strptime(cleaned_input, "%m-%d-%Y")
        except ValueError:
            raise ValueError("Invalid date format, should be in digit MM/DD/YYYY!")

        if valid_birthdate.date() > date.today():
            raise ValueError("Invalid date, should not be in the future!")

        self.__birthdate = valid_birthdate.strftime("%m-%d-%Y")

    def set_sex(self, sex):
        if sex not in ["male", "female"]:
            raise ValueError("sex should be male or female!")

        self.__sex = sex.title()

    def set_phone_number(self, phone_number):
        phone_number_validation = [
            phone_number.isdigit(),
            len(phone_number) == 11,
            phone_number.startswith("09")
        ]

        if not all(phone_number_validation):
            raise ValueError("Phone number should be 11 digits and starts with (09)!")

        self.__phone_number = phone_number

    def set_address(self, address):
        address_validation = [
            all(char == "," or char.isalpha() or char.isdigit() or char.isspace() for char in address),
            len(address) > 8
        ]

        if not all(address_validation):
            raise ValueError("Invalid address, must exceed 8 letters and no symbols!")

        self.__address = address.title()