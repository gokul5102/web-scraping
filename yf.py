# Plotting line charts for 5 banking institutions and NBFCs over a period of 5 years
#(Open,High,Low,Close,Adjusted Close)

import requests 
from bs4 import BeautifulSoup 
import html5lib
import re
from matplotlib import pyplot as plt 

plt.xkcd()

# ICICI 
url1='https://in.finance.yahoo.com/quote/ICICIBANK.NS/history?period1=1448841600&period2=1606694400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r1=requests.get(url1)
soup1=BeautifulSoup(r1.content,'html5lib')

table1= soup1.find('div', class_='Pb(10px) Ovx(a) W(100%)')  

#Hdfc 
url2='https://in.finance.yahoo.com/quote/HDFCBANK.NS/history?period1=1448841600&period2=1606694400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r2=requests.get(url2)
soup2=BeautifulSoup(r2.content,'html5lib')

table2= soup2.find('div', class_='Pb(10px) Ovx(a) W(100%)')  

# bajaj  finance
url3='https://in.finance.yahoo.com/quote/BAJFINANCE.NS/history?period1=1448841600&period2=1606694400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r3=requests.get(url3)
soup3=BeautifulSoup(r3.content,'html5lib')

table3= soup3.find('div', class_='Pb(10px) Ovx(a) W(100%)')  

# kotak mahindra
url4='https://in.finance.yahoo.com/quote/KOTAKBANK.NS/history?period1=1448841600&period2=1606694400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r4=requests.get(url4)
soup4=BeautifulSoup(r4.content,'html5lib')

table4= soup4.find('div', class_='Pb(10px) Ovx(a) W(100%)')  

# axis
url5='https://in.finance.yahoo.com/quote/AXISBANK.NS/history?period1=1448841600&period2=1606694400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r5=requests.get(url5)
soup5=BeautifulSoup(r5.content,'html5lib')

table5= soup5.find('div', class_='Pb(10px) Ovx(a) W(100%)')  

info=[]  # Common variables for every bank
extracted_info=[] #Common variables for every bank

final_dates=[]

open_price_icici=[]
open_price_hdfc=[]
open_price_bajFin=[]
open_price_kotMah=[]
open_price_axis=[]

high_price_icici=[]
high_price_hdfc=[]
high_price_bajFin=[]
high_price_kotMah=[]
high_price_axis=[]

low_price_icici=[]
low_price_hdfc=[]
low_price_bajFin=[]
low_price_kotMah=[]
low_price_axis=[]

close_price_icici=[]
close_price_hdfc=[]
close_price_bajFin=[]
close_price_kotMah=[]
close_price_axis=[]

adjClose_price_icici=[]
adjClose_price_hdfc=[]
adjClose_price_bajFin=[]
adjClose_price_kotMah=[]
adjClose_price_axis=[]

#Icici bank 

final_icici=[] #individual list for every bank


for row in table1.findAll('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'):
         for x in row.findAll('td',class_='Py(10px)'):
              info.append(x.span.text)
         while(len(info)!=0):
              if(re.search("^01-Nov-20([1][6-9]|[2][0])$",info[0])):
                  for i in range(7):
                      extracted_info.append(info[i])
                  final_icici.append(extracted_info)
              extracted_info =[]
              info=info[7:]

for i in final_icici:
     i.pop(-1)
     
for i in final_icici:
     final_dates.append(i[0])#Common for all banks

final_dates.reverse()

for i in final_icici:
     open_price_icici.append(i[1])

for i in final_icici:
     high_price_icici.append(i[2])

for i in final_icici:
     low_price_icici.append(i[3])

for i in final_icici:
     close_price_icici.append(i[4])

for i in final_icici:
     adjClose_price_icici.append(i[5])

open_price_icici.reverse()
high_price_icici.reverse()
low_price_icici.reverse()
close_price_icici.reverse()
adjClose_price_icici.reverse()

open_price_icici=[float(i.replace(',','')) for i in open_price_icici]

high_price_icici=[float(i.replace(',','')) for i in high_price_icici]

low_price_icici=[float(i.replace(',','')) for i in low_price_icici]

close_price_icici=[float(i.replace(',','')) for i in close_price_icici]

adjClose_price_icici=[float(i.replace(',','')) for i in adjClose_price_icici]


#hdfc bank

final_hdfc=[] #individual list for every bank

