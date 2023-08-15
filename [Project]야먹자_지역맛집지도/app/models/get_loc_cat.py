# import googlemaps
import joblib

# import pandas as pd
from tqdm import tqdm
from app.config import GOOGLE_API_KEY
from app.config import BASE_DIR
from geopy import Nominatim


class GetLocCat:
    def __init__(self):
        # self.gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
        self.geo_local = Nominatim(user_agent="South Korea")
        self.pipe = joblib.load(str(BASE_DIR / "models" / "lightgbmClassifier.joblib"))

    def get_loc(self, address):
        lat = []
        lng = []
        for y in tqdm(address):
            try:
                geo = self.geo_local.geocode(y)
                lat_temp = geo.latitude  # 위도
                lng_temp = geo.longitude  # 경도
                lat.append(lat_temp)
                lng.append(lng_temp)
                # googlemaps API
                # geocode_result = self.gmaps.geocode(y, language='ko')
                # lat_temp = geocode_result[0]["geometry"]["location"]["lat"] # 위도
                # lng_temp = geocode_result[0]["geometry"]["location"]["lng"] # 경도
                # lat.append(lat_temp)
                # lng.append(lng_temp)
            except :
                lat.append(0)
                lng.append(0)
        return lat, lng

    def get_cat(self, X):
        self.y = self.pipe.predict(X)
        return self.y

    def run(self, keyword, df):
        df["new_cate"] = self.get_cat(df[["category"]])
        lat, lng = self.get_loc(df["address"])
        df["lat"] = lat
        df["lng"] = lng
        df["keyword"] = keyword
        return df


if __name__ == "__main__":
    gu_list = []
