from selenium import webdriver
import smtplib
#get username and password

def check_price():
    #get url
    url = 'https://www.amazon.com/Razer-Nostromo-PC-Gaming-Keypad/dp/B004AM5RB6?pf_rd_p=5cc0ab18-ad5f-41cb-89ad-d43149f4e286&pd_rd_wg=alE3Y&pf_rd_r=69HXQD7TSNJSVNRGBS37&ref_=pd_gw_wish&pd_rd_w=1QP1k&pd_rd_r=22ba38d8-33ea-42f5-940e-d22478b0b75a'
    #create driver using path to chromedriver
    driver = webdriver.Chrome("/Users/titanmitchell/Downloads/chromedriver")
    #open the
    driver.get(url)

    element = driver.find_element_by_id('productTitle')
    price = driver.find_element_by_id('priceblock_ourprice')
    #converted_price = price[1:5]

    price_text = price.text
    element_text = element.text
    converted_price = price_text[1:7]
    converted_price = float(converted_price)

    if(converted_price < 245.0):
        send_mail()

    print(element_text)
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


check_price()
#element_attribute_value = element.get_attribute('value')

#print (element)
#print 'element.text: {0}'.format(element_text)
#print 'element.get_attribute(\'value\'): {0}'.format(element_attribute_value)

#print(element_text)
#print(price_text)
#print(converted_price)
