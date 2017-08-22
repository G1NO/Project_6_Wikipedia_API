## Overview

The task has three parts:

1. data collection
1. data exploration/algorithm developmnet
1. prediction


## Collection

300 pages across 3 categories were collected using the Wikipedia API and loaded into a Postgres database.

Built a python script that:

- will be run via a command line argument 
    - e.g. `./download #ARGS#`
- can take a filename for which it will read categories
    - e.g. `./download categories.yml`
    - here `categories.yml` would look like
   
       ```
       categories:
         - Machine_learning
         - Business_software
       ``` 
- can take a category as an argument
    - e.g. `./download Machine_learning`
- loads the returned pages into our shared Postgres database

## Search

Performed a search over the data we collected. 

Built a python script that:

- returns a text snippet from each of the top five related articles to a search query
    - a query could be any string of words
    - e.g. `./search top principal component analysis`
- returns the full text from the top related article with related words colored in red
    - e.g. `./search full principal component analysis`

## Predict
Built a predictive model over the data. When a new article comes along, able to predict the category into which that article should fall. 

This section has two scripts:

1. a training script, `./train-model`, that will train a predictive model over the dataset
2. a prediction script that takes as argument an article from Wikipedia
    - e.g. 
    
      ```
      $ ./predict Random_forest
      Predict Category: Machine_learning
      Confidence: 0.9
      ```
