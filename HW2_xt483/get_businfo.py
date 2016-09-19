
import pylab as pl
import json
import requests
import urllib2 as ulr
import numpy as np
import pandas as pd
import os
import sys


def get_info(key,busline,filename):
    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline
    response = ulr.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)




    print "Bus Line :", busline
    bustotal = np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    businfo = pd.DataFrame(columns = ['Latitude', 'Longitude','Stop Name', 'Stop Status'])

    for i in range(bustotal):
        lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        nextstop = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']
        if 'OnwardCall' in nextstop:
            nextstop1 =nextstop['OnwardCall']
   
            if (np.size(nextstop1) > 1):
                stopname = nextstop['OnwardCall'][1]['StopPointName']
                status = nextstop['OnwardCall'][1]['Extensions']['Distances']['PresentableDistance']
            else :
                stopname = 'N/A'
                status = 'N/A'
        else:
            stopname = 'N/A'
            status = 'N/A'
    
        info = pd.DataFrame({ 'Latitude': [lat], 'Longitude': [lon], 'Stop Name': stopname, 'Stop Status': status})    
    
        businfo = businfo.append(info)
    businfo.to_csv(filename,index=0)
    
if __name__ =="main":
    if not len(sys.argv) == 3:
        print 'Enter a valid busline'
        sys.exit()
    get_info(sys.argv[1],sys.argv[2],sys.argv[3])



