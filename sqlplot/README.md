install required python libraries

pip install -r requirements.txt  

On Linux with python 3 use pip3 
pip3 install -r requirements.txt 


SQL example 
(*)timestamp between a range
sql = 'select usage,timestamp from mem where timestamp between "2017-04-27 16:00" and "2017-04-28"'

(*)timestampe newer than specific timestamp
sql = 'select usage,timestamp from mem where timestamp > "2017-04-27 16:00" 

