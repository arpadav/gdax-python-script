from datetime import datetime


#2017-12-19T21:39:58.457Z
#2017-12-19T22:16:55.534000Z

#2017-12-19 17:17:19.463103

thisTime = "2017-12-19T21:39:58.457Z"
newThisTime = thisTime[:19]
newThisTime = newThisTime.replace('T', ' ')
newThisTime = newThisTime.replace('Z', '')
this2Time = "2017-12-19T21:40:02.534000Z"
this2Time = this2Time[:19]
this2Time = this2Time.replace('T', ' ')
this2Time = this2Time.replace('Z', '')
thisTimeobject = datetime.strptime(newThisTime, "%Y-%m-%d %H:%M:%S")
print(thisTimeobject)
this2Timeobject = datetime.strptime(this2Time, "%Y-%m-%d %H:%M:%S")
print(this2Time)
print(this2Timeobject - thisTimeobject)
checkDateobject = (this2Timeobject - thisTimeobject)

if checkDateobject.days <= -1:
    print('yay')