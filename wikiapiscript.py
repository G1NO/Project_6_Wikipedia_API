#!/Users/ginodefalco/anaconda/bin/python

base_url = "https://en.wikipedia.org/w/api.php"

def create_query_param_string(params):
    param_list = [key+'='+str(value) for key, value in params.items()]
    return '?'+'&'.join(param_list)

def wikipedia_page_format(page):
    return page.lower().capitalize().replace(' ','_')

# These helper functions help us parse JSON responses to
# discard metadata corresponding to the response.

def parse_pages_from_json(response_json):
    return response_json['query']['pages']

def parse_headings_from_json(response_json):
    return response_json['mobileview']['sections']

def parse_category_page_from_json(response_json):
    return response_json['query']['categorymembers']

def wikipedia_get_cagegory(category):
    params = { 'action' : 'query',
                'format' : 'json',
                'prop' : 'extracts',
                'exlimit' : 'maxl'
                 }

    params['titles'] = 'Category:'+quote(category)

    query_param_string = create_query_param_string(params)

    response = get(base_url+query_param_string)

    try:
        return parse_pages_from_json(response.json())
    except:
        return response

def wikipedia_get_pages_for_category(category):
    params = { 'action' : 'query',
               'format' : 'json',
               'list' : 'categorymembers',
               'cmlimit' : 'max'
                     }

    params['cmtitle'] = 'Category:'+wikipedia_page_format(category)

    query_param_string = create_query_param_string(params)

    response = get(base_url+query_param_string)

    return response.json()['query']['categorymembers']

    try:
        return parse_headings_from_json(response.json())
    except:
        return response


def wikipedia_get_page_headings(title):
    params = { 'action' : 'mobileview',
               'format' : 'json',
               'prop' : 'sections',
               'sections' : 'all'
                     }

    params['page'] = quote(title)

    query_param_string = create_query_param_string(params)

    response = get(base_url+query_param_string)

    try:
        return parse_headings_from_json(response.json())
    except:
        return parse_headings_from_json(response.json())






from datetime import datetime

print ("You're dead!")
print (datetime.now())
