import http.client,http.cookies
import json
import ssl

hdrs = {
    'X-Requested-With': 'XMLHttpRequest',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection':'keep-alive',
    'Cookie':r'city_path=blagoveshensk; lang=ru; current_path=88379ae5ff2d38ae1181beabfcbf387272473db86a0e34d454dc26a2b7aca18aa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A150%3A%22%7B%22city%22%3A%22ca246032-0759-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0411%5Cu043b%5Cu0430%5Cu0433%5Cu043e%5Cu0432%5Cu0435%5Cu0449%5Cu0435%5Cu043d%5Cu0441%5Cu043a%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D; _csrf=5ea5d6b638e450252b49fcdff56895e68820f549c7748db26eb227177e9808f9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EC4AA7P39lGIwWfYNHsbpuWL-49rCqAM%22%3B%7D; phonesIdent=176da4faa1b6a0e5d752c8aec743fff5ca68fb668aac58c1415f73627269daefa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22bd46013f-05a5-4b28-adc4-c54d4ca2f65d%22%3B%7D; ipp_uid=1651381466695/swggtdC22GUdReAv/fNj99YoJrGPf4zM8wNzNnA==; rrpvid=743399776403078; rcuid=626e14db5f22670001babaa8; _gcl_au=1.1.706192255.1651381466; tmr_lvid=ec1dacd128a9c363c6d9416525508bce; tmr_lvidTS=1650806553136; cartUserCookieIdent_v3=1872635fb9b26e02e521e9709927301fb56396e175bd6484d583f9d7ff72ec61a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22ed9728d4-b7db-3b96-9ccd-40efff833c22%22%3B%7D; _ym_uid=1650806553541180197; _ym_d=1651381467; _ab_=a3beea7dee9e28b54d17a2a6e78bf152cc96eb64e6509aa9c8c7db3063a14bcba%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22_ab_%22%3Bi%3A1%3Ba%3A1%3A%7Bs%3A12%3A%22price-filter%22%3Bs%3A14%3A%22CATALOG_NORMAL%22%3B%7D%7D; __ttl__widget__ui=1651381519872-07e662fbe49e; PHPSESSID=e91413964b1a8fc5afd15f2f0a513e8b; _gid=GA1.2.362607857.1653641760; _gaexp=GAX1.2.F5r0LoWFQuaGkKl-pfLADg.19228.0; banners-hidden=%7B%220871c555-3ae3-4e57-8b61-59061f84aae2%22%3A%5B%5D%7D; flixgvid=flixb9e6bdb2000000.22003022; rerf=AAAAAGKVqhEVgw0SGsBeAg==; _ym_isad=1; __atuvc=1%7C22; ipp_key=v1654084386105/v33947245ba5adc7a72e273/V0irWJ3sI472eDmg7GzexQ==; _gali=header-logo; dnsauth_csrf=6c447864db21fffb818c675c4ca19dff5890c8214f0c4c0d4c3441439f2d4928a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22e7af4342-10ab-4fa5-a5eb-d22fe2551546%22%3B%7D; _gat=1; _ga_FLS4JETDHW=GS1.1.1654087651.23.1.1654087652.0; _ga=GA1.1.1363537464.1651381466; tmr_detect=1%7C1654087652351; _ym_visorc=b; wishlist-id=1934f4022c31bb89b4cb0f4e76691bcdc786f906e472bd2fd3dc39392315b70ea%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22wishlist-id%22%3Bi%3A1%3Bs%3A36%3A%22eaac2a9f-0067-4c65-94b3-50da4bf15fb5%22%3B%7D; tmr_reqNum=295',
    'Host':'www.dns-shop.ru',
    'Referer':'https://www.dns-shop.ru/',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Linux"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
}

c = http.client.HTTPSConnection('www.dns-shop.ru')
c.request('GET','/',headers=hdrs)
r = c.getresponse()

#print(r.read())
hdrs['Cookie'] = rf"{r.headers['Set-Cookie']}; city_path=blagoveshensk; lang=ru; current_path=88379ae5ff2d38ae1181beabfcbf387272473db86a0e34d454dc26a2b7aca18aa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A150%3A%22%7B%22city%22%3A%22ca246032-0759-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu0411%5Cu043b%5Cu0430%5Cu0433%5Cu043e%5Cu0432%5Cu0435%5Cu0449%5Cu0435%5Cu043d%5Cu0441%5Cu043a%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D; _csrf=5ea5d6b638e450252b49fcdff56895e68820f549c7748db26eb227177e9808f9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22EC4AA7P39lGIwWfYNHsbpuWL-49rCqAM%22%3B%7D; phonesIdent=176da4faa1b6a0e5d752c8aec743fff5ca68fb668aac58c1415f73627269daefa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22bd46013f-05a5-4b28-adc4-c54d4ca2f65d%22%3B%7D; ipp_uid=1651381466695/swggtdC22GUdReAv/fNj99YoJrGPf4zM8wNzNnA==; rrpvid=743399776403078; rcuid=626e14db5f22670001babaa8; _gcl_au=1.1.706192255.1651381466; tmr_lvid=ec1dacd128a9c363c6d9416525508bce; tmr_lvidTS=1650806553136; cartUserCookieIdent_v3=1872635fb9b26e02e521e9709927301fb56396e175bd6484d583f9d7ff72ec61a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22ed9728d4-b7db-3b96-9ccd-40efff833c22%22%3B%7D; _ym_uid=1650806553541180197; _ym_d=1651381467; _ab_=a3beea7dee9e28b54d17a2a6e78bf152cc96eb64e6509aa9c8c7db3063a14bcba%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22_ab_%22%3Bi%3A1%3Ba%3A1%3A%7Bs%3A12%3A%22price-filter%22%3Bs%3A14%3A%22CATALOG_NORMAL%22%3B%7D%7D; __ttl__widget__ui=1651381519872-07e662fbe49e; PHPSESSID=e91413964b1a8fc5afd15f2f0a513e8b; _gid=GA1.2.362607857.1653641760; _gaexp=GAX1.2.F5r0LoWFQuaGkKl-pfLADg.19228.0; banners-hidden=%7B%220871c555-3ae3-4e57-8b61-59061f84aae2%22%3A%5B%5D%7D; flixgvid=flixb9e6bdb2000000.22003022; rerf=AAAAAGKVqhEVgw0SGsBeAg==; _ym_isad=1; __atuvc=1%7C22; ipp_key=v1654084386105/v33947245ba5adc7a72e273/V0irWJ3sI472eDmg7GzexQ==; _gali=header-logo; dnsauth_csrf=6c447864db21fffb818c675c4ca19dff5890c8214f0c4c0d4c3441439f2d4928a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%22e7af4342-10ab-4fa5-a5eb-d22fe2551546%22%3B%7D; _gat=1; _ga_FLS4JETDHW=GS1.1.1654087651.23.1.1654087652.0; _ga=GA1.1.1363537464.1651381466; tmr_detect=1%7C1654087652351; _ym_visorc=b; wishlist-id=1934f4022c31bb89b4cb0f4e76691bcdc786f906e472bd2fd3dc39392315b70ea%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22wishlist-id%22%3Bi%3A1%3Bs%3A36%3A%22eaac2a9f-0067-4c65-94b3-50da4bf15fb5%22%3B%7D; tmr_reqNum=295"

c = http.client.HTTPSConnection('www.dns-shop.ru')
c.request('GET','/',headers=hdrs)
r = c.getresponse()

print(r.headers)