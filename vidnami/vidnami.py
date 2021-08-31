import random
import requests
import os
from time import time
from time import sleep



def downloadVideo(link, file_name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    try:
        resp = requests.get(link, headers=headers).content
    except:
        print("Failed to download from {}".format(link))
        return
    if not os.path.exists("downloaded_video"):
        os.mkdir("downloaded_video")
    with open("downloaded_video/" + file_name, mode='wb+') as f:
        f.write(resp)
    print("Video downloaded successfully!")


def login_to_vidnami(driver, vidnami_username, vidnami_password):
    # loading the login page
    print("Opening the login page")
    driver.get("https://app.vidnami.com/")
    # typing the credentials
    driver.find_element_by_name('email').send_keys(vidnami_username)
    driver.find_element_by_name('password').send_keys(vidnami_password)
    # pressing the login button
    driver.find_element_by_class_name(
        'login-button').click()
    print("Login pressed ...")
    print("Waiting for the dashboard to open ...")
    while True:
        try:
            driver.find_element_by_xpath(
                '//a[text()="+ Create a new video"]')
            print("Dashboard page detected!")
            break
        except:
            pass


def start_video_process(driver, one_content):
    driver.get("https://app.vidnami.com/")
    while True:
        timer = int(time())
        while True:
            try:
                sleep(3)
                driver.refresh()
                sleep(3)
                driver.find_element_by_xpath(
                    '//a[text()="+ Create a new video"]').click()
                print("Clicked create a new video button")
                break
            except:
                if int(time()) - timer > 20:
                    print("Refreshing page due to irresponsiveness")
                    driver.refresh()
                    timer = int(time())
                pass
        restart_needed = False
        timer = int(time())
        while True:
            try:
                driver.find_elements_by_class_name('video-wrapper')[2].click()
                print("Clicked 3rd video template")
                break
            except:
                if int(time()) - timer > 20:
                    print("Refreshing page due to irresponsiveness")
                    driver.refresh()
                    restart_needed = True
                    break
                pass
        if not restart_needed:
            break
    while True:
        try:
            driver.find_element_by_xpath(
                '//a[text()="Use This Template"]').click()
            print("Clicked Use this template")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//textarea[@placeholder="Write, or paste your video script here"]').send_keys(one_content)
            print("Typed content")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//span[text()="Create Scenes"]/..').click()
            print("Clicked Create Scenes")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//a[text()="Add Voice Track"]').click()
            print("Clicked Add Voice Track To Your Video")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//span[text()="Auto-voice"]/..').click()
            print("Clicked Auto Voice")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_tag_name('select').click()
            print("Clicked Drop down")
            break
        except:
            pass
    while True:
        try:
            all_voices = driver.find_elements_by_tag_name('option')
            random.choice(all_voices).click()
            print("Clicked a random voice")
            break
        except:
            pass
    while True:
        try:
            all_voices = driver.find_element_by_xpath(
                '//a[text()="Preview Your Video"]').click()
            print("Clicked Preview Your Video")
            break
        except:
            pass
    while True:
        try:
            all_music = driver.find_elements_by_xpath(
                '//span[@class="track-title-text"]')
            random.choice(all_music[1::]).click()
            print("Clicked A random Music")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//a[text()="Looks Good, Continue..."]').click()
            print("Clicked Looks Good, Continue...")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath('//a[text()="change"]').click()
            print("Clicked Change")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath('//input[@value="1080p"]').click()
            print("Clicked 1080p")
            break
        except:
            pass
    while True:
        try:
            driver.find_element_by_xpath(
                '//a[text()="Generate Your Video"]').click()
            print("Clicked Generate Your Video")
            break
        except:
            pass
    while True:
        try:
            download_btn = driver.find_element_by_xpath(
                '//a[text()="Download Your Video"]')
            if download_btn.get_attribute('ng-href').startswith('https://'):
                print("Downloading Video ... Please wait ...")
                downloadVideo(download_btn.get_attribute(
                    'ng-href'), download_btn.get_attribute('download'))
            break
        except:
            pass
