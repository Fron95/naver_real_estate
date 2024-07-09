import requests
import copy
import time
import json
import pandas as pd
import ast
import os
import re

from module.FileManager import FileManager

class Naver_seoul_land(FileManager) :
    def __init__(self) :
        # 경로들 가져오기
        super().__init__()    
        self.info = pd.DataFrame()
        self.articles = pd.DataFrame()
        self.real_trades =  pd.DataFrame()

    def get_provinces(cortarNo = "0000000000") :
        import requests

        cookies = {
            'NNB': 'X4AQ72WKVDWWK',
            '_ga_EFBDNNF91G': 'GS1.1.1710342642.1.0.1710342642.0.0.0',
            '_ga': 'GA1.2.1432322870.1710342643',
            'ASID': 'de6c8eec0000018e4a6f6df000000057',
            'ba.uuid': '5bc9ada0-1bf0-4056-990b-4664443def51',
            '_ga_6Z6DP60WFK': 'GS1.2.1715222690.1.1.1715222788.22.0.0',
            '_fwb': '466u0Eh7yaUAZ21KUVztYh.1715756440721',
            '_fwb': '177FzAmJvq2ZIC2aaw2bGEA.1716702331931',
            'landHomeFlashUseYn': 'Y',
            'NAC': 'eWSqDYgPae4PA',
            'nhn.realestate.article.rlet_type_cd': 'A01',
            'nhn.realestate.article.trade_type_cd': '""',
            'NACT': '1',
            'page_uid': 'ioW/RdqVOsCssAdy5MKssssssko-448268',
            '_naver_usersession_': 'Mm0sn45xW/KWUfblGsoyNQ==',
            'REALESTATE': 'Mon%20Jul%2008%202024%2014%3A56%3A19%20GMT%2B0900%20(KST)',
            'wcs_bt': '4f99b5681ce60:1720418179',
            'BUC': 'ALuosgpXpFwx53eyy1kI1_LZEbyQrVqjHcIRoktl0zI=',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MjA0MTgxNzksImV4cCI6MTcyMDQyODk3OX0.8tTZNWoblgDsDC_4rL8VCwmQOKqF7LBUr1gKDFp7tPo',
            # 'cookie': 'NNB=X4AQ72WKVDWWK; _ga_EFBDNNF91G=GS1.1.1710342642.1.0.1710342642.0.0.0; _ga=GA1.2.1432322870.1710342643; ASID=de6c8eec0000018e4a6f6df000000057; ba.uuid=5bc9ada0-1bf0-4056-990b-4664443def51; _ga_6Z6DP60WFK=GS1.2.1715222690.1.1.1715222788.22.0.0; _fwb=466u0Eh7yaUAZ21KUVztYh.1715756440721; _fwb=177FzAmJvq2ZIC2aaw2bGEA.1716702331931; landHomeFlashUseYn=Y; NAC=eWSqDYgPae4PA; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; NACT=1; page_uid=ioW/RdqVOsCssAdy5MKssssssko-448268; _naver_usersession_=Mm0sn45xW/KWUfblGsoyNQ==; REALESTATE=Mon%20Jul%2008%202024%2014%3A56%3A19%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1720418179; BUC=ALuosgpXpFwx53eyy1kI1_LZEbyQrVqjHcIRoktl0zI=',
            'priority': 'u=1, i',
            'referer': 'https://new.land.naver.com/search?ms=37.5444094,127.0092879,16&a=APT:ABYG:JGC:OPST:OBYG:PRE:JGB&b=A1:B1:B2&e=RETAIL&f=3000&h=165&i=231&j=30&l=700&ad=true',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        params = {
            'cortarNo': cortarNo,
        }

        response = requests.get('https://new.land.naver.com/api/regions/list', params=params, cookies=cookies, headers=headers)
        return response.json()

    def get_districts(cortarNo = "1100000000") :
        import requests

        cookies = {
            'NNB': 'X4AQ72WKVDWWK',
            '_ga_EFBDNNF91G': 'GS1.1.1710342642.1.0.1710342642.0.0.0',
            '_ga': 'GA1.2.1432322870.1710342643',
            'ASID': 'de6c8eec0000018e4a6f6df000000057',
            'ba.uuid': '5bc9ada0-1bf0-4056-990b-4664443def51',
            '_ga_6Z6DP60WFK': 'GS1.2.1715222690.1.1.1715222788.22.0.0',
            '_fwb': '466u0Eh7yaUAZ21KUVztYh.1715756440721',
            '_fwb': '177FzAmJvq2ZIC2aaw2bGEA.1716702331931',
            'landHomeFlashUseYn': 'Y',
            'NAC': 'eWSqDYgPae4PA',
            'nhn.realestate.article.rlet_type_cd': 'A01',
            'nhn.realestate.article.trade_type_cd': '""',
            'NACT': '1',
            'page_uid': 'ioW/RdqVOsCssAdy5MKssssssko-448268',
            '_naver_usersession_': 'Mm0sn45xW/KWUfblGsoyNQ==',
            'REALESTATE': 'Mon%20Jul%2008%202024%2014%3A56%3A19%20GMT%2B0900%20(KST)',
            'wcs_bt': '4f99b5681ce60:1720418179',
            'BUC': 'ALuosgpXpFwx53eyy1kI1_LZEbyQrVqjHcIRoktl0zI=',
        }

        headers = {
            'accept': '*/*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MjA0MTgxNzksImV4cCI6MTcyMDQyODk3OX0.8tTZNWoblgDsDC_4rL8VCwmQOKqF7LBUr1gKDFp7tPo',
            # 'cookie': 'NNB=X4AQ72WKVDWWK; _ga_EFBDNNF91G=GS1.1.1710342642.1.0.1710342642.0.0.0; _ga=GA1.2.1432322870.1710342643; ASID=de6c8eec0000018e4a6f6df000000057; ba.uuid=5bc9ada0-1bf0-4056-990b-4664443def51; _ga_6Z6DP60WFK=GS1.2.1715222690.1.1.1715222788.22.0.0; _fwb=466u0Eh7yaUAZ21KUVztYh.1715756440721; _fwb=177FzAmJvq2ZIC2aaw2bGEA.1716702331931; landHomeFlashUseYn=Y; NAC=eWSqDYgPae4PA; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; NACT=1; page_uid=ioW/RdqVOsCssAdy5MKssssssko-448268; _naver_usersession_=Mm0sn45xW/KWUfblGsoyNQ==; REALESTATE=Mon%20Jul%2008%202024%2014%3A56%3A19%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1720418179; BUC=ALuosgpXpFwx53eyy1kI1_LZEbyQrVqjHcIRoktl0zI=',
            'priority': 'u=1, i',
            'referer': 'https://new.land.naver.com/search?ms=37.5444094,127.0092879,16&a=APT:ABYG:JGC:OPST:OBYG:PRE:JGB&b=A1:B1:B2&e=RETAIL&f=3000&h=165&i=231&j=30&l=700&ad=true',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        params = {
            'cortarNo': cortarNo,
        }

        response = requests.get('https://new.land.naver.com/api/regions/list', params=params, cookies=cookies, headers=headers)
        return response.json()
    
    def get_dong(self, cortarNo ="1120000000") :
        """구 이하 동이름 가져오기"""
        url = "https://new.land.naver.com/api/regions/list"
        headers = {
            "Cookie": "NNB=FCKCGABYXJBGM; ASID=de6c8eec0000018fe0e3f4d60000005d; NAC=r45BBMwegqUeB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=; nhn.realestate.article.ipaddress_city=1100000000; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; landHomeFlashUseYn=Y; page_uid=iFhWwdqVOsCssiyk1dGsssssskR-268088; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; REALESTATE=Sat%20Jun%2022%202024%2011%3A04%3A44%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1719021885; BUC=fZZA8_pWVcDwPBsokKy-ABqKINLnOafN4vdJCZoIdxs=",
            "Referer": "https://new.land.naver.com/complexes?ms=37.554416,127.0195285,17&a=APT:ABYG:JGC:PRE&e=RETAIL",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        params = {
            "cortarNo": cortarNo
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data

    def get_apts(self, cortarNo = "1120011000") :
        """동 이하 아파트 이름 가져오기"""

        url = "https://new.land.naver.com/api/regions/complexes"
        headers = {
            "Cookie": "NNB=FCKCGABYXJBGM; ASID=de6c8eec0000018fe0e3f4d60000005d; NAC=r45BBMwegqUeB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=; nhn.realestate.article.ipaddress_city=1100000000; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; landHomeFlashUseYn=Y; page_uid=iFhWwdqVOsCssiyk1dGsssssskR-268088; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; REALESTATE=Sat%20Jun%2022%202024%2011%3A04%3A44%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1719021885; BUC=fZZA8_pWVcDwPBsokKy-ABqKINLnOafN4vdJCZoIdxs=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        params = {
            "cortarNo": cortarNo,
            "realEstateType": "APT:PRE",
            "order": ""
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data
    
    def fetch_total_complex_naver_got(self) :
        import time
        import random
        시도단위들 = self.get_provinces()['regionList']

        results = []

        for 시도단위 in 시도단위들 :
            시도단위id = 시도단위['cortarNo']
            시도단위이름 = 시도단위['cortarName']
            time.sleep(random.randint(1, 5))
            자치구들 = self.get_districts(시도단위id)['regionList']
            for 자치구 in 자치구들 : 
                자치구id = 자치구['cortarNo']
                자치구이름 = 자치구['cortarName']
                time.sleep(random.randint(1, 5))
                동읍면들 = self.get_dong(자치구id)['regionList']
                for 동읍면 in 동읍면들 : 
                    동읍면id = 동읍면['cortarNo']
                    동읍면이름 = 동읍면['cortarName']
                    time.sleep(random.randint(1, 5))
                    건물들 = self.get_apts(동읍면id)['complexList']
                    for 건물 in 건물들 : 
                        건물id = 건물['complexNo']
                        건물이름 = 건물['complexName']
                        건물타입 = 건물['realEstateTypeCode']
                        위도 = 건물['latitude']
                        경도 = 건물['longitude']
                        result = (시도단위id, 시도단위이름, 자치구id, 자치구이름, 동읍면id, 동읍면이름, 건물id, 건물타입, 건물이름, 위도, 경도)
                        results.append(result)
                        print(result)

    # 매물조회
    def fetch_apt_items(self, 
                  complexNo = 1147, 
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
                  ) -> json :
        """단일 물건에 대한 매물정보 (호가정보) 가져오기.
        complexNo : 물건id
        tradeType : A1(매매) | B1(전세)
        areaNos : 미기재 시 전체 평수에 대해. 복수 선택은 :으로 이어붙임. (예시. 1:2)
        page : scroll 에 따라 추가정보 호출."""

        url = f"https://new.land.naver.com/api/articles/complex/{complexNo}"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MTkwMjQ2MTEsImV4cCI6MTcxOTAzNTQxMX0.x3jYojHGWB6R2BHcODH8LI4CaxaxyHdcHFucBFCIS0Y",
            "Cookie": "NNB=FCKCGABYXJBGM; ASID=de6c8eec0000018fe0e3f4d60000005d; NAC=r45BBMwegqUeB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=; nhn.realestate.article.ipaddress_city=1100000000; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; landHomeFlashUseYn=Y; page_uid=iFhWwdqVOsCssiyk1dGsssssskR-268088; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; REALESTATE=Sat%20Jun%2022%202024%2011%3A50%3A11%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1719024611; BUC=Dwr5Ph9_Z0h12xcrVOHR5Bz1D2_7_i3ypl51m0vlbfk=",
            "Referer": "https://new.land.naver.com/complexes/1147?ms=37.544731,126.9391515,17&a=APT:PRE&b=A1&e=RETAIL",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        params = {
            "realEstateType": realEstateType,
            "tradeType": tradeType,
            "tag": "::::::::",
            "rentPriceMin": rentPriceMin,
            "rentPriceMax": rentPriceMax,
            "priceMin": priceMin,
            "priceMax": priceMax,
            "areaMin": areaMin,
            "areaMax": areaMax,
            "oldBuildYears": oldBuildYears,
            "recentlyBuildYears": recentlyBuildYears,
            "minHouseHoldCount": minHouseHoldCount,
            "maxHouseHoldCount": maxHouseHoldCount,
            "showArticle": "false",
            "sameAddressGroup": "true",
            "minMaintenanceCost": "",
            "maxMaintenanceCost": "",
            "priceType": "RETAIL",
            "directions": "",
            "page": page,
            "complexNo": complexNo,
            "buildingNos": "",
            "areaNos": areaNos,
            "type": "list",
            "order": "rank"
        }

        response = requests.get(url, headers=headers, params=params)
        result = response.json()
        print("fetch_apt_items", result)

        return result
    
    # 해당 물건에 관한 모든 매물을 가져옴.
    def fetch_apt_items_mult(self, 
                  complexNo = 1147, 
                  realEstateType = "APT:PRE",
                  tradeType = "A1:B1", 
                  areaNos = '', # 미입력시 전체
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
                  sleep = 1,
                #   merge = 'apt'
                ) :
        
        results = []
        is_more_data = True
        howmany = 0
        while is_more_data :
            howmany += 1
            print(howmany)
            try:
                raw_data:json = self.fetch_apt_items(
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
                    maxHouseHoldCount = maxHouseHoldCount,
                )

                result :dict = {}
                is_more_data:bool = raw_data['isMoreData'] 
                for article  in raw_data['articleList']  :
                    for col in self.cols_article :
                        result[col] = article.get(col,"")
                    
                    results.append(copy.deepcopy(result))

            except Exception as e:
                print(f"(1)Error fetching data for complexNo {complexNo} and areaNo {areaNos}: {e}")
                is_more_data = False
            
            page += 1 
            time.sleep(sleep)

            df = pd.DataFrame(results) # 판다스 데이터프레임

            self.articles = df # 인스턴스로 저장
        
        return df # 판다스 데이터프레임
    


    # 단지정보
    def fetch_apt_info(self, complexNo=1147):
        """단지정보 조회"""
        url = f"https://new.land.naver.com/api/complexes/overview/{complexNo}"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MTkwMjUyNDAsImV4cCI6MTcxOTAzNjA0MH0.ld0GtF1d0IZK-kDSqcmFarUz00qPN7g-7i_J5RpgTDY",
            "Cookie": "NNB=FCKCGABYXJBGM; ASID=de6c8eec0000018fe0e3f4d60000005d; NAC=r45BBMwegqUeB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=; nhn.realestate.article.ipaddress_city=1100000000; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; landHomeFlashUseYn=Y; page_uid=iFhWwdqVOsCssiyk1dGsssssskR-268088; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; REALESTATE=Sat%20Jun%2022%202024%2012%3A00%3A40%20GMT%2B0900%20(KST); BUC=RCphcWIuUeinf-MgG0Dke4l0F8fEAWdtIj-xN1lIlTE=; wcs_bt=4f99b5681ce60:1719025241",
            "Priority": "u=1, i",
            "Referer": "https://new.land.naver.com/complexes?ms=37.544731,126.942547,17&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        raw_data = response.json()
        result = self.total_apts_naver_got[self.total_apts_naver_got['complexNo'] == complexNo].copy()

        for col in self.cols_info:         
            try:
                result.at[result.index[0], col] = raw_data.get(col, '')
            except Exception as e:
                print(f"at complexNo: {complexNo}, error occurred with column: {col}")
                continue

        for col in self.cols_pyeongs:
            pyeong_info = {}
            if col in raw_data:
                for pyeong in raw_data[col]:
                    pyeongNo = pyeong['pyeongNo']
                    exclusiveArea = pyeong['exclusiveArea']        
                    pyeong_info[pyeongNo] = exclusiveArea
            str_result = json.dumps(pyeong_info)
            result[col] = str_result

        self.info = result # 인스턴스로 저장
        print("fetch_apt_items", result)
        return result # 판다스 데이터프레임
    
    def merge_info_articles(self, info_data , article_data ) :
        sample_df = pd.DataFrame()
        if (type(info_data) != type(sample_df) ) or (type(article_data) != type(sample_df) ) :
            print('판다스 데이터프레임 데이터타입을 입력해주세요.')
            return
        
        for col in info_data.columns : 
            article_data.loc[:,col] = info_data[col].values[0]
        
        return article_data
        

    # todo : 이 이하는 아직 정리하지 못했다.


    # 실거래가
    def fetch_real_trade(self, complexNo=1147, areaNo=0, db = 'apts') :
        """아파트 특정 평수 실거래가 조회"""

        url = f"https://new.land.naver.com/api/complexes/{complexNo}/prices/real"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MTkwMjYwNzYsImV4cCI6MTcxOTAzNjg3Nn0.-ohhan7oQNVxYwRI3nmwcmE3JeyD3M-HkvPJVShbEu4",
            "Cookie": "NNB=FCKCGABYXJBGM; ASID=de6c8eec0000018fe0e3f4d60000005d; NAC=r45BBMwegqUeB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=; nhn.realestate.article.ipaddress_city=1100000000; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; landHomeFlashUseYn=Y; page_uid=iFhWwdqVOsCssiyk1dGsssssskR-268088; _fwb=61LHhDmgSVSDTIn6beSYcT.1719020991264; REALESTATE=Sat%20Jun%2022%202024%2012%3A14%3A36%20GMT%2B0900%20(KST); wcs_bt=4f99b5681ce60:1719026076; BUC=p18HRKA3Y0XSqzq3tugbJNgv64iu42F1PQpR6QUumsI=",
            "Priority": "u=1, i",
            "Referer": "https://new.land.naver.com/complexes/1147?ms=37.5404435,126.9390494,16&a=APT:ABYG:JGC:PRE&b=A1&e=RETAIL&ad=true",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        params = {
            "complexNo": complexNo,
            "tradeType": "A1",
            "year": 5,
            "priceChartChange": "false",
            "areaNo": areaNo,
            "type": "table"
        }
        response = requests.get(url, headers=headers, params=params)
        raw_data = response.json()['realPriceOnMonthList'] 

        results = []

        try:
            if db == 'apts_info' :
                result = self.apts_info[self.apts_info['complexNo'] == complexNo].iloc[0, :]  # 기존 row의 데이터 포함
            else : 
                result = self.total_apts_naver_got[self.total_apts_naver_got['complexNo'] == complexNo].iloc[0, :]  # 기존 row의 데이터 포함
            result['areaNo'] = areaNo
            

            for month in raw_data :
                for trade in month['realPriceList'] :
                    for col in self.cols_trade:
                        if col in trade:
                            result.loc[:,col] = trade[col]
                    results.append(result.copy())
        except Exception as e:
            print(f"(2)Error fetching data for complexNo {complexNo} and areaNo {areaNo}: {e}")

        return result
    
    def str2dict(self, data) :
        return ast.literal_eval(data)
    
    def get_pyeongs(self, complexNo) :
        pyeongs = self.apts_info[self.apts_info['complexNo'] == complexNo]['pyeongs'].values[0]
        pyeongs = self.str2dict(pyeongs)
        return pyeongs


         

    def fetch_real_trade_mult(self, complexNo, pyeongs,  db = 'apts') : 
        """아파트 단위 실거래가 조사"""
        results = []
        for areaNo, pyeong in pyeongs.items():
            try:
                result = self.fetch_real_trade(complexNo=complexNo, areaNo=areaNo, db=db)
                for idx in range(len(result)) :
                    result[idx] = result[idx]['pyeong'] = pyeong
                results.append(result.copy())
            except Exception as e:
                print(f"(3)Error fetching data for complexNo {complexNo} and areaNo {areaNo}: {e}")
        return results