for row in table2.findAll('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'):
         for x in row.findAll('td',class_='Py(10px)'):
              info.append(x.span.text)
         while(len(info)!=0):
              if(re.search("^01-Nov-20([1][6-9]|[2][0])$",info[0])):
                  for i in range(7):
                      extracted_info.append(info[i])
                  final_hdfc.append(extracted_info)
              extracted_info =[]
              info=info[7:]

for i in final_hdfc:
     i.pop(-1)

for i in final_hdfc:
     open_price_hdfc.append(i[1])

for i in final_hdfc:
     high_price_hdfc.append(i[2])

for i in final_hdfc:
     low_price_hdfc.append(i[3])

for i in final_hdfc:
     close_price_hdfc.append(i[4])

for i in final_hdfc:
     adjClose_price_hdfc.append(i[5])

open_price_hdfc.reverse()
high_price_hdfc.reverse()
low_price_hdfc.reverse()
close_price_hdfc.reverse()
adjClose_price_hdfc.reverse()

open_price_hdfc=[float(i.replace(',','')) for i in open_price_hdfc]

high_price_hdfc=[float(i.replace(',','')) for i in high_price_hdfc]

low_price_hdfc=[float(i.replace(',','')) for i in low_price_hdfc]

close_price_hdfc=[float(i.replace(',','')) for i in close_price_hdfc]

adjClose_price_hdfc=[float(i.replace(',','')) for i in adjClose_price_hdfc]

#bajFinance

final_bajFin=[] #individual list for every bank

for row in table3.findAll('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'):
         for x in row.findAll('td',class_='Py(10px)'):
              info.append(x.span.text)
         while(len(info)!=0):
              if(re.search("^01-Nov-20([1][6-9]|[2][0])$",info[0])):
                  for i in range(7):
                      extracted_info.append(info[i])
                  final_bajFin.append(extracted_info)
              extracted_info =[]
              info=info[7:]

for i in final_bajFin:
     i.pop(-1)

for i in final_bajFin:
     open_price_bajFin.append(i[1])

for i in final_bajFin:
     high_price_bajFin.append(i[2])

for i in final_bajFin:
     low_price_bajFin.append(i[3])

for i in final_bajFin:
     close_price_bajFin.append(i[4])

for i in final_bajFin:
     adjClose_price_bajFin.append(i[5])

open_price_bajFin.reverse()
high_price_bajFin.reverse()
low_price_bajFin.reverse()
close_price_bajFin.reverse()
adjClose_price_bajFin.reverse()

open_price_bajFin=[float(i.replace(',','')) for i in open_price_bajFin]

high_price_bajFin=[float(i.replace(',','')) for i in high_price_bajFin]

low_price_bajFin=[float(i.replace(',','')) for i in low_price_bajFin]

close_price_bajFin=[float(i.replace(',','')) for i in close_price_bajFin]

adjClose_price_bajFin=[float(i.replace(',','')) for i in adjClose_price_bajFin]

#Kotak mahindra bank

final_kotMah=[] #individual list for every bank

for row in table4.findAll('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'):
         for x in row.findAll('td',class_='Py(10px)'):
              info.append(x.span.text)
         while(len(info)!=0):
              if(re.search("^01-Nov-20([1][6-9]|[2][0])$",info[0])):
                  for i in range(7):
                      extracted_info.append(info[i])
                  final_kotMah.append(extracted_info)
              extracted_info =[]
              info=info[7:]

for i in final_kotMah:
     i.pop(-1)

for i in final_kotMah:
     open_price_kotMah.append(i[1])

for i in final_kotMah:
     high_price_kotMah.append(i[2])

for i in final_kotMah:
     low_price_kotMah.append(i[3])

for i in final_kotMah:
     close_price_kotMah.append(i[4])

for i in final_kotMah:
     adjClose_price_kotMah.append(i[5])

open_price_kotMah.reverse()
high_price_kotMah.reverse()
low_price_kotMah.reverse()
close_price_kotMah.reverse()
adjClose_price_kotMah.reverse()

open_price_kotMah=[float(i.replace(',','')) for i in open_price_kotMah]

high_price_kotMah=[float(i.replace(',','')) for i in high_price_kotMah]

low_price_kotMah=[float(i.replace(',','')) for i in low_price_kotMah]

close_price_kotMah=[float(i.replace(',','')) for i in close_price_kotMah]

adjClose_price_kotMah=[float(i.replace(',','')) for i in adjClose_price_kotMah]

#axis bank

final_axis=[] #individual list for every bank

