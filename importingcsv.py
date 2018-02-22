import psycopg2
import csv

csv_data = csv.reader(open('IN.csv'))
conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
cur.execute("COPY apitest FROM '/home/girish/machine_learning_internship_project/IN.csv' WITH DELIMITER ',' CSV;")
print ("CSV data imported")
conn.commit()
cur.close()
