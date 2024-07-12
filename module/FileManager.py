import os
import pandas as pd
import re

class FileManager:
    def __doc__(self) :
        """
    FileManager 클래스는 부동산 관련 데이터를 관리하는 기능을 제공합니다.
    
    이 클래스는 다음과 같은 기능을 수행합니다:
    1. 경로 설정 및 파일 관리
    2. 지역 설정 및 데이터 로드/저장
    3. 데이터 변환 및 처리
    
    Attributes:
        1. 경로들
        root_path (str): 현재 스크립트의 디렉토리 경로.
        db_folder (str): 데이터베이스 폴더 경로.
        result_folder (str): 결과 폴더 경로.
        total_complex_path (str): 전체 아파트 데이터를 저장하는 파일 경로.
        total_apts (DataFrame): 전체 아파트 데이터.
        apts (DataFrame): 전체 아파트 데이터의 복사본.
        district_dir (str): 특정 지역의 데이터 저장 디렉토리 경로.
        apts_dir (str): 특정 지역의 아파트 데이터 파일 경로.
        article_dir (str): 특정 지역의 매물 데이터 파일 경로.
        trade_dir (str): 특정 지역의 실거래 데이터 파일 경로.
        info_dir (str): 특정 지역의 정보 데이터 파일 경로.

        2. 칼럼들
        apts_info (DataFrame): 특정 지역의 아파트 정보 데이터.
        apts_article (DataFrame): 특정 지역의 매물 데이터.
        apts_trade (DataFrame): 특정 지역의 실거래 데이터.
        cols_article (list): 매물 데이터의 열 이름 리스트.
        cols_trade (list): 실거래 데이터의 열 이름 리스트.
        cols_info (list): 아파트 정보 데이터의 열 이름 리스트.
        cols_pyeongs (list): 평수 데이터의 열 이름 리스트.
        kor_cols_article (list): 매물 데이터의 한글 열 이름 리스트.
        kor_cols_trade (list): 실거래 데이터의 한글 열 이름 리스트.
        kor_cols_info (list): 아파트 정보 데이터의 한글 열 이름 리스트.
        kor_cols_pyeongs (list): 평수 데이터의 한글 열 이름 리스트.

    Methods:
        manage_paths():
            초기 설정을 수행하고 필요한 디렉토리와 파일을 생성합니다.
        
        create_folder_if_not_exists(folder_path):
            지정된 경로에 폴더가 존재하지 않으면 폴더를 생성합니다.
        
        ensure_csv_exists(file_path):
            지정된 경로에 CSV 파일이 존재하지 않으면 빈 DataFrame으로 파일을 생성합니다.
        
        manage_files():
            데이터 파일을 관리하고 필요한 열 이름 리스트를 초기화합니다.
        
        config_district(name_district):
            특정 지역의 데이터를 설정하고, 필요한 파일과 디렉토리를 생성 및 초기화합니다.
        
        renew():
            특정 지역의 매물, 실거래, 정보 데이터를 로드합니다.
        
        save(data, kind):
            데이터를 저장하고, 필요한 경우 가격을 변환합니다.
        
        load(kind):
            지정된 종류의 데이터를 로드합니다.
    """
        
    def __init__(self):
        self.manage_paths()
        self.manage_files()

    def manage_paths(self):
        # 폴더
        
        self.root_path = os.getcwd()   # 루트경로
        self.db_folder = os.path.join(self.root_path, 'DB') # db경로
        self.result_folder = os.path.join(self.root_path, '부동산') #결과물경로
        self.create_folder_if_not_exists(self.db_folder) # 폴더가 존재하지 않으면 생성
        self.create_folder_if_not_exists(self.result_folder) # 폴더가 존재하지 않으면 생성
        
        # 파일
        self.total_complex_path = os.path.join(self.db_folder, 'total_complex_naver_got.csv')  # DB 폴더에 total_apts_naver_got.csv 파일 위치 설정
        self.ensure_csv_exists(self.total_complex_path) # CSV 파일이 존재하지 않으면 빈 DataFrame 생성 후 저장
        
    def create_folder_if_not_exists(self, folder_path):
        """폴더가 존재하지 않으면 생성합니다."""
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
    def ensure_csv_exists(self, file_path):
        """CSV가 존재하지 않으면 생성합니다."""
        if not os.path.exists(file_path):
            # 빈 DataFrame 생성 후 저장
            df = pd.DataFrame()
            df.to_csv(file_path, index=False, encoding='cp949')
    
    def manage_files(self):
        """CSV와 관련한 파일과 칼럼들을 관리합니다."""
        # 3개다 같은겁니다.
        self.total_apts_naver_got = pd.read_csv(self.total_complex_path, encoding='cp949')
        # self.total_apts = pd.read_csv(self.total_complex_path, encoding='cp949') # CSV 파일 읽기
        # self.apts = pd.read_csv(self.total_complex_path, encoding='cp949') # CSV 파일 읽기

        self.cols_article = ['articleNo', 'articleName', 'tradeTypeName', 'areaName', 'dealOrWarrantPrc', 'floorInfo', 'realEstateTypeName',  'isPriceModification',  'area1', 'area2', 'direction', 'articleConfirmYmd', 'articleFeatureDesc', 'tagList', 'buildingName', 'sameAddrCnt', 'sameAddrMaxPrc', 'sameAddrMinPrc']
        self.cols_trade = ['tradeType', 'floor', 'formattedPrice', 'formattedTradeYearMonth']
        self.cols_info = ['complexTypeName', 'complexName', 'totalHouseHoldCount', 'totalDongCount', 'useApproveYmd', 'minArea', 'maxArea']
        self.cols_pyeongs = ['pyeongs']

        self.cols_translation = {
            'provinceName' : '시/도',
            'districtName' : '시/구',
            'dongName' : '동/읍/면',
            'complexName' : '물건이름',
            'realEstateType' : '물건종류',
            'complexLatitude' : '위도',
            'complexLongitude' : '경도',
    'articleNo': '게시글번호',
    'articleName': '게시글이름',
    'realEstateTypeName': '부동산유형',
    'tradeTypeName': '거래유형',
    'floorInfo': '층정보',
    'isPriceModification': '가격수정여부',
    'dealOrWarrantPrc': '거래가격(만원)',
    'areaName': '지역이름',
    'area1': '공급면적',
    'area2': '전용면적',
    'direction': '방향',
    'articleConfirmYmd': '게시글확인날짜',
    'articleFeatureDesc': '게시글특징설명',
    'tagList': '태그목록',
    'buildingName': '건물명',
    'sameAddrCnt': '같은매물개수',
    'sameAddrMaxPrc': '같은매물최고가',
    'sameAddrMinPrc': '같은매convert_price물최저가',
    'pyeongs': '보유평수(제곱미터)',
        'tradeType': '거래유형',
    'floor': '층',
    'formattedPrice': '포맷된가격',
    'formattedTradeYearMonth': '포맷된거래년월',
        'complexTypeName': '단지유형',
    'complexName': '단지명',
    'totalHouseHoldCount': '총세대수',
    'totalDongCount': '총동수',
    'useApproveYmd': '사용승인날짜',
    'minArea': '최소면적',
    'maxArea': '최대면적',
}


    # 이하는 아직 정립되지 않았음.
    def config_district(self, name_district = None):
        """지역설정"""
        self.district_dir = os.path.join(self.root_path, name_district)  # self.base_dir -> self.root_path로 변경
        if not os.path.exists(self.district_dir):
            os.mkdir(self.district_dir)
        self.apts_dir = os.path.join(self.district_dir, f'{name_district}.csv')
        self.article_dir = os.path.join(self.district_dir, f'{name_district}_매물.csv')
        self.trade_dir = os.path.join(self.district_dir, f'{name_district}_실거래.csv')
        self.info_dir = os.path.join(self.district_dir, f'{name_district}_정보.csv')

        total_apts_naver_got = self.total_apts_naver_got[self.total_apts_naver_got['cortarName_district'] == name_district]
        total_apts_naver_got.reset_index(drop=True, inplace=True)
        total_apts_naver_got.to_csv(self.apts_dir, encoding='cp949', index=False)

        self.renew()

    def renew(self):
        try:
            self.apts_info = self.load('info')
        except:
            pass
        try:
            self.apts_article = self.load('article')
        except:
            pass
        try:
            self.apts_trade = self.load('trade')
        except:
            pass
    def convert_price(self, x):
                if isinstance(x, int):
                    return x * 10000 if x <= 100 else x
                if not isinstance(x, str):
                    return x
                try:
                    if '억' in x:
                        parts = x.split('억')
                        if len(parts) == 2 and parts[1].strip():
                            return int(parts[0].strip()) * 10000 + int(re.sub(r'[^\d]', '', parts[1]))
                        else:
                            return int(parts[0].strip()) * 10000
                    else:
                        return int(re.sub(r'[^\d]', '', x))
                except ValueError:
                    return x

    def save(self, data, kind):
        if isinstance(data, dict) and all(isinstance(v, (int, float, str)) for v in data.values()):
            df = pd.DataFrame([data])
        else:
            df = pd.DataFrame(data)

        
        
        if kind == 'article':
            df['floorInfo'] = df['floorInfo'].apply(lambda x: x+'층')
            df['dealOrWarrantPrc'] = df['dealOrWarrantPrc'].apply(self.convert_price)
            df.to_csv(self.article_dir, encoding='cp949', index=False)
        elif kind == 'trade':
            df['formattedPrice'] = df['formattedPrice'].apply(self.convert_price)
            df.to_csv(self.trade_dir, encoding='cp949', index=False)
        elif kind == 'info':
            df.to_csv(self.info_dir, encoding='cp949', index=False)
        else:
            print("kind에 article, trade, info 중 하나를 넣으세요.")
        return df
    
    def load(self, kind):
        if kind == 'article':
            df = pd.read_csv(self.article_dir, encoding='cp949')
        elif kind == 'trade':
            df = pd.read_csv(self.trade_dir, encoding='cp949')
        elif kind == 'info':
            df = pd.read_csv(self.info_dir, encoding='cp949')
        else:
            print("kind에 article, trade, info 중 하나를 넣으세요.")
        return df
