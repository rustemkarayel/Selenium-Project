from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#LOCATORS
locatorAyakkabı="AYAKKABI"
locatorErkek_ayakkabı="div:nth-of-type(1) > div:nth-of-type(1) > a > img[alt='#']"
locatorDeniz_ayakkabısı="a[title='Baskılı Erkek Deniz Ayakkabısı']  .product-image__image"
locatorBeden=".hidden-mobile [key='4']"
locatorSepete_ekle="a#pd_add_to_cart"
locatorSepet_sayfası=".header-section div:nth-child(3) .dropdown-label"
locatorAnasayfa=".main-header-logo"

driver=webdriver.Chrome()
driver.maximize_window()

#1.https://www.lcwaikiki.com/tr-TR/TR adresine gidin.
driver.get("https://www.lcwaikiki.com/tr-TR/TR")
assert driver.title=="LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki"

#2.Herhangi bir kategori sayfasına gidin.
Ayakkabı=driver.find_element(By.LINK_TEXT,locatorAyakkabı).click()
#driver.execute_script("arguments[0].click()",Ayakkabı)= İsteğe göre click() yerine .execute_script kullanılabilir.
assert driver.title=="kadın erkek cocuk bebek ayakkabı - LC Waikiki"

#3.Herhangi bir ürün sayfasına gidin.
Erkek_ayakkabı=driver.find_element(By.CSS_SELECTOR,locatorErkek_ayakkabı).click()

assert driver.title=="Erkek Ayakkabı, Sneaker, Bot Modelleri - LC Waikiki"

Deniz_ayakkabısı=driver.find_element(By.CSS_SELECTOR,locatorDeniz_ayakkabısı).click()
assert driver.title=="Lacivert Baskılı Erkek Deniz Ayakkabısı - S2HM40Z8-CRP - LC Waikiki"

#4.Ürünü sepete ekleyin.
Beden=driver.find_element(By.CSS_SELECTOR,locatorBeden).click()
assert driver.title=="Lacivert Baskılı Erkek Deniz Ayakkabısı - S2HM40Z8-CRP - LC Waikiki"

Sepete_ekle=driver.find_element(By.CSS_SELECTOR,locatorSepete_ekle).click()
assert driver.title=="Lacivert Baskılı Erkek Deniz Ayakkabısı - S2HM40Z8-CRP - LC Waikiki"

#5.Sepet sayfasına gidin.
Sepet_sayfası=driver.find_element(By.CSS_SELECTOR,locatorSepet_sayfası).click()
assert driver.title=="Sepetim - LC Waikiki"

#6.Anasayfaya geri dönün.
Anasayfa=driver.find_element(By.CSS_SELECTOR,locatorAnasayfa).click()
assert driver.title=="LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki"

print("TEST SUCCESSFUL!")
time.sleep(3)
driver.quit()



