# uploading data to database table
import json
import psycopg2
with open('data.json') as f:
    js = json.load(f)
conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")	
cur = conn.cursor()
for data in js['features']:
    parent=data['properties']['parent']
    name = data['properties']['name']
    tpe = data['properties']['type']
    print(data['geometry']['coordinates'][0])    
    for coordinatee in data['geometry']['coordinates'][0]:    
        lng = coordinatee[0]
        lat = coordinatee[1]
       
        cur.execute("INSERT INTO boundary (name,type,parent,latitude,longitutde) VALUES ('"+name+"','"+tpe+"','"+parent+"',"+str(lat)+","+str(lng)+");")
	
           		
    print("entris done")	
conn.commit()
