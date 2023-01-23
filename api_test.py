import os
import requests
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
keycode_decoding = os.environ.get('keycode_encoding')

# 버스노선 조회
def getBusRouteInfoItem(key, route_id):
    url = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'
    params ={'serviceKey' : key, 'routeId' : route_id }
    return requests.get(url, params=params)

# 정류장 조회
def getBusStationList(key, keyword):
    url = 'http://apis.data.go.kr/6410000/busstationservice/getBusStationList'
    params ={'serviceKey' : key, 'keyword' : keyword }
    return requests.get(url, params=params)

# 버스 도착 정보 조회
def getBusArrivalList(key, station_id):
    url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList'
    params ={'serviceKey' : key, 'stationId' : station_id }
    return requests.get(url, params=params)

# 버스 위치 정보 조회
def getBusLocationList(key, route_id):
    url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
    params ={'serviceKey' : key, 'routeId' : route_id }
    return requests.get(url, params=params)

# districtCd : 노선 관할지역코드 (1:서울, 2:경기, 3:인천)

# 신분당선 강남역 22009
response = getBusStationList(keycode_decoding, '22009')
root = ET.fromstring(response.text)
bus_station_info_list = []
for idx_child, child in enumerate(root.find('msgBody')):
    temp_dict = {}
    for a in child:
        temp_dict[a.tag] = a.text
    bus_station_info_list.append(temp_dict)
pprint(bus_station_info_list)


response = getBusArrivalList(keycode_decoding, '121000009')
root = ET.fromstring(response.text)
bus_arrival_info_list = []
for idx_child, child in enumerate(root.find('msgBody')):
    temp_dict = {}
    for a in child:
        temp_dict[a.tag] = a.text
    bus_arrival_info_list.append(temp_dict)
pprint(bus_arrival_info_list)

# 5100번 버스 / 200000115
response = getBusRouteInfoItem(keycode_decoding, '200000115')
root = ET.fromstring(response.text)
bus_route_info_list = []
for idx_child, child in enumerate(root.find('msgBody')):
    temp_dict = {}
    for a in child:
        temp_dict[a.tag] = a.text
    bus_route_info_list.append(temp_dict)
pprint(bus_route_info_list)


response = getBusLocationList(keycode_decoding, '200000115')
root = ET.fromstring(response.text)
bus_location_info_list = []
for idx_child, child in enumerate(root.find('msgBody')):
    temp_dict = {}
    for a in child:
        temp_dict[a.tag] = a.text
    bus_location_info_list.append(temp_dict)
pprint(bus_location_info_list)