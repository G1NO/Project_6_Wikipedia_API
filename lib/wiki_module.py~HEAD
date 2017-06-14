import requests
import json
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer

# Return the pages corresponding to a passed category name
# Returns a table of (category id, category name, )
# On a failure, the return is (-1, "", [])
def query_category(category):

    HTTP = "https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{}&cmlimit=500&titles={}&format=json".format(category,category)

    response = requests.get(HTTP)

    data_dict = json.loads(response.text)

    # Restrict to pages, dropping sub-categories
    subject_pages = [(row['pageid'], row['title'].encode('ascii','replace')) for row in data_dict["query"]["categorymembers"] if row['ns'] == 0]

    category_dict = data_dict["query"]["pages"][data_dict["query"]["pages"].keys()[0]]

    categoryid = category_dict.get("pageid","")
    categoryname = category_dict.get("title","")
    if categoryname != "":
        categoryname = categoryname.encode('ascii', 'replace')

    return (categoryid, categoryname, subject_pages)

def query_page(page_code):

    HTTP ="https://en.wikipedia.org/w/api.php?action=parse&format=json&pageid={}&prop=text|sections&contentmodel=wikitext".format(page_code)

    response = requests.get(HTTP)

    data_dict = json.loads(response.text.encode('ascii', 'replace'))

    if data_dict.get("error", None) != None:
        return ("", "")
    
    page_sections = [row['line'] for row in data_dict['parse']['sections']]

    extracted_text = data_dict['parse']['text']['*']
    soup = BeautifulSoup(extracted_text, "lxml")

    preprocessor = CountVectorizer().build_preprocessor()
    processed_text = preprocessor(preprocessor(soup.get_text()))

    tokenizer = CountVectorizer().build_tokenizer()
    merged_text = " ".join(tokenizer(processed_text.replace('\n',' ')))

    return (extracted_text, merged_text.encode('ascii', 'replace'))
