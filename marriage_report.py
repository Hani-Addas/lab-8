import os
import sqlite3
import pandas as pd
from create_relationships import db_path, script_dir

def main():
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # SQL query to get all married couples
    married_couples_query = """
    SELECT p1.name, p2.name, r.start_date
    FROM relationships r
    JOIN people p1 ON r.person1_id = p1.id
    JOIN people p2 ON r.person2_id = p2.id
    """

    cur.execute(married_couples_query)
    married_couples = cur.fetchall()

    con.close()

    return married_couples

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for person in name_and_age_list:
        name, age = person
        print(f"{name} is {age} years old.")
        
def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date.

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    df = pd.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Start Date'])
    df.to_csv(csv_path, index=False)
   

if __name__ == '__main__':
   main()
