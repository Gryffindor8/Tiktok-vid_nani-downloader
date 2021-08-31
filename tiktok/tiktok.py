

def login_to_tiktok(driver, tiktok_fb_email, tiktok_fb_password):
    driver.get("https://www.tiktok.com/login")
    while True:
        try:
            driver.find_element_by_xpath(
                '//div[text()="Log in with Facebook"]').click()
            print("Clicked login with facebook")
            break
        except:
            pass
    driver.switch_to.window(driver.window_handles[-1])
    while True:
        try:
            driver.find_element_by_id(
                'email').send_keys(tiktok_fb_email)
            print("Typed email")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_id(
                'pass').send_keys(tiktok_fb_password)
            print("Typed password")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_name(
                'login').click()
            print("Clicked login")
            break
        except:
            pass
    driver.switch_to.window(driver.window_handles[0])


def start_tiktok_process(driver):
    pass
