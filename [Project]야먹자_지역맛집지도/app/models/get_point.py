from geopy import Nominatim

def get_point(keyword):
    geo_local = Nominatim(user_agent='South Korea')
    geo = geo_local.geocode(keyword)
    point = (geo.latitude, geo.longitude)
    return point

    
if __name__ == "__main__":
    print(get_point("제주 한림/애월"))