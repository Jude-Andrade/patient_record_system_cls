import json
import database.db_connection as db_connection
from database.repository import PatientRepository
from models.patient import Patient

class PatientController:
    def __init__(self):
        self.connection = db_connection.get_connection()
        self.patient_repository = PatientRepository()
        self.patient = Patient()

    def run(self):
        while True:
            print("\n========== Patient Record System ==========\n")
            print("[1]. Patients")
            print("[0]. Exit.")

            choice_main = input("Enter Selection: ").strip()

            valid_choice_main = ["1", "0"]

            if choice_main not in valid_choice_main:
                print("Enter a Valid Selection!")
                continue

            if choice_main == "1":
                self.patient_menu()
            else:
                is_true = self.exit_opt()
                if not is_true:
                    continue
                print("Exitting app...")
                break

    def exit_opt(self):
        while True:
            print("Are your sure you want to exit?")
            print("[y]. Yes     [n]. No")

            choice_exit = input("Enter Selection: ").strip().lower()

            valid_choice_exit = ["y", "n"]

            if choice_exit not in valid_choice_exit:
                print("Enter a Valid Selection!")
                continue

            return True if choice_exit == "y" else False

    def back_opt(self):
        while True:
            print("Are your sure you want to go back?")
            print("[y]. Yes     [n]. No")

            choice_back = input("Enter Selection: ").strip().lower()

            valid_choice_back = ["y", "n"]

            if choice_back not in valid_choice_back:
                print("Enter a Valid Selection!")
                continue

            return True if choice_back == "y" else False

    def patient_menu(self):
        while True:
            print("\n========== Patient Record System ==========\n")
            print("[1]. Register Patient.")
            print("[2]. View Patient Record.")
            print("[3]. Update Patient Record.")
            print("[4]. Delete Patient Record.")
            print("[0]. Back.")

            choice_patient_menu = input("Enter Selection: ").strip()

            valid_choice_patient_menu = ["1", "2", "3", "4", "0"]

            if choice_patient_menu not in valid_choice_patient_menu:
                print("Enter a Valid Selection!")
                continue

            if choice_patient_menu == "1":
                self.register_patient()
            elif choice_patient_menu == "2":
                self.view_patient_menu()
            elif choice_patient_menu == "3":
                self.update_patient_menu()
            elif choice_patient_menu == "4":
                self.delete_patient_by_id()
            else:
                is_true = self.back_opt()
                if not is_true:
                    continue
                break

    def register_patient(self):
        name_flag = False
        birthdate_flag = False
        sex_flag = False
        phone_number_flag = False
        address_flag = False
        blood_type_flag = False
        medical_history_flag = False

        while not all([name_flag, birthdate_flag, sex_flag, phone_number_flag, address_flag, blood_type_flag, medical_history_flag]):
            if not name_flag:
                name = input("Enter Name: ").strip()
                try:
                    self.patient.set_name(name)
                    name_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not birthdate_flag:
                birthdate = input("Enter Birthday (MM/DD/YYYY): ").strip()
                try:
                    self.patient.set_birthdate(birthdate)
                    birthdate_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not sex_flag:
                sex = input("Enter Sex (male or female): ").strip().lower()
                try:
                    self.patient.set_sex(sex)
                    sex_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not phone_number_flag:
                phone_number = input("Enter Phone Number: ").strip()
                try:
                    self.patient.set_phone_number(phone_number)
                    phone_number_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not address_flag:
                address = input("Enter Address: ").strip().lower()
                try:
                    self.patient.set_address(address)
                    address_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not blood_type_flag:
                blood_type = input("Enter Blood Type: ").strip().upper()
                try:
                    self.patient.set_blood_type(blood_type)
                    blood_type_flag = True
                except ValueError as error:
                    print(f"Error: {error}")
                    continue

            if not medical_history_flag:
                medical_history = {
                    "allergy": [],
                    "asthma": [],
                    "diabetes": [],
                    "heart_disease": [],
                    "hypertension": [],
                    "surgery": [],
                    "other": []
                }

                while True:
                    print("\nMedical Condition:\n")
                    print("[1]. Allergy")
                    print("[2]. Asthma")
                    print("[3]. Diabetes")
                    print("[4]. Heart Disease")
                    print("[5]. Hypertension")
                    print("[6]. Surgery")
                    print("[7]. Other")
                    print("[0]. Done")

                    medical_condition_validation = ["1", "2", "3", "4", "5", "6", "7", "0"]

                    choice_medical_condition = input("Enter Selection: ").strip()

                    if choice_medical_condition not in medical_condition_validation:
                        print("Invalid option. Please try again.")
                        continue

                    if choice_medical_condition == "0":
                        break
                    elif choice_medical_condition == "1":
                        choice_1 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["allergy"].append(choice_1)
                    elif choice_medical_condition == "2":
                        choice_2 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["asthma"].append(choice_2)
                    elif choice_medical_condition == "3":
                        choice_3 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["diabetes"].append(choice_3)
                    elif choice_medical_condition == "4":
                        choice_4 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["heart_disease"].append(choice_4)
                    elif choice_medical_condition == "5":
                        choice_5 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["hypertension"].append(choice_5)
                    elif choice_medical_condition == "6":
                        choice_6 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["surgery"].append(choice_6)
                    elif choice_medical_condition == "7":
                        choice_7 = input("Enter medical condition statement: ").strip().lower()
                        medical_history["other"].append(choice_7)

                self.patient.set_medical_history(medical_history)
                medical_history_flag = True

        valid_name = self.patient.get_name()
        valid_birthdate = self.patient.get_birthdate()
        valid_sex = self.patient.get_sex()
        valid_phone_number = self.patient.get_phone_number()
        valid_address = self.patient.get_address()
        valid_blood_type = self.patient.get_blood_type()
        valid_medical_history = self.patient.get_medical_history()

        is_registered = self.patient_repository.add_record(
            valid_name, valid_birthdate, valid_sex, valid_phone_number,
            valid_address, valid_blood_type, valid_medical_history
        )

        if not is_registered:
            print("Status: Registration failed!")
            return

        print("Status: Registration Successfull!")
        return

    def view_patient_menu(self):
        while True:
            print("\n========== Patient Record System ==========\n")
            print("[1]. View Patient Record by Name.")
            print("[2]. View All Patient Records.")
            print("[0]. Back.")

            choice_view_patient_menu = input("Enter Selection: ").strip()

            valid_view_patient_menu = ["1", "2", "0"]

            if choice_view_patient_menu not in valid_view_patient_menu:
                print("Enter a valid selection!")
                continue

            if choice_view_patient_menu == "1":
                self.view_patient_by_name()
            elif choice_view_patient_menu == "2":
                self.view_all_patient()
            else:
                is_true = self.back_opt()
                if not is_true:
                    continue
                break

    def view_patient_by_name(self):
        name_flag = False
        while not name_flag:
            name = input("Enter Name to View: ").strip()
            try:
                self.patient.set_name(name)
                name_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        valid_name = self.patient.get_name()
        data = self.patient_repository.view_by_name(valid_name)

        if not data:
            print("Name Entered does not Exists!")
            return
        else:
            print(f"Patient Records with name conaining '{valid_name}'")
            for datum in data:
                print(f"ID: {datum['id']}")
                print(f"Full Name: {datum['name']}")
                print(f"Sex: {datum['sex']}")
                print(f"Phone Number: {datum['phone_number']}")
                print(f"Address: {datum['address']}")
                print(f"Blood Type: {datum['blood_type']}")
                print(f"Medical History: {json.loads(datum['medical_history'])}")
            return

    def view_all_patient(self):
        data = self.patient_repository.view_all()

        if not data:
            print("No data to show!")
            return
        else:
            print("All Data:")
            for datum in data:
                print(f"ID: {datum['id']}")
                print(f"Full Name: {datum['name']}")
                print(f"Sex: {datum['sex']}")
                print(f"Phone Number: {datum['phone_number']}")
                print(f"Address: {datum['address']}")
                print(f"Blood Type: {datum['blood_type']}")
                print(f"Medical History: {json.loads(datum['medical_history'])}")
            return

    def update_patient_menu(self):
        while True:
            print("\n========== Patient Record System ==========\n")
            print("[1]. Update Phone Number.")
            print("[2]. Update Address.")
            print("[3]. Update All.")
            print("[0]. Back.")

            choice_update_patient_menu = input("Enter Selection: ").strip()

            valid_update_patient_menu = ["1", "2", "3", "0"]

            if choice_update_patient_menu not in valid_update_patient_menu:
                print("Enter a valid selection!")
                continue

            if choice_update_patient_menu == "1":
                self.update_patient_phone_number_by_id()
            elif choice_update_patient_menu == "2":
                self.update_patient_address_by_id()
            elif choice_update_patient_menu == "3":
                self.update_patient_all_by_id()
            else:
                is_true = self.back_opt()
                if not is_true:
                    continue
                break

    def update_patient_phone_number_by_id(self):
        id_flag = False
        phone_number_flag = False

        while not id_flag:
            try:
                id = int(input("Enter ID: "))
                is_id_exist = self.patient_repository.check_id(id)
                if not is_id_exist:
                    print("ID does not exist, update Failed!")
                    continue
                id_flag = True
            except ValueError:
                print("Error: ID should be a digit!")
                continue

        while not phone_number_flag:
            new_phone_number = input("Enter New Phone Number: ").strip()
            try:
                self.patient.set_phone_number(new_phone_number)
                phone_number_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        valid_phone_number = self.patient.get_phone_number()
        is_phone_number_changed = self.patient_repository.update_by_id_phone_number(id, valid_phone_number)

        if is_phone_number_changed == "repeated":
            print("New Phone Number Inputted is the Current!")
            return
        elif not is_phone_number_changed:
            print("Phone Number Updated Unsuccessfully!")
            return
        else:
            print("Phone Number Updated Successfully")
            return

    def update_patient_address_by_id(self):
        id_flag = False
        address_flag = False

        while not id_flag:
            try:
                id = int(input("Enter ID: "))
                is_id_exist = self.patient_repository.check_id(id)
                if not is_id_exist:
                    print("ID does not exist, update Failed!")
                    continue
                id_flag = True
            except ValueError:
                print("Error: ID should be a digit!")
                continue

        while not address_flag:
            new_address = input("Enter New Address: ").strip()
            try:
                self.patient.set_address(new_address)
                address_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        valid_address = self.patient.get_address()
        is_address_changed = self.patient_repository.update_by_id_address(id, valid_address)

        if is_address_changed == "repeated":
            print("New Address Inputted is the Current!")
            return
        elif not is_address_changed:
            print("Address Updated Unsuccessfully!")
            return
        else:
            print("Address Updated Successfully")
            return

    def update_patient_all_by_id(self):
        id_flag = False
        name_flag = False
        birthdate_flag = False
        sex_flag = False
        phone_number_flag = False
        address_flag = False
        blood_type_flag = False
        medical_history_flag = False

        while not id_flag:
            try:
                id = int(input("Enter ID: "))
                is_id_exist = self.patient_repository.check_id(id)
                if not is_id_exist:
                    print("ID does not exist, update Failed!")
                    continue
                id_flag = True
            except ValueError:
                print("Error: ID should be a digit!")
                continue

        while not name_flag:
            new_name = input("Enter New Name: ").strip()
            try:
                self.patient.set_name(new_name)
                name_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not birthdate_flag:
            new_birthdate = input("Enter New Birthday (MM/DD/YYYY): ").strip()
            try:
                self.patient.set_birthdate(new_birthdate)
                birthdate_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not sex_flag:
            new_sex = input("Enter New Sex (male or female): ").strip().lower()
            try:
                self.patient.set_sex(new_sex)
                sex_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not phone_number_flag:
            new_phone_number = input("Enter New Phone Number: ").strip()
            try:
                self.patient.set_phone_number(new_phone_number)
                phone_number_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not address_flag:
            new_address = input("Enter New Address: ").strip()
            try:
                self.patient.set_address(new_address)
                address_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not blood_type_flag:
            new_blood_type = input("Enter New Blood Type: ").strip().upper()
            try:
                self.patient.set_blood_type(new_blood_type)
                blood_type_flag = True
            except ValueError as error:
                print(f"Error: {error}")

        while not medical_history_flag:
            new_medical_history = {
                "allergy": [],
                "asthma": [],
                "diabetes": [],
                "heart_disease": [],
                "hypertension": [],
                "surgery": [],
                "other": []
            }

            while True:
                print("\nMedical Condition:\n")
                print("[1]. Allergy")
                print("[2]. Asthma")
                print("[3]. Diabetes")
                print("[4]. Heart Disease")
                print("[5]. Hypertension")
                print("[6]. Surgery")
                print("[7]. Other")
                print("[0]. Done")

                medical_condition_validation = ["1", "2", "3", "4", "5", "6", "7", "0"]

                choice_medical_condition = input("Enter Selection: ").strip()

                if choice_medical_condition not in medical_condition_validation:
                    print("Invalid option. Please try again.")
                    continue

                if choice_medical_condition == "0":
                    break
                elif choice_medical_condition == "1":
                    choice_1 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["allergy"].append(choice_1)
                elif choice_medical_condition == "2":
                    choice_2 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["asthma"].append(choice_2)
                elif choice_medical_condition == "3":
                    choice_3 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["diabetes"].append(choice_3)
                elif choice_medical_condition == "4":
                    choice_4 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["heart_disease"].append(choice_4)
                elif choice_medical_condition == "5":
                    choice_5 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["hypertension"].append(choice_5)
                elif choice_medical_condition == "6":
                    choice_6 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["surgery"].append(choice_6)
                elif choice_medical_condition == "7":
                    choice_7 = input("Enter medical condition statement: ").strip().lower()
                    new_medical_history["other"].append(choice_7)

            self.patient.set_medical_history(new_medical_history)
            medical_history_flag = True

        valid_name = self.patient.get_name()
        valid_birthdate = self.patient.get_birthdate()
        valid_sex = self.patient.get_sex()
        valid_phone_number = self.patient.get_phone_number()
        valid_address = self.patient.get_address()
        valid_blood_type = self.patient.get_blood_type()
        valid_medical_history = self.patient.get_medical_history()

        is_all_changed = self.patient_repository.update_by_id_all(
            id, valid_name, valid_birthdate, valid_sex, valid_phone_number,
            valid_address, valid_blood_type, valid_medical_history
        )

        if is_all_changed == "repeated":
            print("New Data Inputted is the Current!")
            return
        elif not is_all_changed:
            print("Patient Record Updated Unsuccessfully!")
            return
        else:
            print("Patient Record Updated Successfully")
            return

    def delete_patient_by_id(self):
        id_flag = False

        while not id_flag:
            try:
                id = int(input("Enter ID: "))
                is_id_exist = self.patient_repository.check_id(id)
                if not is_id_exist:
                    print("ID does not exist, delete Failed!")
                    continue
                id_flag = True
            except ValueError:
                print("Error: ID should be a digit!")
                continue

        is_deleted = self.patient_repository.delete_by_id(id)

        if not is_deleted:
            print("Patient Record Deleted Unsuccessfully!")
            return
        else:
            print("Patient Record Deleted Successfully")
            return

if __name__ == "__main__":
    controller = PatientController()
    controller.run()