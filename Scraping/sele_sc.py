#-*- coding: utf-8 -*-
# Name : Selenuim based on Scraping, Ref : selenium.dev, https://itjy2.tistory.com/m/141, https://rubber-tree.tistory.com/88
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

def init():
    try:
        # Open and close a browser
        options = ChromeOptions()
        # options.page_load_strategy = 'normal'
        # options.headless = True

        # Use install()
        # service = Service(executable_path=ChromeDriverManager().install())
        # Hard Coded Location
        service = Service(executable_path="./webdriver/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as error:
        print(error)
    finally:
        return driver

# 네이버 로그인 테스트 : send_keys and submit
def naver_login_test(driver=None):
    # 네이버 로그인페이지 주소
    url = "https://nid.naver.com/nidlogin.login"
    user = "alone76"
    password = "!dkffkddl77"

    # Take action on browser
    driver.get(url)
    print("로그인 페이지에 접속하였습니다")

    # 아이디 입력박스에 아이디 입력하기
    driver.find_element(by=By.ID, value="id").send_keys(user)

    # 비밀번호 입력박스에 비빌번호를 입력하기
    driver.find_element(by=By.ID, value="pw").send_keys(password)

    # 아이디와 비밀번호를 전송한다.
    # 로그인창 submit버튼 id값을 찾고 submit()메소드를 통해 값 전송
    driver.find_element(by=By.ID, value="log.login").submit()
    print("로그인에 성공하였습니다.")

# 보배드림 테스트 : BeautifulSoup으로 html 정보 분석
def bobae_test(driver):
    url = "https://m.bobaedream.co.kr"
    driver.get(url)
    x_path = '//*[@id="bobaeHead"]/div[1]/div/div[2]/div[2]/form/div[2]/button/span'
    driver.find_element(by=By.XPATH, value=x_path).click()
    driver.find_element(by=By.NAME, value="keyword").send_keys("카니발")
    driver.find_element(by=By.NAME, value="keyword").submit()
    htlm = driver.page_source
    soup = BeautifulSoup(htlm, 'html.parser')
    search_result = soup.select_one('ul.imgList01')
    commu_list = search_result.select('li > a')

    links = []
    for commu in commu_list[:5]:
        link = commu['href']
        link = url + link
        links.append(link)
    print(links)

if __name__ == '__main__':
    driver = init()

    try:
        # naver_login_test(driver=driver)
        bobae_test(driver=driver)
    except Exception as error:
        print(error)
    finally:
        # time.sleep(3.0)
        driver.quit()