## Overview

The task has three parts:

1. data collection
1. data exploration/algorithm developmnet
1. prediction


## Collection

In teams, collect at least 300 pages across 3 categories using the Wikipedia API and load these pages into a Postgres database.

You must build a python script that:

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

Individually, perform a search over the data we collected. 

You must build a python script that:

- returns a text snippet from each of the top five related articles to a search query
    - a query could be any string of words
    - e.g. `./search top principal component analysis`
- returns the full text from the top related article with related words colored in red
    - e.g. `./search full principal component analysis`

## Predict
Build a predictive model over your data. When a new article comes along, you must be able to predict the category into which that article should fall. 

This section will have two scripts:

1. a training script, `./train-model`, that will train a predictive model over your dataset
2. a prediction script that takes as argument an article from Wikipedia
    - e.g. 
    
      ```
      $ ./predict Random_forest
      Predict Category: Machine_learning
      Confidence: 0.9
      ```
