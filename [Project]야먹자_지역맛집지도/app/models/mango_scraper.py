from bs4 import BeautifulSoup
import aiohttp
import asyncio
from fake_useragent import UserAgent
import time
import pandas as pd

BASE_URL = "https://www.mangoplate.com/search/"


class MangoScraper:
    async def fetch(session, url):
        # 페이지 별 데이터를 한번에 모아 dict로 반환
        async with session.get(url) as response:
            html_data = await response.text()
            soup = BeautifulSoup(html_data, "html.parser")
            data = soup.find("ul", "list-restaurants")
            title = data.find_all("h2", "title")
            titles = [x.text.replace("\n", "").replace(" ", "") for x in title]
            url = data.find_all("a", "only-desktop_not")
            urls = ["https://www.mangoplate.com" + x["href"] for x in url]
            rating = data.find_all("strong", "search_point")
            ratings = [x.text for x in rating]
            etc = data.find_all("p", "etc")
            # locations = [x.text.split("-")[0].strip() for x in etc]
            address = data.find_all("img", "center-croping")
            addresses = [x["alt"].split("-")[1].lstrip() for x in address]
            categories = [x.text.split("-")[1].replace(" ", "") for x in etc]
            dict_col = [
                "title",
                "url",
                "rating",
                # "location",
                "category",
                "address",
            ]
            dict_list = [
                titles,
                urls,
                ratings,
                # locations,
                categories,
                addresses,
            ]
            dict_data = dict(zip(dict_col, dict_list))
            return dict_data

    async def search(self, keyword):
        ua = UserAgent(verify_ssl=False)
        userAgent = ua.random
        headers = {"User-Agent": userAgent}
        urls = [
            f"{BASE_URL}{keyword}?keyword={keyword}&page={i}"
            for i in range(1, 2)  # 1 ~ 50 페이지까지 수집
        ]  # 1 ~ 5페이지
        async with aiohttp.ClientSession(headers=headers) as session:
            all_data = await asyncio.gather(
                *[MangoScraper.fetch(session, url) for url in urls]
            )  # 페이지 별 dict를 list로 묶어 반환
        return all_data

    def run(self, keyword):
        return asyncio.run(self.search(keyword))


if __name__ == "__main__":
    pass
    # gu_list = ["도봉구", "강북구", "노원구", "은평구", "성북구", "중랑구", "서대문구", "종로구", "동대문구", "마포구", "중구",\
    #             "용산구", "성동구", "광진구", "강서구", "양천구", "구로구", "금천구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]
    # for x in gu_list:
    #     keyword = x
    #     scraper = MangoScraper()
    #     start = time.time()
    #     results = scraper.run(keyword)
    #     end = time.time()
    #     df = pd.DataFrame(results[0])
    #     for x in results[1:]:
    #         df2 = pd.DataFrame(x)
    #         df = pd.concat([df, df2])
    #     df.to_csv(f"{keyword}.csv", index=False, encoding='utf-8-sig')
    #     print((end - start))