for row in table5.findAll('tr',class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'):
         for x in row.findAll('td',class_='Py(10px)'):
              info.append(x.span.text)
         while(len(info)!=0):
              if(re.search("^01-Nov-20([1][6-9]|[2][0])$",info[0])):
                  for i in range(7):
                      extracted_info.append(info[i])
                  final_axis.append(extracted_info)
              extracted_info =[]
              info=info[7:]

for i in final_axis:
     i.pop(-1)


for i in final_axis:
     open_price_axis.append(i[1])

for i in final_axis:
     high_price_axis.append(i[2])

for i in final_axis:
     low_price_axis.append(i[3])

for i in final_axis:
     close_price_axis.append(i[4])

for i in final_axis:
     adjClose_price_axis.append(i[5])

open_price_axis.reverse()
high_price_axis.reverse()
low_price_axis.reverse()
close_price_axis.reverse()
adjClose_price_axis.reverse()

open_price_axis=[float(i.replace(',','')) for i in open_price_axis]

high_price_axis=[float(i.replace(',','')) for i in high_price_axis]

low_price_axis=[float(i.replace(',','')) for i in low_price_axis]

close_price_axis=[float(i.replace(',','')) for i in close_price_axis]

adjClose_price_axis=[float(i.replace(',','')) for i in adjClose_price_axis]

#Plotting charts

#Open
plt.figure(1)
plt.plot(final_dates,open_price_icici,label='ICICI Bank',color='red')
plt.plot(final_dates,open_price_axis,label='Axis Bank',color='yellow')
plt.plot(final_dates,open_price_kotMah,label='Kotak Mahindra Bank',color='green')
plt.plot(final_dates,open_price_hdfc,label='HDFC Bank',color='blue')
plt.plot(final_dates,open_price_bajFin,label='Bajaj Finance',color='black')
plt.xlabel("Dates of Interest")
plt.ylabel("Open price ")
plt.title("Open prices for various banks over 5 years")
plt.legend(loc=0)
plt.tight_layout()

#High
plt.figure(2)
plt.plot(final_dates,high_price_icici,label='ICICI Bank',color='red')
plt.plot(final_dates,high_price_axis,label='Axis Bank',color='yellow')
plt.plot(final_dates,high_price_kotMah,label='Kotak Mahindra Bank',color='green')
plt.plot(final_dates,high_price_hdfc,label='HDFC Bank',color='blue')
plt.plot(final_dates,high_price_bajFin,label='Bajaj Finance',color='black')
plt.xlabel("Dates of Interest")
plt.ylabel("High price ")
plt.title("High prices for various banks over 5 years")
plt.legend(loc=0)
plt.tight_layout()

#Low
plt.figure(3)
plt.plot(final_dates,low_price_icici,label='ICICI Bank',color='red')
plt.plot(final_dates,low_price_axis,label='Axis Bank',color='yellow')
plt.plot(final_dates,low_price_kotMah,label='Kotak Mahindra Bank',color='green')
plt.plot(final_dates,low_price_hdfc,label='HDFC Bank',color='blue')
plt.plot(final_dates,low_price_bajFin,label='Bajaj Finance',color='black')
plt.xlabel("Dates of Interest")
plt.ylabel("low price ")
plt.title("Low prices for various banks over 5 years")
plt.legend(loc=0)
plt.tight_layout()

#Close
plt.figure(4)
plt.plot(final_dates,close_price_icici,label='ICICI Bank',color='red')
plt.plot(final_dates,close_price_axis,label='Axis Bank',color='yellow')
plt.plot(final_dates,close_price_kotMah,label='Kotak Mahindra Bank',color='green')
plt.plot(final_dates,close_price_hdfc,label='HDFC Bank',color='blue')
plt.plot(final_dates,close_price_bajFin,label='Bajaj Finance',color='black')
plt.xlabel("Dates of Interest")
plt.ylabel("Close price ")
plt.title("Closing prices for various banks over 5 years")
plt.legend(loc=0)
plt.tight_layout()

#Adjusted close
plt.figure(5)
plt.plot(final_dates,adjClose_price_icici,label='ICICI Bank',color='red')
plt.plot(final_dates,adjClose_price_axis,label='Axis Bank',color='yellow')
plt.plot(final_dates,adjClose_price_kotMah,label='Kotak Mahindra Bank',color='green')
plt.plot(final_dates,adjClose_price_hdfc,label='HDFC Bank',color='blue')
plt.plot(final_dates,adjClose_price_bajFin,label='Bajaj Finance',color='black')
plt.xlabel("Dates of Interest")
plt.ylabel("Adjusted Close price ")
plt.title("Adjusted Closing prices for various banks over 5 years")
plt.legend(loc=0)
plt.tight_layout()

plt.show()




   



