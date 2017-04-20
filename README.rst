Run
===

Install requirement
-------------------

$ pip install -r requirements.txt

Crawl rae
---------

$ PATH=$PATH:. python main.py

Parse Results
-------------

# Create database
python sql_create.py

# Parse
python extract.py

Count
-----

python count.py
