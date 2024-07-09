import pandas as pd
import os
from module.Naver_seoul_land import Naver_seoul_land

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
              progressChanged=None,
              resultReady=None) : 
        
        realEstateType = "APT:PRE"
        # 수집할 컨테이너
        ult_results = pd.DataFrame()

        # 반복문 시작
        total = len(complexNos)
        trial = 0
        for complexNo in complexNos : 
            # 상태표시창
            progress = int(trial/total)
            trial += 1
            if progressChanged : progressChanged.emit(progress)
            
            # (1) 아파트정보 info 가져오기
            info = self.fetch_apt_info(
                complexNo = complexNo
            )

            print(
                "complexNo" , complexNo,
                "realEstateType" , realEstateType,
                "tradeType" , tradeType,
                "areaNos" , areaNos,
                "page" , page,
                "rentPriceMin" , rentPriceMin,
                "rentPriceMax" , rentPriceMax,
                "priceMin" , priceMin,
                "priceMax" , priceMax,
                "areaMin" , areaMin,
                "areaMax" , areaMax,
                "oldBuildYears" , oldBuildYears,
                "recentlyBuildYears" , recentlyBuildYears,
                "minHouseHoldCount" , minHouseHoldCount,
                "maxHouseHoldCount" , maxHouseHoldCount,

            )


            
            # todo : result를 제거해야함
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
            
            print(complexNo,"articles" ,len(articles))
            print(complexNo,"info" ,len(info))
            
            # for col in apt.columns :
            #     articles[col] = apt[col].values[0]
            for col in info.columns :
                articles[col] = info[col].values[0]
                

            ult_results = pd.concat([ult_results, articles])

            print(len(ult_results))

        return ult_results
            
