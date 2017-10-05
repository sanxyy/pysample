# 2 STEPS to work on the sample 
You need to install python depedent libs, use sqlite CLI to check DB content

# Python depedent libraries installation
install required python libraries

pip install -r requirements.txt  

On Linux with python 3 use pip3 
pip3 install -r requirements.txt 

Additionally, if error " No module named '_tkinter'" raised, 
on Ubuntu install the python3-tk package

sudo apt-get install python3-tk

# SQLite quick start

sqlite3 test.db   ( connect to an existing DB named test.db)
sqlite> .schema   (show table schema)
sqlite> .quit    (quit)

#SQL example 
(*)timestamp between a range
sql = 'select usage,timestamp from mem where timestamp between "2017-04-27 16:00" and "2017-04-28"'

(*)timestampe newer than specific timestamp
sql = 'select usage,timestamp from mem where timestamp > "2017-04-27 16:00" 



