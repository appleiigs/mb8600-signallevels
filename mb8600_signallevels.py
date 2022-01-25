import time
#import urllib.request
#from pprint import pprint
from html_table_parser.parser import HTMLTableParser
from webbot import Browser

modemURL = "https://192.168.100.1/"
outputFileName = "mb8600log.csv"
mb8600UserName = "admin"
mb8600Password = "motorola"

web=Browser(showWindow=False)
web.go_to(modemURL)
web.click('Username')
web.type(mb8600UserName)
web.click('Password')
web.type(mb8600Password)
web.click("Login")
web.click('Advanced')
web.click('Connection')
time.sleep(30)                   #need to give the modem time to measure levels
content=web.get_page_source()
web.click('Back')
web.click('Logout')
web.quit()


# Define the HTMLTableParser object
p = HTMLTableParser()
# feed the html contents in the # HTMLTableParser object
p.feed(content)

#now parse downstream signal levels table
#downstream info is in the 8th table, i.e. p.tables[8]
#p.tables[8][1] has the header:['Channel', 'Lock Status', 'Modulation', 'Channel ID', 'Freq. (MHz)', 'Pwr (dBmV)', 'SNR (dB)', 'Corrected', 'Uncorrected']
#p.tables[8][2] starts the data: ['1', 'Locked', 'QAM256', '41', '645.0', '7.3', '42.4', '426', '256']
#downstream channels 1-33 exist

channel=range(33)
chData=[]
maxChannel=33-1               #take care of 0-indexing
empty=["","","","","","","","",""]
downOutput=""

try:
    for ch in channel:
        chData.append(p.tables[8][ch+2])
except:
    maxChannel=ch-1            #could be cases where <33 channels are locked and/or have data

for ch in channel:
    if ch<=maxChannel:
        data=chData[ch]
    else:
        data=empty
    downOutput=downOutput+",".join(data)+","

#now parse upstream signal levels table
#upstream info is in the 11th table, i.e. p.tables[11]
#p.tables[11][1] has the header: ['Channel', 'Lock Status', 'Channel Type', 'Channel ID', 'Symb. Rate (Ksym/sec)', 'Freq. (MHz)', 'Pwr (dBmV)']
#p.tables[11][2] starts the data: ['1', 'Locked', 'SC-QAM', '1', '5120', '16.4', '43.3']
#upstream channels 1-5 exist

channel=range(5)
chData=[]
maxChannel=5-1                #take care of 0-indexing
empty=["","","","","","",""]
upOutput=""

try:
    for ch in channel:
        chData.append(p.tables[11][ch+2])
except:
    maxChannel=ch-1           #could be cases where <5 channels are locked and/or have data

for ch in channel:
    if ch<=maxChannel:
        data=chData[ch]
    else:
        data=empty
    upOutput=upOutput+",".join(data)+","

sampleTime=time.strftime("%m/%d/%y,%H:%M:%S,")

f=open(outputFileName, "a")
f.write(sampleTime)
f.write(downOutput)
f.write(upOutput)
f.write("\n")
f.close()

exit()
