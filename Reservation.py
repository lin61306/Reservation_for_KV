import pyautogui
import webbrowser 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import time
import schedule

#開啟網頁網址 ex 高榮掛號
url ='https://webreg.vghks.gov.tw/wps/portal/web/onlinereg'

#掛號科別
section_1 = "內科"
section_2 = "免疫風濕科"

#預約資訊
reservation_ID = "E221042318"

#預約區間
reservation_duration = "08/16~08/22"

#預約執行時間
reservation_start_time = "2022-08-08 07:30:00"

#預約醫生
doctor_name = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[3]/table/tbody/tr[3]/td[6]/ul/li[1]/div"

#初診/復診
select_1st_or_2nd = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[3]/table/tbody/tr[2]/td/span[2]/input"

#選擇預約資訊
select_ID = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[3]/table/tbody/tr[3]/td/span[2]/input"

#選取輸入預約資訊欄位
enter_ID_section = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[3]/table/tbody/tr[3]/td/input"

#送出預約資訊
send_reservarion = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[3]/div/a[2]"

#確認預約資訊
confirm_reservarion = "/html/body/div[1]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td/div/form/div[2]/table/tbody/tr[2]/td[2]/div[2]/div/a[2]"

#預約程序排成時間
schedule_start_time = "07:29"

def Reservation_doctor():

    # 使用 Chrome 的 WebDriver
    browser = webdriver.Chrome()
    
    # 開啟 輸入網址
    browser.get(url)

    #選擇科別
    select = browser.find_element(By.LINK_TEXT, section_1)
    select.click()
    
    select = browser.find_element(By.LINK_TEXT, section_2)
    select.click()
    
    #選擇日期
    select = Select(browser.find_element(By.NAME, "ns_Z7_CMRPOKG10GEA60INIP7A8O04T1_weekList"))
    select.select_by_visible_text(reservation_duration)
        
    while True:
        #get time
        #now = (datetime.datetime.now() + datetime.timedelta(seconds=6)).strftime('%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'\r{now}', end = '')
        
        #check booking time
        if (reservation_start_time < now):
            print("\nstart resvation precess")
        
            #refresh chrome
            browser.refresh()
            
            #select docter
            select = browser.find_element(By.XPATH, doctor_name)
            print(select.text)
            select.click() 
            
            #select first/seconds
            select = browser.find_element(By.XPATH, select_1st_or_2nd)
            select.click()
            
            #select ID
            select = browser.find_element(By.XPATH, select_ID)
            select.click()
            
            # enter ID
            select = browser.find_element(By.XPATH, enter_ID_section)
            select.send_keys(reservation_ID)
            
            #send reversation
            select = browser.find_element(By.XPATH, send_reservarion)
            select.click()
            
            #confirm reversation
            select = browser.find_element(By.XPATH, confirm_reservarion)
            select.click()
            
            #end process
            break
        
        time.sleep(0.5)
    # do once
    return schedule.CancelJob

    # 關閉瀏覽器
    # browser.close()

#Reservation_doctor()

schedule.every().day.at(schedule_start_time).do(Reservation_doctor) #部署在每天的XX:YY执行job()函数的任务

while True:

    schedule.run_pending()

    time.sleep(30)