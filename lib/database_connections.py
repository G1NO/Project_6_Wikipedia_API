# Created by Chris Peterson 1/26/2017, revised 2/1/2017

import psycopg2
import yaml

def connect_to_postgres (location = 'remote'):
    """ Open a psycopg2 connection and create a cursor based on a yaml credential file.
        The current expected name of the yaml file is "Database_credentials"; please customize this to your taste.
        The credentials file will look for a entry in the dictionary called 'remote' by default.  If the remote
        databse is unavailalbe, it will attempt to connect with the settings the 'local' key.  
        Please remember to close the cursor and connection when you are done using them.        
    """
#TO DO: make  'location' to a list and iterate through the list, rather than default to local db.
#TO DO: add credential file support as a param for the function call.


    with open('Database_credentials', 'r') as f:
        credentials =  yaml.load(f) 
    
    try:
        connection = psycopg2.connect(**credentials[location])
        print "Connected to server {}.".format(credentials[location]['host'])
        return connection, connection.cursor()
    except:
        print 'FAILED to connect to server {}.  Trying local server.'.format(credentials[location]['host'])
        try:
            connection = psycopg2.connect(**credentials['local'])
            print "Conencted to localhost."
            return connection, connection.cursor()
        except:
            print "No Database is available"
            pass 