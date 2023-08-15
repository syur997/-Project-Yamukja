import pandas as pd
import folium
from folium.features import CustomIcon
from folium import Marker # Icon, CircleMarker
from app.config import BASE_DIR
import folium.plugins as plug
from folium import plugins

from pathlib import Path

class Make_map:
    
    def load_data(df, parking_df):
        df = pd.DataFrame(list(df))
        parking_df = pd.DataFrame(list(parking_df))
        df["rating"] = df["rating"].apply(lambda x : str(x))
        return df, parking_df
    
    def makemap(df, parking_df, point):
        map = folium.Map(location=[point[0], point[1]], zoom_start=13) # 37.5222564, 126.9120236

        fg = folium.FeatureGroup(name='식당')
        map.add_child(fg)

        g_meat = plugins.FeatureGroupSubGroup(fg, '고기')
        map.add_child(g_meat)

        g_kor = plugins.FeatureGroupSubGroup(fg, '한식')
        map.add_child(g_kor)

        g_chn = plugins.FeatureGroupSubGroup(fg, '중식')
        map.add_child(g_chn)

        g_jap = plugins.FeatureGroupSubGroup(fg, '일식')
        map.add_child(g_jap)

        g_wst = plugins.FeatureGroupSubGroup(fg, '양식')
        map.add_child(g_wst)

        g_etc = plugins.FeatureGroupSubGroup(fg, '기타')
        map.add_child(g_etc)

        g_cafe = folium.FeatureGroup(name='카페')
        map.add_child(g_cafe)

        g_park = folium.FeatureGroup('주차장')
        map.add_child(g_park)

        folium.LayerControl(collasped=False).add_to(map)
        
        # 식당, 카페 marker 찍기
        for idx in df.index:

            if df['new_cate'][idx] =='meat':
                icon_meat_png = str(BASE_DIR / "templates" / "marker_image" / "고기.png")
                icon_meat = CustomIcon(icon_meat_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_meat).add_to(g_meat)
            
            
            elif df['new_cate'][idx] =='kor':
                icon_kor_png = str(BASE_DIR / "templates" / "marker_image" / "한식.png")
                icon_kor = CustomIcon(icon_kor_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_kor).add_to(g_kor)
                
            elif df['new_cate'][idx] =='chn':
                icon_chn_png = str(BASE_DIR / "templates" / "marker_image" / "중식.png")
                icon_chn = CustomIcon(icon_chn_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_chn).add_to(g_chn)
        
            
            elif df['new_cate'][idx] =='jap':
                icon_jap_png = str(BASE_DIR / "templates" / "marker_image" / "일식.png")
                icon_jap = CustomIcon(icon_jap_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_jap).add_to(g_jap)
            
            
            elif df['new_cate'][idx] =='wst':
                icon_wst_png = str(BASE_DIR / "templates" / "marker_image" / "양식.png")
                icon_wst = CustomIcon(icon_wst_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_wst).add_to(g_wst)
                
                
            elif df['new_cate'][idx] =='cafe':
                icon_cafe_png = str(BASE_DIR / "templates" / "marker_image" / "카페.png")
                icon_cafe = CustomIcon(icon_cafe_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_cafe).add_to(g_cafe)   
            
            else :
                icon_etc_png = str(BASE_DIR / "templates" / "marker_image" / "식당.png")
                icon_etc = CustomIcon(icon_etc_png, icon_size=(30, 30), icon_anchor=(10, 20))
                folium.Marker([df['lat'][idx], df['lng'][idx]], 
                                popup=folium.Popup('<center><strong>'+ df['title'][idx] + '</strong></center><br>'\
                                                + '별점:'+ df['rating'][idx] + '<br>'\
                                                + '분류:' + df['category'][idx] + '<br>'\
                                                + '<a href=' + df['url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 300),
                                tooltip=df['title'][idx], icon=icon_etc).add_to(g_etc)
                
        # 주차장 클러스터 만들어주기
        mc = plug.MarkerCluster()

            # 주차장 marker 찍기
        for idxx in parking_df.index :
                icon_park_png = str(BASE_DIR / "templates" / "marker_image" / "주차장.png")
                icon_park = CustomIcon(icon_park_png, icon_size=(30, 30), icon_anchor=(10, 20))
                mc.add_child(Marker([parking_df['주차장 위치 좌표 위도'][idxx], parking_df['주차장 위치 좌표 경도'][idxx]],\
                                    popup=folium.Popup('<center><strong>'+ parking_df['주차장명'][idxx]+'</strong></center><br>'\
                                                        + '전화번호:' + parking_df['전화번호'][idxx]+ '<br>'\
                                                        + '야간 개방 여부:' + parking_df['야간무료개방여부명'][idxx] + '<br>', max_width = 400),
                                    tooltip=parking_df['주차장명'][idxx], icon=icon_park)).add_to(g_park)
            
        map
        return map._repr_html_()