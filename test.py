from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/tools/chromedriver.exe")
driver.maximize_window();

driver.get("http://localhost/form.php")
driver.find_element_by_name("nip").send_keys("12345")
driver.find_element_by_name("nama").send_keys("John Wick")
driver.find_element_by_name("nik").send_keys("061120301")
driver.find_element_by_name("alamat").send_keys("Tangerang")
driver.find_element_by_name("perusahaan").send_keys("Fiktif Inc.")
driver.find_element_by_name("tanggal").send_keys("01/01/2021")
driver.find_element_by_name("divisi").send_keys("hrd")
driver.find_element_by_name("posisi").send_keys("staff")
driver.find_element_by_name("gaji").send_keys("1000000")
driver.find_element_by_name("atasan").send_keys("Jack Reacher")
driver.find_element_by_name("submit").click()

driver.close()
driver.quit()
print("Test Selesai ....")