import os
import requests
import xml.etree.ElementTree as ET

from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()
keycode_decoding = settings.KEYCODE_DECODING

# 버스노선 조회
@router.get("/getBusRouteInfoItem")
def getBusRouteInfoItem(key: str, route_id: int):
    url = 'http://apis.data.go.kr/6410000/busrouteservice/getBusRouteInfoItem'
    params ={'serviceKey' : key, 'routeId' : route_id }
    return requests.get(url, params=params)

# 정류장 조회
@router.get("/getBusStationList")
def getBusStationList(key, keyword):
    url = 'http://apis.data.go.kr/6410000/busstationservice/getBusStationList'
    params ={'serviceKey' : key, 'keyword' : keyword }
    response = requests.get(url, params=params)
    print(response)

    response = getBusStationList(keycode_decoding, '22009')
    root = ET.fromstring(response.text)
    bus_station_info_list = []
    for idx_child, child in enumerate(root.find('msgBody')):
        temp_dict = {}
        for a in child:
            temp_dict[a.tag] = a.text
        bus_station_info_list.append(temp_dict)
    print(bus_station_info_list)
    return response

# 버스 도착 정보 조회
@router.get("/getBusArrivalList")
def getBusArrivalList(key, station_id):
    url = 'http://apis.data.go.kr/6410000/busarrivalservice/getBusArrivalList'
    params ={'serviceKey' : key, 'stationId' : station_id }
    return requests.get(url, params=params)

# 버스 위치 정보 조회
@router.get("/getBusLocationList")
def getBusLocationList(key, route_id):
    url = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList'
    params ={'serviceKey' : key, 'routeId' : route_id }
    return requests.get(url, params=params)