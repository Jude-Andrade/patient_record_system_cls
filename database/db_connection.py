import sqlite3 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "clinic.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def initialize_database():
    create_tables_script = """
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        birthdate TEXT NOT NULL, --MM-DD-YYYY
        sex TEXT NOT NULL, --Female OR Male
        phone_number TEXT NOT NULL,
        address TEXT NOT NULL,
        blood_type TEXT NOT NULL,
        medical_history TEXT NOT NULL,
        submitted_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    
    CREATE TRIGGER IF NOT EXISTS update_patients_timestamp
    AFTER UPDATE ON patients
    FOR EACH ROW
    BEGIN
        UPDATE patients 
        SET updated_at = CURRENT_TIMESTAMP 
        WHERE id = OLD.id;
    END;
        """

    with get_connection() as connection:
        connection.executescript(create_tables_script)
        
        
if __name__ == "__main__":
    # This only runs if you execute database.py directly
    print("Testing the database setup...")
    initialize_database()