import selenium.webdriver as webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pprint


def get_proxy(proxies):
    print(proxies)
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = proxies
    prox.ftp_proxy = proxies
    prox.ssl_proxy = proxies
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    return capabilities


def get_search_results(search_body, proxy=None):
    url = 'https://www.google.com/'
    options = webdriver.ChromeOptions()
    # Input path to your profile. You can find him by enter "chrome://version/" in your Chrome browser.
    options.add_argument(
        "--user-data-dir=/home/gavnuk/.config/google-chrome/Default")
    chromedriver = '/home/gavnuk/python/Traffic Project/chromedriver'
    if proxy:
        capabilities = get_proxy(proxy)
        browser = webdriver.Chrome(
            executable_path=chromedriver,
            desired_capabilities=capabilities)
    else:
        browser = webdriver.Chrome(
            executable_path=chromedriver,
            chrome_options=options)
    browser.get(url)
    search_element = browser.find_element_by_name('q')
    search_element.send_keys(search_body)
    search_element.submit()
    links = browser.find_elements_by_xpath(
        '//div[@class="rc"]/div/a[1]')
    results = []
    for link in links:
        results.append(link.get_attribute('href'))
    browser.close()
    return results


if __name__ == '__main__':
    search_body = input("Please input, what do you want to search: ")
    results = get_search_results(search_body)
    pprint.pprint(results)
