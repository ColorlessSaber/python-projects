"""
Python: 3.13.4
Author: Michael Heilman
Project Scope: Create an SQL database that will store the text files found in a given tuple list, and also
                print the qualifying text files to the console.
"""
import sqlite3 as sql

def scan_list_for_txt_files(list_to_scan):
    txt_files_found = [] # a list to hold txt files to insert into a database
    for file in list_to_scan:
        if file.endswith('.txt'):
            txt_files_found.append(file)
    return txt_files_found


def insert_txt_files_into_db(files_to_insert):
    # Create the SQL database if it does not exist, and the table to hold the text files
    with sql.connect('sql_text_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_txt_files(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT)
        """)
        conn.commit()

        # Insert text files into database
        for file in files_to_insert:
            cursor.execute("""
            INSERT INTO tbl_txt_files(file_name)
            VALUES(?)
            """,(file,))
            conn.commit()

def query_txt_files():
    # Query the text files from the database and print them to the console
    with sql.connect('sql_text_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT file_name 
        FROM tbl_txt_files
        """)
        db_file_list = cursor.fetchall()
        for file in db_file_list:
            print("File: {}\n".format(file))

if __name__ == '__main__':
    # The tuple list containing the text files to find mingled among other files.
    file_list = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    txt_files_for_db = scan_list_for_txt_files(file_list)
    insert_txt_files_into_db(txt_files_for_db)
    query_txt_files()