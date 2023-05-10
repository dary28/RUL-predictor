import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler

def getBatteryCapacity(Battery):
    cycle = []
    capacity = []
    i = 1
    for Bat in Battery:
        if Bat['cycle'] == 'discharge':
            cycle.append(i)
            capacity.append(Bat['data']['Capacity'][0])
            i += 1
    return [cycle, capacity]

def getChargingValues(Battery, Index):
    Battery = Battery[Index]['data']
    index = []
    i = 1
    for iterator in Battery['Voltage_measured']:
        index.append(i)
        i += 1
    return [index, Battery['Voltage_measured'], Battery['Current_measured'], Battery['Temperature_measured'], Battery['Voltage_charge'], Battery['Time']]

def getDischargingValues(Battery, Index):
    Battery = Battery[Index]['data']
    index = []
    i = 1
    for iterator in Battery['Voltage_measured']:
        index.append(i)
        i += 1
    return [index, Battery['Voltage_measured'], Battery['Current_measured'], Battery['Temperature_measured'], Battery['Voltage_load'], Battery['Time']]

def getMaxDischargeTemp(Battery):
    cycle = []
    temp = []
    i = 1
    for Bat in Battery:
        if Bat['cycle'] == 'discharge':
            cycle.append(i)
            temp.append(max(Bat['data']['Temperature_measured']))
            i += 1
    return [cycle, temp]

def getMaxChargeTemp(Battery, discharge_len):
    cycle = []
    temp = []
    i = 1
    for Bat in Battery:
        if Bat['cycle'] == 'charge':
            cycle.append(i)
            temp.append(max(Bat['data']['Temperature_measured']))
            i += 1
    return [cycle[:discharge_len], temp[:discharge_len]]

def getDataframe(Battery):
    l = getBatteryCapacity(Battery)
    data = {'cycle':l[0],'capacity':l[1]}
    d=pd.DataFrame(data)
    return d




