import pandas as pd
    
# 1~ 50페이지까지의 데이터를 모두 합쳐 데이터프레임으로 변환 후 반환
def make_df(data):
    df = pd.DataFrame()
    for x in data:
        df2 = pd.DataFrame(x)
        df = pd.concat([df, df2])
        df["rating"] = df["rating"].apply(lambda x : float(x))
    return df