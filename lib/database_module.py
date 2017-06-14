<<<<<<< HEAD
#Created 2/1/2017 by Chris Peterson

import psycopg2
from database_connections import connect_to_postgres
=======
#Created 2/1/2017 by Chris Peterson and Suketu Kothari
#modified 2/5/2017
#Version : 1.1 release candidate 1

import psycopg2
import yaml
import re
>>>>>>> fd052599eb038f52abdd23f0da9c12b0d6780617

def insert_category ( category_id,category_name):
	"""
	This function will insert the values passed into the categories table in the wikipedia database.  
	If the category number matches a value in the table, the category title will be updated.
	"""

	connection, cursor = connect_to_postgres()
	update_sql = u"""
   	 	INSERT INTO category
    	(category_id, category_name) VALUES ({}, '{}')
    	on conflict (category_id) do 
    		UPDATE set category_name =excluded.category_name;
    	""".format(category_id, category_name)
	cursor.execute(update_sql)
	connection.commit()
	connection.close()


def insert_page ( page_id, category_id, page_title, page_text):
	"""
	This function will insert the values passed into the page table in the wikipedia database.  
	If the page_id matches a value in the table, the page title and page text will be updated.
	"""

	connection, cursor = connect_to_postgres()
	insert_page = u"""
		INSERT INTO page (page_id, title, page)
		VALUES ({}, '{}', '{}')
		on conflict (page_id) do 
    		UPDATE set title =excluded.title, page = exlcuded.page;
	""".format(page_id, page_text, page_text)
	insert_page_cate = u"""
		INSERT INTO page_cate (page_id, category_id)
<<<<<<< HEAD
		VALUES ({}, {});
	""".format(page_id, category_number)
	
	cursor.execute(insert_page)
	cursor.execute(insert_page_cate)
	connection.commit()

	cursor.close()
	connection.close()
=======
		VALUES ({}, {})
		on conflict do nothing;
    """.format(page_id, category_id)
	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(insert_page)
	    cursor.execute(insert_page_cate)
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return "OK"
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
    	return e.pgerror

def select_pages ( page_ids, location = 'remote'):
	"""
	This function will return pages the have a pagid in the list 'page_ids'.  
	Set the location string to select the database to be used.
	"""
	if len(page_ids) ==1:
		page_ids = page_ids *2
	page_ids = tuple(page_ids)  #converts the list 'page_ids' into a format the SQL likes.
	
	select_pages_sql = u"""
	    SELECT DISTINCT page_id, title, page
	    FROM page
	    WHERE page_id IN {};
	    """.format(page_ids)
	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_pages_sql)
	    returned_pages = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return returned_pages
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
    	return e.pgerror
>>>>>>> fd052599eb038f52abdd23f0da9c12b0d6780617

def insert_page ( page_id, category_id, page_title, page_text):
	"""
	This function will insert the values passed into the page table in the wikipedia database.  
	If the page_id matches a value in the table, the page title and page text will be updated.
	"""

<<<<<<< HEAD
	connection, cursor = connect_to_postgres()
	insert_page = u"""
		INSERT INTO page (page_id, title, page)
		VALUES ({}, '{}', '{}')
		on conflict (page_id) do 
    		UPDATE set title =excluded.title, page = exlcuded.page;
	""".format(page_id, page_text, page_text)
	insert_page_cate = u"""
		INSERT INTO page_cate (page_id, category_id)
		VALUES ({}, {});
	""".format(page_id, category_number)
	
	cursor.execute(insert_page)
	cursor.execute(insert_page_cate)
	connection.commit()
=======
	select_category_sql = u"""
    	SELECT category.category_name, category.category_id 
    	FROM category
    	join page_cate
    	on page_cate.category_id = category.category_id
    	WHERE page_cate.page_id = {};
    	""".format(page_id)

	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_category_sql)
	    returned_cate = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return returned_cate	
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
	    return e.pgerror

def connect_to_postgres (location = 'remote'):
    """ v 1.2 Open a psycopg2 connection and create a cursor based on a yaml credential file.
        The current expected name of the yaml file is "Database_credentials"; please customize this to your taste.
        The credentials file will look for a entry in the dictionary called 'remote' by default.  If the remote
        databse is unavailalbe, it will attempt to connect with the settings the 'local' key.  
        Please remember to close the cursor and connection when you are done using them.        
    """
#TO DO: make  'location' to a list and iterate through the list, rather than default to local db.
#TO DO: add credential file support as a param for the function call.

>>>>>>> fd052599eb038f52abdd23f0da9c12b0d6780617

<<<<<<< HEAD
	cursor.close()
	connection.close()
=======
    with open('config/credentials.yml', 'r') as f:
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
<<<<<<< HEAD
>>>>>>> 0c3977ee492193762cbd644f55eb176ef556d2af
=======

def execute_sql_statement ( sql_select, location = 'remote'):
	"""
	This function will return run an arbitrary SQL select command.
	"""
	if  re.search('^[select]', sql_select.lower()) and not re.search(';(?!$)',sql_select):
	    print "OK"
	else:
	    raise ValueError('The SELECT statment is not valid: {}'.format(sql_select))

	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(sql_select)
	    returned_cate = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return returned_cate	
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
	    return e.pgerror

def select_all_page_vectors ( location = 'remote'):
	"""
	This function will return all page vectors, and page_ids.
	"""
	select_page_vectors_sql = u"""
    	SELECT * FROM page_vec
    	"""

	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_page_vectors_sql)
	    page_vectors = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return page_vectors	
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
	    return e.pgerror

def select_page_vectors ( page_ids, location = 'remote'):
	"""
	This function will return page vectors that have a pagid in the list 'page_ids'.  
	Set the location string to select the database to be used.
	"""
	if len(page_ids) ==1:
		page_ids = page_ids *2
	page_ids = tuple(page_ids)  #converts the list 'page_ids' into a format the SQL likes.
	
	select_page_vectors_sql = u"""
	    SELECT DISTINCT page_id, page_vec
	    FROM page_vec
	    WHERE page_id IN {};
	    """.format(page_ids)
	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_page_vectors_sql)
	    returned_pages = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return returned_pages
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
    	return e.pgerror


def select_all_category_vectors ( location = 'remote'):
	"""
	This function will return all category vectors, and category_ids.
	"""
	select_category_vectors_sql = u"""
    	SELECT * FROM cate_vec
    	"""

	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_category_vectors_sql)
	    category_vectors = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return category_vectors	
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
	    return e.pgerror

def select_category_vectors ( cagetgory_ids , location = 'remote'):
	"""
	This function will return category vectors that have a category id in the list 'categoru_ids'.  
	Set the location string to select the database to be used.
	"""
	if len(cagetgory_ids) ==1:
		cagetgory_ids = cagetgory_ids *2
	cagetgory_ids = tuple(cagetgory_ids)  #converts the list 'categoru_ids' into a format the SQL likes.
	
	select_category_vectors_sql = u"""
	    SELECT DISTINCT category_id, cate_vec
	    FROM cate_vec
	    WHERE category_id IN {};
	    """.format(cagetgory_ids)
	try:
	    connection, cursor = connect_to_postgres(location)
	    cursor.execute(select_category_vectors_sql)
	    returned_vectors = cursor.fetchall()
	    connection.commit()
	    cursor.close()
	    connection.close()
	    return returned_vectors
	except psycopg2.Error as e:
	    connection.rollback()
	    cursor.close()
	    connection.close()
    	return e.pgerror
>>>>>>> fd052599eb038f52abdd23f0da9c12b0d6780617
