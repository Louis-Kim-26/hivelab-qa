# unittest 모듈 불러오기
import unittest
# webdriver 모듈을 selenium 패키지에서 불러오기
from selenium import webdriver
# Options 클래스를 selenium.webdriver.chrome.options 모듈에서 불러오기
from selenium.webdriver.chrome.options import Options
# ChromeDriverManager 클래스를 webdriver_manager.chrome 모듈에서 불러오기
from webdriver_manager.chrome import ChromeDriverManager
# 엑셀 사용을 위한 라이브러리
from openpyxl import load_workbook, Workbook

<<<<<<< HEAD
# 커스텀 모듈인 functions 불러오기
import functions
from locator import *

class MainTest(unittest.TestCase):

=======
class MainTest(unittest.TestCase):
>>>>>>> 86c3881c616c96321f8d964384ec4c0a2084ddf0
    # 테스트를 위한 설정
    def setUp(self) -> None:
        #드라이버 설정
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
<<<<<<< HEAD
        # options.add_argument("headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://semdev.hivelab.co.kr:3443/global/galaxy/galaxy-s23/")

        #로그인 설정
        loginPage = functions.LoginPage(self.driver)
        # Dev 이용 시 활성화
        loginPage.dev_login("test", "test")
        # P6 이용 시 활성화
        #loginPage.p6_login("qauser02", "samsungqa")
    
    # Highlights 페이지 컬러칩 클릭 후 스크린샷
    def _test_highlightspage_colorchip_click_screenshot(self):
        highlightsPage = functions.HighlightsPage(self.driver)
        highlightsPage.colorchip_click_screenshot(1)

    # Compare 페이지 컬러칩 클릭 후 스크린샷
    def _test_comparepage_colorchip_click_screenshot(self):
        comparePage = functions.ComparePage(self.driver)
        comparePage.colorchip_click_screenshot(1)

    # Highlights 페이지 카피덱 반영 확인
    def _test_copy_applied(self):
        highlightsPage = functions.HighlightsPage(self.driver)
        excelfile = 'D3_COPY.xlsx'
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.DESIGN_SECTION, 'E19:E21', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.COLORS_SECTION, 'E27:E31', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.ONLINEEXCLUSIVECOLORS_SECTION, 'E39:E43', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.MATERIALS_SECTION, 'E51:E54', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.CAMERA_SECTION, 'E65:E68', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.NIGHTOGRAPHYCAMERA_SECTION, 'E71:E89', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.HIGHRESOLUTION_SECTION, 'E92:E97', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.EXPERTRAW_SECTION, 'E100:E113', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.PERFORMANCE_SECTION, 'E116:E122', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.BATTERY_SECTION, 'E127:E130', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.DISPLAY_SECTION, 'E135:E138', excelfile)
        # highlightsPage.copydeck_text_applied(HighlightsPageLocators.PRODUCTIVITYWITHSPEN_SECTION, 'E142:E145', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.SMARTSWITCH_SECTION, 'E157:E163', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.PCCONTINUITY_SECTION, 'E168:E173', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.ONEUI_SECTION, 'E180:E184', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.SAMSUNGWALLET_SECTION, 'E187:E191', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.SAMSUNGHEALTH_SECTION, 'E195:E201', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.ACCESSORIES_SECTION, 'E205:E207', excelfile)
        highlightsPage.copydeck_text_applied(HighlightsPageLocators.FAQ_SECTION, 'E210:E244', excelfile)
    
    # 최하단 디스클레이머 카피덱 반영 확인
    def _test_bottomDisclaimer_copy_applied(self):
        disclaimer = functions.Common(self.driver)
        excelfile = 'Disclaimer_Result.xlsx'
        sheetname = 'Sheet1'
        disclaimer.copydeck_disclaimerText_applied(excelfile, sheetname)

    # 본문에 모든 각주 클릭하여 이동된 화면 스크린샷 저장
    def _test_disclaimerNumber_click(self):
        disclaimer = functions.Common(self.driver)
        excelfile = 'Disclaimer_Result.xlsx'
        sheetname = 'Sheet1'
        option = '1'
        disclaimer.body_disclaimerNumber_click(excelfile, sheetname, option)

    # 55개국 최하단 각주번호 순서 확인
    def _test_bottomDisclaimerNumber_order_check(self):
        disclaimer = functions.Common(self.driver)
        excelfile = 'Disclaimer_Result.xlsx'
        sheetname = 'Sheet2'
        disclaimer.bottomDisclaimerNumber_order_check(excelfile, sheetname)
=======
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("https://www.samsung.com/uk/smartphones/galaxy-s23-ultra/")
    
    def example1(self):
        print("hello world")
>>>>>>> 86c3881c616c96321f8d964384ec4c0a2084ddf0

    # 테스트 종료 후 드라이버 닫기
    def tearDown(self):
        self.driver.close()
<<<<<<< HEAD
        


if __name__ == "__main__":
    unittest.main()
    
=======

        
if __name__ == "__main__":
    unittest.main()
>>>>>>> 86c3881c616c96321f8d964384ec4c0a2084ddf0
