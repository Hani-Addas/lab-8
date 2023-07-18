import os
import sqlite3
from faker import Faker
import random



# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network10.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # Function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query that creates a table named 'relationships'.
    create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships
    (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
    );
    """
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # Function body
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    fake = Faker()
    
    # Generate and execute the INSERT queries to add relationships to the table
    for _ in range(200):
        person1_id = random.randint(1, 200)
        person2_id = random.randint(1, 200)
        while person2_id == person1_id:
            person2_id = random.randint(1, 200)
        relationship_type = fake.random_element(elements=('friend', 'family', 'colleague', 'partner'))
        start_date = fake.date_between(start_date='-50y', end_date='today').strftime('%Y-%m-%d')

        add_relationship_query = """
        INSERT INTO relationships
        (
            person1_id,
            person2_id,
            type,
            start_date
        )
        VALUES (?, ?, ?, ?);
        """

        c.execute(add_relationship_query, (person1_id, person2_id, relationship_type, start_date))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
