import sqlite3
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

'''

connect to a sqlllite database , generate a graph using matplotlib

'''
def queryData():
    #sql = 'select usage,timestamp from mem where timestamp > "2017-08-01 00:00" and timestamp < "2017-08-31 23:00" '
    sql = 'select usage,timestamp from mem '
    print(sql)
    c = sqlite3.connect('test')
    result = c.execute(sql).fetchall()
    memList=[]
    dates=[]
    for row in result:
        memList.append(row[0]/1100000)
        dates.append(row[1])

    #print(dates)
    x = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in dates]
    #print(x)
    #2017-04-11 10:49:24
    
	#set x axis label , the following is 
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))	
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))	
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    
    #the unit of x axis (the interval between each point )is 2 hour if the following locator is set
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
	#the unit of x axis is 2 days if the following locator is set 
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
    
    
    plt.plot(x,memList,"g-")
     
    #plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.ylabel('Memory usage')
    plt.xlabel('Date')
	
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.show()
    print('bye !')
    
queryData()
