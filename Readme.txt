explaination of the assigment

stage-1
1) First all the needed tables are created in the datebase by tablecreation.py file
2) Then IN.csv data is imported to table apitest by the file importingcsv.py
3) run api.py that contains all the api's that was asked to built
4) Next post to "/post_location" can be hit by passing require json data and can be tested through testing/stage1gettest.py by the command "nosetests --verbosity=2 stage1gettest.py"

Stage-2
1) Next get to "/get_using_postgres" can be hit by passing require latitude and longitude as json and can be test by stage2gettest.py by the command "nosetests --verbosity=2 stage2gettest.py"
2) Next get to "/get_using_self" can be hit by passing require latitude and longitude as json and can be test by stage2gettest.py by the command "nosetests --verbosity=2 stage2gettest.py"

stage-3
1) Next get to "/get_location" can be hit by passing require latitude and longitude as json to get wheather point lies in a region or not stored in database and can be test by stage2gettest.py by the command "nosetests --verbosity=2 stage3gettest.py"
