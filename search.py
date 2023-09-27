from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
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
    chrome_options.add_argument("--start-maximized")  # 브라우저 최대화

    driver = webdriver.Chrome(options=chrome_options)

    # 1
    # 검색
    # 🚨 Trusted Parts : X 당신이 로봇이 아님을 확인하기 위한 필수 절차입니다. 화면 노출
    # driver.get('https://www.trustedparts.com/en')
    # element = driver.find_element(By.ID, 'searchTextMobileInput')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 X 차단되었습니다. 화면 노출
    # driver.get('https://www.trustedparts.com/en/sign-in')
    # element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/form/div[1]/input')
    # element.send_keys('TEST')
    # element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/form/div[2]/input')
    # element.send_keys('1234')
    # element.send_keys(Keys.RETURN)

    # 2
    # Findchips : O
    # driver.get('https://www.findchips.com/')
    # # 검색
    # element = driver.find_element(By.CLASS_NAME, 'search-field')
    # element.send_keys(search_term)
    # element.send_keys(Keys.RETURN)
    # 로그인 O 아이디 비밀번호 전달 못받음
    # driver.get('https://www.findchips.com/signin')
    # element = driver.find_element(By.ID, 'email-address')
    # element.send_keys('test')
    # element = driver.find_element(By.ID, 'password')
    # element.send_keys('123456')
    # driver.find_element(By.CLASS_NAME, 'signin').click()

    # 3 0
    # 검색
    # Find IC : O
    # driver.get('https://www.findic.kr/')
    # driver.find_element('id', 'search-kw').send_keys('aaa')
    # driver.find_element("id","search-submit").click()
    # 로그인 X 아이디 비밀번호 전달 못받음
    # driver.get('https://www.findic.kr/')
    # driver.maximize_window()
    # driver.find_element(By.CLASS_NAME, 'header_login').click()
    # element = driver.find_element(By.XPATH, '/html/body/div[18]/div[1]/div[2]/div/form/dl[1]/dd/input')
    # element.send_keys('testsetset123214214@naver.com')
    # element = driver.find_element(By.XPATH, '/html/body/div[18]/div[1]/div[2]/div/form/dl[2]/dd/input')
    # element.send_keys('1234')
    # element.send_keys(Keys.RETURN)

    # 4 0
    # 검색
    # Partsner : O
    # driver.get('http://www.partsner.com/')
    # element = driver.find_element(By.ID, 'q_txt')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 O 아이디 비밀번호 전달 못받음
    # driver.get('http://www.partsner.com/member/login_frm.php')
    # element = driver.find_element(By.NAME, 'member_id')
    # element.send_keys('test')
    # element = driver.find_element(By.NAME, 'member_pass')
    # element.send_keys('123')
    # driver.find_element(By.NAME, 'Submit_Mod').click()

    # 5 0
    # 검색
    # 올파츠 : O
    # driver.get('https://www.allparts.co.kr/')
    # element = driver.find_element(By.ID, 'search_part')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 O
    # driver.get('https://www.allparts.co.kr/')
    # element = driver.find_element(By.ID, 'user_id')
    # element.send_keys('mworksk2')
    # element = driver.find_element(By.ID, 'pswd')
    # element.send_keys('tvp5150am1pbsr')
    # element.send_keys(Keys.RETURN)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.presence_of_element_located((By.ID, 'btnHideWeek')))
    # element.click()

    # 6 0
    # 검색
    # Net Components : O
    # driver.get('https://m.netcomponents.com/ko/home/index/')
    # element = driver.find_element(By.CLASS_NAME, 'searched-part')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 O 계정 번호 없음
    # driver.get('https://m.netcomponents.com/ko/account/login')
    # element = driver.find_element(By.ID, 'AccountNumber')
    # element.send_keys('123456')
    # element = driver.find_element(By.ID, 'UserName')
    # element.send_keys('mworksk')
    # element = driver.find_element(By.ID, 'Password')
    # element.send_keys('Tvp5150am1!!')
    # element.send_keys(Keys.RETURN)

    # 7 0
    # 검색
    # IC Source : O (요긴 좀 느림)
    # driver.get('https://icsource.com/Home/Index.aspx')
    # element = driver.find_element(By.ID, 'ctl00_txtSearchTerm')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 -> X 아이디는 정상적으로 들어가는데 비밀번호는 입력이 안됨
    # driver.get('https://icsource.com/Home/Index.aspx')
    # element = driver.find_element(By.XPATH, '/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/input')
    # element.send_keys('mworks')
    # element = driver.find_element(By.XPATH, '/html/body/form/div[6]/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/input[2]')
    # element.send_keys('Tvp5150am1!!')
    # element.send_keys(Keys.RETURN)

    # 8 0
    # 검색
    # The Broker Forum : O
    # driver.get('https://www.brokerforum.com/')
    # element = driver.find_element(By.ID, 'originalFullPartNumber')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 x
    # driver.get('https://www.brokerforum.com/')
    # element = driver.find_element(By.ID, 'mainMenuLoginButton')
    # element.click()
    # element = driver.find_element(By.ID, 'Session_Username')
    # element.send_keys('mworkskap')
    # element = driver.find_element(By.ID, 'Session_Password')
    # element.send_keys('Tvp5150am1!!')
    # element.send_keys(Keys.RETURN)

    # 9 0
    # 검색
    # Digi Parts : O
    # driver.get('https://www.digipart.com/')
    # element = driver.find_element('id', 'term')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN)
    # 로그인 없음

    # 10
    # 검색
    # HK inventory : O
    # driver.get('https://www.hkinventory.com/')
    # driver.find_element('id', 'pnums').send_keys('aaa')
    # driver.find_element(By.CSS_SELECTOR, 'form#frmOfferSearch a').click()
    # 로그인 O (아이디를 무조건 이메일형식으로 작성 필요 아닐시 에러 발생), 아이디 비밀번호 전달 못받음
    # driver.get('https://www.hkinventory.com/')
    # driver.maximize_window()
    # element = driver.find_element(By.ID, 'btn_sign-in')
    # element.click()
    # element = driver.find_element(By.ID, 'username')
    # element.send_keys('tjehdrjs72@naver.com')
    # element = driver.find_element(By.ID, 'passwdInput')
    # element.send_keys('1234')
    # element.send_keys(Keys.RETURN)

    # 11
    # 검색
    # 🚨 AD Web : X 아날로그 디바이스 쿠키 정책 하단 팝업이 노출됨
    # driver.get('https://www.analog.com/en/index.html')
    # driver.find_element('id', 'text-global-search').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'adi-h__search__controls__button--search').click()
    # 로그인 X 아날 로그 디 바이스 쿠키 정책 하단 팝업이 노출됨
    # driver.get('https://analogb2c.b2clogin.com/analogb2c.onmicrosoft.com/b2c_1a_adi_signuporsigninsocial/oauth2/v2.0/authorize?client_id=5a2d9b38-78a8-415d-8565-5229c9ed6ed2&scope=https%3A%2F%2Fanalogb2c.onmicrosoft.com%2Fmyanalog%2Fwrite%20openid%20profile%20offline_access&redirect_uri=https%3A%2F%2Fwww.analog.com%2Fredirect-sso.html&client-request-id=a16432a9-f262-4503-9776-eacc24872a02&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.28.0&client_info=1&code_challenge=n807L_U0p5vFO0JItJCSWPlnIoWpDE3WogkpxY3XSY4&code_challenge_method=S256&nonce=181a94b4-d9ca-4232-9625-0bb4488bac18&state=eyJpZCI6IjAyMWU0OTRjLTg4ZDQtNGUyYi05OTc2LTA0NTZmMWM5MGE2NyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D%7Chttps%3A%2F%2Fmy.analog.com%2Fen%2Fapp&ui_locales=en&startUrl=https://my.analog.com/en/app&cookieAccepted=null')
    # driver.maximize_window()
    # element = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    # element.click()
    # element = driver.find_element(By.ID, 'signInName')
    # element.send_keys('bmselec@bmselec.co.kr')
    # element = driver.find_element(By.ID, 'password')
    # element.send_keys('Tvp5150am1!!')

    # 12
    # 검색
    # Microchip Direct : O
    # driver.get('https://www.microchipdirect.com/')
    # driver.find_element(By.CSS_SELECTOR, 'ul#search-column input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'input-group-text').click()
    # 로그인 X 로그인 창 열리는 과정 까지 성공 아이디 비밀번호 CLASS, ID 확인불가
    # driver.get('https://www.microchipdirect.com/')
    # element = driver.find_element(By.ID, 'loginButton')
    # element.click()

    # 13
    # 검색
    # TI Store : O
    # driver.get('https://www.ti.com/ko-kr/homepage.html')
    # driver.find_element(By.CSS_SELECTOR, 'div#searchboxheader input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'CoveoSearchButton').click()
    # 로그인 O
    # driver.get('https://login.ti.com/as/authorization.oauth2?response_type=code&scope=openid%20email%20profile&client_id=DCIT_ALL_WWW-PROD&state=ASyLnI6G2yrRzK62u53IkdH9_T0&redirect_uri=https%3A%2F%2Fwww.ti.com%2Foidc%2Fredirect_uri%2F&nonce=EB0zAM0EHXE83JqVK1Bagm3Wa84cROtpvDQ23RP6LrY&response_mode=form_post')
    # driver.find_element(By.ID, 'username').send_keys('INFO@OLIVE-EMS.COM')
    # driver.find_element(By.ID, 'nextbutton').click()
    # element = driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/div/div[2]/ti-password/input')
    # element.send_keys('Tvp5150am1!!')
    # element = driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/div/div[2]/div[4]/ti-button')
    # element.click()

    # 14
    # 검색
    # DigiKey : O
    # driver.get('https://www.digikey.kr/')
    # driver.find_element(By.CLASS_NAME, 'header__searchinput').send_keys('aaa')
    # driver.find_element('id', 'header-search-button').click()
    # 로그인 O
    # driver.get('https://auth.digikey.com/as/authorization.oauth2?response_type=code&client_id=pa_wam&redirect_uri=https%3A%2F%2Fwww.digikey.kr%2Fpa%2Foidc%2Fcb&state=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiMnMiLCJzdWZmaXgiOiJmOEx2dEQuMTY5NTM2OTQyMSJ9..d3nF437ZPvg3QdKkDo_K1A.FA3TFUieEfwgAkWAPtVRuFjG7txjlzoieI19X_EpMRw8PnCG0hxhwJJVMlZoZhi1W7uK2bwWEjNWJYpXjFSbwhNDSqbNAFacEKwCCTMQV6lPwG7WIbYQfbOzk017vsOg66YVqocP9a4yj1dYYutPdulzvYBfFe4zJ9Tmpvq7efw.UFToSImrG3hF8eZNousKUw&nonce=kNKpYHE7UPwlT-maF5aS5ltAusqHv5V4IF9z0DX-M64&scope=openid%20address%20email%20phone%20profile&vnd_pi_requested_resource=https%3A%2F%2Fwww.digikey.kr%2FMyDigiKey%2FLogin%3Fsite%3DKR%26lang%3Den%26returnurl%3Dhttps%253A%252F%252Fwww.digikey.kr%252Fen&vnd_pi_application_name=DigikeyProd-Mydigikey')
    # element = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[2]/input')
    # element.send_keys('ekim@microworks.co.kr')
    # element = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/form/div[3]/input')
    # element.send_keys('tvp5150am1!!')
    # element.send_keys(Keys.RETURN)

    # 15
    # 검색
    # Mouser : O
    # driver.get('https://www.mouser.kr/')
    # driver.find_element(By.CLASS_NAME, 'search-input').send_keys('aaa')
    # driver.find_element('id', 'hdrSrch').click()
    # 로그인
    # driver.get('https://www.mouser.kr/MyAccount/MouserLogin?qs=0gZ0gv0KDwsgKSbV9hbU5Q%3d%3d')
    # element = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[1]/input')
    # element.send_keys('Amypark')
    # element = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div/div[1]/div[4]/form/div[2]/input')
    # element.send_keys('tvp5150am1')
    # element.send_keys(Keys.RETURN)

    # 16
    # 검색
    # Arrow : O
    # driver.get('https://www.arrow.com/ko-kr')
    # driver.find_element(By.CLASS_NAME, 'Search-bar-select-input').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME, 'Embedded-search-button').click()
    # 로그인 O
    # driver.get('https://www.arrow.com/ko-kr/login?gotoSplash=true&url=')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[3]/input')
    # element.send_keys('mjang@microworks.co.kr')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[12]/div[3]/div/div/div/form/div[4]/input')
    # element.send_keys('Tvp5150am1pbsr!')
    # element.send_keys(Keys.RETURN)

    # 17
    # 검색
    # Element14 : O
    # driver.get('https://kr.element14.com/')
    # driver.find_element('id', 'SimpleSearchForm_SearchTerm').send_keys('aaa')
    # driver.find_element('id', 'searchMain').click()
    # 로그인
    # driver.get('https://kr.element14.com/webapp/wcs/stores/servlet/LogonForm?myAcctMain=1&catalogId=15001&storeId=10187&langId=-9&URL=https%3A%2F%2Fkr.element14.com%2F')
    # element = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[4]/input')
    # element.send_keys('Steelan')
    # element = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[7]/input')
    # element.send_keys('tvp5150am1')
    # element = driver.find_element(By.XPATH, '/html/body/div[4]/div/main/div[1]/div[1]/form/div[2]/div[2]/div[9]/input')
    # element.click()

    # 18
    # 검색
    # Verical : O
    # driver.get('https://www.verical.com/')
    # element = driver.find_element('id', 'mat-input-1')
    # element.send_keys('aaa')
    # element.send_keys(Keys.RETURN) # enter 이벤트 사용
    # 로그인 O
    # driver.get('https://www.verical.com/sign-in?return=%2F')
    # element = driver.find_element(By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[1]/div/div[1]/div/input')
    # element.send_keys('mjang@microworks.co.kr')
    # element = driver.find_element(By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/sign-in-register-page/div/div/div/mat-tab-group/div/mat-tab-body[1]/div/div/div/sign-in-form/form/mat-form-field[2]/div/div[1]/div/input')
    # element.send_keys('Tvp5150am1pbsr!')
    # element.send_keys(Keys.RETURN)

    # 19
    # 검색
    # Chip One Stop : O
    # driver.get('https://www.chip1stop.com/KOR/ko')
    # driver.find_element('id', 'headerKeywordSearch').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME,'m-header-search-form-btn').click()
    # 로그인 O
    # driver.get('https://www.chip1stop.com/KOR/ko/login')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/form/dl/dd[1]/input')
    # element.send_keys('mworksk')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[1]/form/dl/div/dd/input')
    # element.send_keys('mworksk123')
    # element.send_keys(Keys.RETURN)

    # 20
    # 검색
    # 🚨 LCSC Electronics :  O
    # driver.get('https://www.lcsc.com/')
    # driver.find_element(By.CSS_SELECTOR, "div.v-card__title button").click()
    # driver.find_element('id', 'input-23').send_keys('aaa')
    # driver.find_element(By.CLASS_NAME,"search-btn").click()
    # 로그인 O 아이디 비밀번호 전달 못받음
    # driver.get('https://passport.lcsc.com/#/login?client_id=d21d8e5e1c4b48efb8c538d8fd8530a9&response_type=code&from=lcsc&state=20230922&redirect_url=https%3A%2F%2Fwmsc.lcsc.com%2Fwmsc%2Flogin%2Fcallback%3Fref%3Dhttps%3A%2F%2Fwww.lcsc.com%2F')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/form/div[1]/div/div[1]/input')
    # element.send_keys('TEST@naver.com')
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/form/div[2]/div/div/div/input')
    # element.send_keys('1234')
    # element.send_keys(Keys.RETURN)


    # 탭으로 연속 검색 테스트
    driver.get('https://www.findchips.com/')

    element = driver.find_element(By.CLASS_NAME, 'search-field')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('https://www.findic.kr/')
    driver.find_element(By.ID, 'search-kw').send_keys(search_term)
    driver.find_element(By.ID, 'search-submit').click()
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[2])

    driver.get('http://www.partsner.com/')
    element = driver.find_element(By.ID, 'q_txt')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[3])

    driver.get('https://www.allparts.co.kr/')
    element = driver.find_element(By.ID, 'search_part')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[4])

    driver.get('https://m.netcomponents.com/ko/home/index/')
    element = driver.find_element(By.CLASS_NAME, 'searched-part')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[5])

    driver.get('https://icsource.com/Home/Index.aspx')
    element = driver.find_element(By.ID, 'ctl00_txtSearchTerm')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[6])

    driver.get('https://www.brokerforum.com/')
    element = driver.find_element(By.ID, 'originalFullPartNumber')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[7])

    driver.get('https://www.digipart.com/')
    element = driver.find_element('id', 'term')
    element.send_keys(search_term)
    element.send_keys(Keys.RETURN)
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[8])

    driver.get('https://www.digipart.com/')
    element = driver.find_element(By.XPATH, '/ html / body / div[1] / div / div[1] / form / div / div / input')
    element.send_keys(search_term)
    element = driver.find_element(By.XPATH, '/ html / body / div[1] / div / div[1] / form / div / div / span / button')
    element.click()