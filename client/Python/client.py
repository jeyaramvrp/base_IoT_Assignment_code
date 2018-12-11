#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib2
import matplotlib.pyplot as tempgraph

#For plotting
tempgraph.ion()
fig=tempgraph.figure()
tempgraph.axis([0,12,0,99])

response = urllib2.urlopen('http://localhost:8080/')
resp = response.read()

#Read Response
resp = resp.split('\n')
#Time in X axis and temp on Y axis
for data in resp:
  try:
      x=int(data[15:17])
      y=int(data[40:42])
      tempgraph.scatter(x,y);
      tempgraph.show()
      tempgraph.pause(0.001)
  except:
      pass
