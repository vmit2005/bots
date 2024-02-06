import requests

cookies = {
    'VISITOR_INFO1_LIVE': 'CnWLY-KoWdg',
    '__Secure-3PSID': 'HggEDHnZ1rW2YnF0mJhMw9MuFc03jvujVyYIXF4sC57Ff2HT-guUA-h_xg90kEjrPIbgkQ.',
    '__Secure-3PAPISID': 'SMKebe1c6Cw9uaaL/AmPKC1j_ks4CzSt5U',
    'LOGIN_INFO': 'AFmmF2swRAIgSQl0nmBeITx_O0cqAnC0KO5qMMaPD01cpJXCqans3eoCIF6Mst1vkxFhfgJfzdhURvKgSL7TU_S20F6w0BGNkRaI:QUQ3MjNmdzFEb0ZrcnNKV0R2dVFFamV4R3FHVmxuWGhUSlN1NHZTaEVxSmxNbnl1ZmRJbVZWV0tkaWZjZWdsVFNBUkVUeVJ1MzU4NnhVZkduLWM4ZXNkZkdXNG16SlUzNG9oMWVXaEl0MTVnQnRqYVhzMjB3d213VXZORHNPS3Jpb3l2bFhOeXVndlJLWk9aM3pQWmIyeTlGYlV5VERjZHJR',
    'PREF': 'tz=Europe.Astrakhan&f5=20000',
    'VISITOR_PRIVACY_METADATA': 'CgJSVRICGgA%3D',
    'YSC': 'qFYU0unpFLc',
    'wide': '1',
    '__Secure-1PSIDTS': 'sidts-CjIB3e41he5h-JOSE-sPDmUxwY7w2RMhjvckZPmP9DxFUd3vjDIslFNxLgGIKiJqZ9nU2RAA',
    '__Secure-3PSIDTS': 'sidts-CjIB3e41he5h-JOSE-sPDmUxwY7w2RMhjvckZPmP9DxFUd3vjDIslFNxLgGIKiJqZ9nU2RAA',
    '__Secure-3PSIDCC': 'ACA-OxNbdYju7O1h4wRpaucK087A26tpC9dRe70gta3UxEVcAUYWsM0XE3u4E4G2Z0HKm2DeXVg',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'VISITOR_INFO1_LIVE=CnWLY-KoWdg; __Secure-3PSID=HggEDHnZ1rW2YnF0mJhMw9MuFc03jvujVyYIXF4sC57Ff2HT-guUA-h_xg90kEjrPIbgkQ.; __Secure-3PAPISID=SMKebe1c6Cw9uaaL/AmPKC1j_ks4CzSt5U; LOGIN_INFO=AFmmF2swRAIgSQl0nmBeITx_O0cqAnC0KO5qMMaPD01cpJXCqans3eoCIF6Mst1vkxFhfgJfzdhURvKgSL7TU_S20F6w0BGNkRaI:QUQ3MjNmdzFEb0ZrcnNKV0R2dVFFamV4R3FHVmxuWGhUSlN1NHZTaEVxSmxNbnl1ZmRJbVZWV0tkaWZjZWdsVFNBUkVUeVJ1MzU4NnhVZkduLWM4ZXNkZkdXNG16SlUzNG9oMWVXaEl0MTVnQnRqYVhzMjB3d213VXZORHNPS3Jpb3l2bFhOeXVndlJLWk9aM3pQWmIyeTlGYlV5VERjZHJR; PREF=tz=Europe.Astrakhan&f5=20000; VISITOR_PRIVACY_METADATA=CgJSVRICGgA%3D; YSC=qFYU0unpFLc; wide=1; __Secure-1PSIDTS=sidts-CjIB3e41he5h-JOSE-sPDmUxwY7w2RMhjvckZPmP9DxFUd3vjDIslFNxLgGIKiJqZ9nU2RAA; __Secure-3PSIDTS=sidts-CjIB3e41he5h-JOSE-sPDmUxwY7w2RMhjvckZPmP9DxFUd3vjDIslFNxLgGIKiJqZ9nU2RAA; __Secure-3PSIDCC=ACA-OxNbdYju7O1h4wRpaucK087A26tpC9dRe70gta3UxEVcAUYWsM0XE3u4E4G2Z0HKm2DeXVg',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"116.0.5845.96"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2271 Safari/537.36',
}

response = requests.get('https://www.youtube.com/', cookies=cookies, headers=headers)
with open ('rez.html','w') as file:
    file.write(response.text)