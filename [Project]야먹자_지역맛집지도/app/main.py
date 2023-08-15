from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # 템플릿 엔진
from app.config import BASE_DIR  # 현재 config.py가 있는 주소를 반환
from app.models import mongodb
from app.models.map_maker import Make_map
from app.models.mango_scraper import MangoScraper
from app.models.get_loc_cat import GetLocCat
from app.models.change_df import make_df
from app.models.get_point import get_point

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# 기본 화면
@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


# 입력 후 화면
@app.get("/input", response_class=HTMLResponse)
async def input(request: Request):
    # 1. 쿼리에서 제외할 음식 추출
    keyword = request.query_params.get("q")  # 쿼리에서 키워드 추출
    # (예외처리)
    # 1) 입력받은 값이 없는 경우
    if not keyword:  # 키워드가 없다면 사용자에게 검색을 요구
        context = {"request": request}
        return templates.TemplateResponse("index2.html", context=context)
    else:
        # 이미 DB에 저장되어 있는 자료라면
        if mongodb.db["ya"].find_one({"keyword": keyword}):
            map_info = mongodb.db["ya"].find(
                {"$and": [{"keyword": keyword}, {"rating": {"$gte": 3.0}}]}
            )  # 키워드가 같고 별점이 3.0 이상인 곳만 데이터 추출
            parking_info = mongodb.db["parking"].find({"주소": {"$regex": keyword}})
            df, parking = Make_map.load_data(map_info, parking_info)
            point = get_point(keyword)  # 검색 위치의 좌표 확보
            map_info = Make_map.makemap(df, parking, point)
            context = {"request": request, "map": map_info}
            return templates.TemplateResponse("index2.html", context=context)
        else:  # DB에 저장되어 있지 않는 자료라면 수집 후 저장 한 뒤 맵 생성
            mango_scraper = MangoScraper()
            mango_data = await mango_scraper.search(keyword)
            df = make_df(mango_data)
            get_loccat = GetLocCat()
            new_df = get_loccat.run(keyword, df)  # keyword 와 관련된 지도 좌표와 DataFrame을 반환
            mongodb.db["ya"].insert_many(new_df.to_dict("records"))  # DataFrame을 DB에 저장
            map_info = mongodb.db["ya"].find(
                {"$and": [{"keyword": keyword}, {"rating": {"$gte": 3.0}}]}
            )  # 키워드가 같고 별점이 3.0 이상인 곳만 데이터 추출
            parking_info = mongodb.db["parking"].find({"주소": {"$regex": keyword}})
            point = get_point(keyword)  # 검색 위치의 좌표 확보
            df, parking = Make_map.load_data(map_info, parking_info)
            map_info = Make_map.makemap(df, parking, point)
            context = {"request": request, "map": map_info}
            return templates.TemplateResponse("index2.html", context=context)


# app이 시작될 때 실행
@app.on_event("startup")
def on_app_start():
    mongodb.connect()


# app이 멈출 때 실행
@app.on_event("shutdown")
def on_app_shutdown():
    mongodb.close()
