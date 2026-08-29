import json
import database.db_connection as db_connection

class PatientRepository:
    def __init__(self):
        self.connection = db_connection.get_connection()

    def add_record(self, valid_name, valid_birthdate, valid_sex, valid_phone_number, valid_address, valid_blood_type, valid_medical_history):
        with self.connection as connection:
            medical_history_json = json.dumps(valid_medical_history)
            cursor = connection.execute("""
                INSERT INTO patients (name, birthdate, sex, phone_number, address, blood_type, medical_history)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (valid_name, valid_birthdate, valid_sex, valid_phone_number, valid_address, valid_blood_type, medical_history_json))
            return cursor.rowcount == 1

    def view_by_name(self, valid_name):
        with self.connection as connection:
            search_pattern = f"%{valid_name}%"
            return connection.execute("""
                SELECT id, name, birthdate, sex, phone_number, address, blood_type, medical_history
                FROM patients
                WHERE name LIKE ?
            """, (search_pattern,)).fetchall()

    def view_all(self):
        with self.connection as connection:
            return connection.execute("""
                SELECT id, name, birthdate, sex, phone_number, address, blood_type, medical_history
                FROM patients
            """).fetchall()

    def check_id(self, id):
        with self.connection as connection:
            exists = connection.execute("SELECT 1 FROM patients WHERE id = ?", (id,)).fetchone()
            return exists is not None

    def update_by_id_phone_number(self, id, new_phone_number):
        with self.connection as connection:
            prior_phone_number = connection.execute("SELECT phone_number FROM patients WHERE id = ?", (id,)).fetchone()
            current_phone_number = prior_phone_number["phone_number"]

            if current_phone_number == new_phone_number:
                return "repeated"

            connection.execute("""
                UPDATE patients
                SET phone_number = ?
                WHERE id = ?
            """, (new_phone_number, id))

            subsequent_phone_number = connection.execute("SELECT phone_number FROM patients WHERE id = ?", (id,)).fetchone()
            after_phone_number_update = subsequent_phone_number["phone_number"]

            if after_phone_number_update == current_phone_number:
                return False

            return True

    def update_by_id_address(self, id, new_address):
        with self.connection as connection:
            prior_address = connection.execute("SELECT address FROM patients WHERE id = ?", (id,)).fetchone()
            current_address = prior_address["address"]

            if current_address == new_address:
                return "repeated"

            connection.execute("""
                UPDATE patients
                SET address = ?
                WHERE id = ?
            """, (new_address, id))

            subsequent_address = connection.execute("SELECT address FROM patients WHERE id = ?", (id,)).fetchone()
            after_address_update = subsequent_address["address"]

            if after_address_update == current_address:
                return False

            return True

    def update_by_id_all(self, id, new_name, new_birthdate, new_sex, new_phone_number, new_address, new_blood_type, new_medical_history):
        with self.connection as connection:
            new_medical_history_json = json.dumps(new_medical_history)

            prior_data = connection.execute("""
                SELECT name, birthdate, sex, phone_number, address, blood_type, medical_history
                FROM patients
                WHERE id = ?
            """, (id,)).fetchone()

            current_name = prior_data["name"]
            current_birthdate = prior_data["birthdate"]
            current_sex = prior_data["sex"]
            current_phone_number = prior_data["phone_number"]
            current_address = prior_data["address"]
            current_blood_type = prior_data["blood_type"]
            current_medical_history = prior_data["medical_history"]

            if (current_name == new_name and
                current_birthdate == new_birthdate and
                current_sex == new_sex and
                current_phone_number == new_phone_number and
                current_address == new_address and
                current_blood_type == new_blood_type and
                current_medical_history == new_medical_history_json):
                return "repeated"

            connection.execute("""
                UPDATE patients
                SET name = ?,
                    birthdate = ?,
                    sex = ?,
                    phone_number = ?,
                    address = ?,
                    blood_type = ?,
                    medical_history = ?
                WHERE id = ?
            """, (new_name, new_birthdate, new_sex, new_phone_number, new_address, new_blood_type, new_medical_history_json, id))

            subsequent_data = connection.execute("""
                SELECT name, birthdate, sex, phone_number, address, blood_type, medical_history
                FROM patients
                WHERE id = ?
            """, (id,)).fetchone()

            after_name_update = subsequent_data["name"]
            after_birthdate_update = subsequent_data["birthdate"]
            after_sex_update = subsequent_data["sex"]
            after_phone_number_update = subsequent_data["phone_number"]
            after_address_update = subsequent_data["address"]
            after_blood_type_update = subsequent_data["blood_type"]
            after_medical_history_update = subsequent_data["medical_history"]

            if (after_name_update == current_name and
                after_birthdate_update == current_birthdate and
                after_sex_update == current_sex and
                after_phone_number_update == current_phone_number and
                after_address_update == current_address and
                after_blood_type_update == current_blood_type and
                after_medical_history_update == current_medical_history):
                return False

            return True

    def delete_by_id(self, id):
        with self.connection as connection:
            exists = connection.execute("SELECT 1 FROM patients WHERE id = ?", (id,)).fetchone()
            if not exists:
                return False

            connection.execute("DELETE FROM patients WHERE id = ?", (id,))
            return True