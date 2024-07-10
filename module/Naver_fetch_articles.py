import pandas as pd
import os
from module.Naver_seoul_land import Naver_seoul_land
import time
import numpy as np

class Naver_fetch_articles(Naver_seoul_land) :
    def __init__(self) :
        super().__init__()
        
    # todo : 셀레니움으로 header를 좀 가져와야한다.
    def fetch(self, 
              complexNos = [1147, 119219], 
              realEstateType = "APT:PRE",
              tradeType = "A1:B1", 
              areaNos = '',
              page = 1, 
              rentPriceMin= 0,
              rentPriceMax= 900000000,
              priceMin= 0,
              priceMax= 900000000,
              areaMin= 0,
              areaMax= 900000000,
              oldBuildYears= "",
              recentlyBuildYears= "",
              minHouseHoldCount= "",
              maxHouseHoldCount= "",
              delay = 2.0,
              progressChanged=None,
              progressNameChanged=None,
              resultReady=None) : 
        
        realEstateType = "APT:PRE"
        # 수집할 컨테이너
        ult_results = pd.DataFrame()

        # 반복문 시작
        total = len(complexNos)
        trial = 0
        progress = trial/total*100
        if progressChanged : progressChanged.emit(progress)

        for complexNo in complexNos : 
            time.sleep(np.random.randint(delay))
            # 상태표시창
            if progressNameChanged : 
                progressName = self.total_apts_naver_got[self.total_apts_naver_got['complexNo'] == complexNo]['complexName'].values[0]
                progressNameChanged.emit(f"진행 중 : {progressName}")
            
            # (1) 아파트정보 info 가져오기
            info = self.fetch_apt_info(
                complexNo = complexNo
            )

            # (2) 매물 articles 가져오기
            articles = self.fetch_apt_items_mult(
                complexNo = complexNo, 
                realEstateType = realEstateType,
                tradeType = tradeType,
                areaNos = areaNos,
                page = page, 
                rentPriceMin = rentPriceMin,
                rentPriceMax = rentPriceMax,
                priceMin = priceMin,
                priceMax = priceMax,
                areaMin = areaMin,
                areaMax = areaMax,
                oldBuildYears = oldBuildYears,
                recentlyBuildYears = recentlyBuildYears,
                minHouseHoldCount = minHouseHoldCount,
                maxHouseHoldCount = maxHouseHoldCount,)
            
            for col in info.columns :
                articles[col] = info[col].values[0]
                

            ult_results = pd.concat([ult_results, articles])

            # 상태표시창
            if progressChanged :
                trial += 1
                progress = trial/total*100
                progressChanged.emit(progress)
        
        progressChanged.emit(100)
        progressNameChanged.emit('완료')

        cols = list(ult_results.columns)
        for col in cols :
            if col in self.cols_translation :
                cols[cols.index(col)] = self.cols_translation[col]
        ult_results.columns = cols

        return ult_results
            
