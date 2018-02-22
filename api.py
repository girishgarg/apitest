import json
import flask
import httplib2
from flask import Flask, render_template, request, jsonify, make_response
import psycopg2
from shapely.geometry import shape, Point
app = Flask(__name__)


# REST API: POST Request

#stage 1
@app.route('/post_location', methods=['GET','POST'])
def related():
    try: 
        pincode = request.json['pincode']	
        lat = request.json['latitude']	
        lng = request.json['longitude']
        address = request.json['address']
        city = request.json['city']
        conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")
        cur = conn.cursor() 
        #this query is to check is there any entry that contain same pincode that we are adding or is there points that have less than 1 km distance because that they are and then data is not inserted in it
        cur.execute("SELECT apitest.key, apitest.latitude, apitest.longitude, earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) as distance FROM apitest WHERE key='IN/"+pincode+"' OR earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) <1000;")
        fet = cur.fetchone()
        result = ""
        pin = 'IN/'+pincode
        if cur.rowcount>0:	
            result = "entry exist"
            print("entry alerady exist or latitude and long nearly equal to some intial data")
        else:
            cur.execute("INSERT INTO apitest (key, place_name, admin_name1, latitude, longitude, accuracy) VALUES ('"+pin+"','"+address+"','"+city+"',"+lat+","+lng+",'')");
            result = "entry added"
        # for just testing entry is added or not
        cur.execute("SELECT key, latitude, longitude,place_name, admin_name1 FROM apitest WHERE key='IN/110009';")
        fett = cur.fetchone()
        print(fett)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'task': result}),201
    except Exception as e:
        print(e)
        return jsonify({'error':'error'})


#stage 2
#this api gives Pincode lie in 5km around the given point including itself
@app.route('/get_using_postgres', methods=['GET','POST'])
def related1():
    try:
       lat = request.json['latitude']
       lng = request.json['longitude']
       result = []
       conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")	
       cur = conn.cursor() 
       cur.execute("SELECT apitest.key FROM apitest WHERE earth_box(ll_to_earth("+lat+","+lng+"),5000) @> ll_to_earth(apitest.latitude, apitest.longitude);")
       res = cur.fetchall()
       print(cur.rowcount)
       for row in res:
           print(row)
           result.append(row[0]) 

       return jsonify({'task': result}),201
    

    except Exception as e:
        print(e)
        return jsonify({'error':'error'})	


#this api gives Pincode lie in 5km around the given point excluding itself
@app.route('/get_using_self', methods=['GET','POST'])
def related2():
    try:
       lat = request.json['latitude']
       lng = request.json['longitude']
       result = []
       conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432")	
       cur = conn.cursor()
       
       cur.execute("SELECT apitest.key, earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) as distance FROM apitest WHERE earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(apitest.latitude, apitest.longitude)) <=5000;") 
       print(cur.rowcount)
       res = cur.fetchall()
       for row in res:
           print(row)
           result.append(row[0]) 

       return jsonify({'task': result}),201
    

    except Exception as e:
        print(e)
        return jsonify({'error':'error'})	

# the difference bettween both is using earth_box it output the points including itself and incase of urself api it exclude this point.


#stage 3
#in this first data is added to the table boundary by running uploadingdata.py and here i use shapely.geometry to get shape anf check point inside this shape   
@app.route('/get_location', methods=['GET','POST'])
def related3():
    try:
        lat = request.json['latitude']
        lng = request.json['longitude']
        conn = psycopg2.connect(dbname="postgres", user = "postgres", password = "pass", host = "127.0.0.1", port = "5432") 
        result = ""	
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT name,type,parent FROM boundary;")
        fetch = cur.fetchall()
        for row in fetch:
            geo = {}
            codi = []
            codionemore = []
            cur.execute("SELECT latitude, longitutde FROM boundary WHERE name = '"+row[0]+"';")
            fet = cur.fetchall()
            for x in fet:
                point = []
                point.append(float(x[0]))
                point.append(float(x[1]))
                codi.append(point)
            geo['type'] = 'Polygon'
            codionemore.append(codi) 
            geo['coordinates'] = codionemore
            polygon = shape(geo)
            point = Point(lat, lng)
            if polygon.contains(point):
               result = "point lie in "+row[0]
               print("point lie in "+row[0])
               break;
            else:
               result = "point doesnot lie in given data"
               print("point doesnot lie in given data")
        
        return jsonify({'task': result}),201
    

    except Exception as e:
        print(e)
        return jsonify({'error':'error'})
    

if __name__ == '__main__':

    app.run(debug=True,port=5000)


