from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time


def perform_search(search_term):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--disable-extensions")
    # 시크릿 창 모드
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=chrome_options)

    # 1
    # 🚨 Trusted Parts : X 당신이 로봇이 아님을 확인하기 위한 필수 절차입니다. 화면 노출
    # driver.get('https://www.trustedparts.com/en')
    # element = driver.find_element(By.ID, 'searchTextMobileInput')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 2
    # Findchips : O
    driver.get('https://www.findchips.com/')

    # 검색어 입력
    element = driver.find_element(By.CLASS_NAME, 'search-field')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)

    # 3
    # Find IC : O
    # driver.get('https://www.findic.kr/')
    # driver.find_element('id', 'search-kw').send_keys('aaa')
    # driver.find_element("id","search-submit").click()

    # 4
    # Partsner : O
    # driver.get('http://www.partsner.com/')
    # element = driver.find_element(By.ID, 'q_txt')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 5
    # 올파츠 : O
    # driver.get('https://www.allparts.co.kr/')
    # element = driver.find_element(By.ID, 'search_part')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 6
    # Net Components : O
    # driver.get('https://m.netcomponents.com/ko/home/index/')
    # element = driver.find_element(By.CLASS_NAME, 'searched-part')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 7
    # IC Source : O (요긴 좀 느림)
    # driver.get('https://icsource.com/Home/Index.aspx')
    # element = driver.find_element(By.ID, 'ctl00_txtSearchTerm')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 8
    # The Broker Forum : O
    # driver.get('https://www.brokerforum.com/')
    # element = driver.find_element(By.ID, 'originalFullPartNumber')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 9
    # Digi Parts : O
    # driver.get('https://www.digipart.com/')
    # element = driver.find_element('id', 'term')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)

    # 10
    # HK inventory : O
    # driver.get('https://www.hkinventory.com/')
    # driver.find_element('id', 'pnums').send_keys('aaa')
    # driver.find_element(By.CSS_SELECTOR, 'form#frmOfferSearch a').click()

    # 11
    # 🚨 AD Web : X 아날로그 디바이스 쿠키 정책 하단 팝업이 노출됨
    # driver.get('https://www.analog.com/en/index.html')
    # driver.find_element('id', 'text-global-search').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'adi-h__search__controls__button--search').click()

    # 12
    # Microchip Direct : O
    # driver.get('https://www.microchipdirect.com/')
    # driver.find_element(By.CSS_SELECTOR, 'ul#search-column input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'input-group-text').click()

    # 13
    # TI Store : O
    # driver.get('https://www.ti.com/ko-kr/homepage.html')
    # driver.find_element(By.CSS_SELECTOR, 'div#searchboxheader input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'CoveoSearchButton').click()

    # 14
    # DigiKey : O
    # driver.get('https://www.digikey.kr/')
    # driver.find_element(By.CLASS_NAME, 'header__searchinput').send_keys('aaa')
    # driver.find_element('id', 'header-search-button').click()

    # 15
    # Mouser : O
    # driver.get('https://www.mouser.kr/')
    # driver.find_element(By.CLASS_NAME, 'search-input').send_keys('aaa')
    # driver.find_element('id', 'hdrSrch').click()

    # 16
    # Arrow : O
    # driver.get('https://www.arrow.com/ko-kr')
    # driver.find_element(By.CLASS_NAME, 'Search-bar-select-input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'Embedded-search-button').click()

    # 17
    # Element14 : O
    # driver.get('https://kr.element14.com/')
    # driver.find_element('id', 'SimpleSearchForm_SearchTerm').send_keys('aaa')
    # driver.find_element('id', 'searchMain').click()

    # 18
    # Verical : O
    # driver.get('https://www.verical.com/')
    # element = driver.find_element('id', 'mat-input-1')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN) # enter 이벤트 사용

    # 19
    # Chip One Stop : O
    # driver.get('https://www.chip1stop.com/KOR/ko')
    # driver.find_element('id', 'headerKeywordSearch').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME,'m-header-search-form-btn').click()

    # 20
    # LCSC Electronics :  O
    # driver.get('https://www.lcsc.com/')
    # driver.find_element(By.CSS_SELECTOR, "div.v-card__title button").click()
    # driver.find_element('id', 'input-23').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME,"search-btn").click()

    # 드라이버 종료
    # driver.quit()
