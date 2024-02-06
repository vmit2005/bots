import requests


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://www.wildberries.ru/brands/gigabyte', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/i/header/logo-v1.svg', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/i/v3/apps/qr.png', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/j/app.min.751e846987147bf6.js', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/j/spa/index.min.787ac5ed32f77e22.js', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 13:52:06 GMT',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = ''

response = requests.get('https://static-basket-01.wb.ru/vol0/r/js-templates-ru-ru.9.3.136.js', params=params, headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 13:52:06 GMT',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = ''

response = requests.get('https://static-basket-01.wb.ru/vol0/r/route-data-ru.9.3.136.js', params=params, headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2211%22%20height%3D%2216%22%20viewBox%3D%220%200%2011%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M10.5385%205.34162C10.5385%207.56736%207.53919%2012.3921%206.06629%2014.6272C5.68463%2015.2063%204.85387%2015.2063%204.47221%2014.6272C2.99931%2012.3921%200%207.56736%200%205.34162C0%202.39153%202.35912%200%205.26925%200C8.17938%200%2010.5385%202.39153%2010.5385%205.34162ZM7.72821%205.34157C7.72821%206.71829%206.62728%207.83433%205.26922%207.83433C3.91116%207.83433%202.81024%206.71829%202.81024%205.34157C2.81024%203.96486%203.91116%202.84882%205.26922%202.84882C6.62728%202.84882%207.72821%203.96486%207.72821%205.34157Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E%0A',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2227%22%20height%3D%2224%22%20viewBox%3D%220%200%2027%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M8.5%201.5C8.5%202.5%206%202.5%204.5%202.5C3%202.5%200.5%202.5%200.5%201.5C0.5%200.5%203%200.5%204.5%200.5C6%200.5%208.5%200.5%208.5%201.5ZM11.8212%2016.119C11.3452%2016.1949%2010.8829%2015.9206%2010.7214%2015.4665L7.48289%206.35812C7.24913%205.70067%207.74355%205.01199%208.44122%205.02324L25.8008%205.30317C26.425%205.31324%2026.8875%205.88644%2026.7654%206.49865L25.4106%2013.2909C25.3288%2013.701%2025.0004%2014.017%2024.5874%2014.0828L11.8212%2016.119ZM13.6523%2021.0331C13.6523%2022.3178%2012.6109%2023.3593%2011.3262%2023.3593C10.0415%2023.3593%209%2022.3178%209%2021.0331C9%2019.7484%2010.0415%2018.707%2011.3262%2018.707C12.6109%2018.707%2013.6523%2019.7484%2013.6523%2021.0331ZM22.957%2023.3593C24.2417%2023.3593%2025.2832%2022.3178%2025.2832%2021.0331C25.2832%2019.7484%2024.2417%2018.707%2022.957%2018.707C21.6723%2018.707%2020.6309%2019.7484%2020.6309%2021.0331C20.6309%2022.3178%2021.6723%2023.3593%2022.957%2023.3593Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E%0A',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2248%22%20height%3D%2224%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M38.7%2013.5l-.2.3a6%206%200%2010-.6.6l-.6.4%204.7%204.5a1%201%200%20001.3-1.3l-4.6-4.5zM34%2014a4.1%204.1%200%20110-8.3%204.1%204.1%200%20010%208.3z%22%20fill%3D%22%23B6B6B6%22%2F%3E%3Cpath%20d%3D%22M14.7%2013.5l-.2.3a6%206%200%2010-.6.6l-.6.4%204.7%204.5a1%201%200%20001.3-1.3l-4.6-4.5zM10%2014a4.1%204.1%200%20110-8.3%204.1%204.1%200%20010%208.3z%22%20fill%3D%22%23fff%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2272%22%20height%3D%2224%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M67.9%2020H52c-.3%200-.6-.1-.8-.3-.2-.2-.3-.5-.3-.8V7.4c0-.3.1-.6.3-.8.2-.2.5-.3.8-.3H55L57.2%204h5.6l2.3%202.3h2.8c.3%200%20.6.1.8.3.2.2.3.5.3.8V19c0%20.3-.1.6-.3.8-.2.2-.5.3-.8.3zm-.6-12h-3l-2.2-2.3H58L55.6%208h-3v10.3h14.7V8zm-7.3.6a3.9%203.9%200%20013.6%202.4%204%204%200%2001-.8%204.4%204%204%200%2001-6.7-2.8c0-1%20.4-2.1%201.1-2.9A4%204%200%200160%208.6zm0%206.3a2.2%202.2%200%20002-1.5%202.3%202.3%200%2000-.4-2.4%202.2%202.2%200%2000-3.9%201.6c0%20.6.3%201.2.7%201.6.4.4%201%20.7%201.6.7z%22%20fill%3D%22%23CB11AB%22%2F%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M43.9%2020H28c-.3%200-.6-.1-.8-.3-.2-.2-.3-.5-.3-.8V7.4c0-.3.1-.6.3-.8.2-.2.5-.3.8-.3H31L33.2%204h5.6l2.3%202.3h2.8c.3%200%20.6.1.8.3.2.2.3.5.3.8V19c0%20.3-.1.6-.3.8-.2.2-.5.3-.8.3zm-.6-12h-3l-2.2-2.3H34L31.6%208h-3v10.3h14.7V8zm-7.3.6a3.9%203.9%200%20013.6%202.4%204%204%200%2001-.8%204.4%204%204%200%2001-6.7-2.8c0-1%20.4-2.1%201.1-2.9A4%204%200%200136%208.6zm0%206.3a2.2%202.2%200%20002-1.5%202.3%202.3%200%2000-.4-2.4%202.2%202.2%200%2000-3.9%201.6c0%20.6.3%201.2.7%201.6.4.4%201%20.7%201.6.7z%22%20fill%3D%22%23999%22%2F%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M19.9%2020H4c-.3%200-.6-.1-.8-.3-.2-.2-.3-.5-.3-.8V7.4c0-.3.1-.6.3-.8.2-.2.5-.3.8-.3H7L9.2%204h5.6l2.3%202.3h2.8c.3%200%20.6.1.8.3.2.2.3.5.3.8V19c0%20.3-.1.6-.3.8-.2.2-.5.3-.8.3zm-.6-12h-3l-2.2-2.3H10L7.6%208h-3v10.3h14.7V8zm-7.3.6a3.9%203.9%200%20013.6%202.4%204%204%200%2001-.8%204.4A4%204%200%20018%2012.6c0-1%20.4-2.1%201.1-2.9A4%204%200%200112%208.6zm0%206.3a2.2%202.2%200%20002-1.5%202.3%202.3%200%2000-.4-2.4%202.2%202.2%200%2000-3.8%201.6c0%20.6.2%201.2.6%201.6.4.4%201%20.7%201.6.7z%22%20fill%3D%22%23fff%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22M16%208A7.999%207.999%200%201%201%200%208h2.002a5.998%205.998%200%201%200%2011.996%200H16z%22%20fill%3D%22%23CB11AB%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2219%22%20height%3D%2223%22%20fill%3D%22none%22%3E%3Cpath%20fill%3D%22%23B3B3B3%22%20d%3D%22M18.602%2017.579a12.268%2012.268%200%200%201-1.213%202.18c-.638.91-1.16%201.538-1.562%201.888-.624.574-1.292.867-2.008.884-.514%200-1.133-.146-1.855-.443-.723-.295-1.388-.441-1.996-.441-.638%200-1.322.146-2.053.441-.733.297-1.323.451-1.774.467-.687.03-1.37-.273-2.054-.908-.435-.38-.98-1.032-1.634-1.955-.7-.986-1.276-2.129-1.727-3.432C.242%2014.852%200%2013.49%200%2012.17c0-1.512.327-2.816.98-3.908a5.754%205.754%200%200%201%202.055-2.079A5.527%205.527%200%200%201%205.813%205.4c.545%200%201.26.168%202.148.5.886.332%201.455.5%201.704.5.186%200%20.818-.196%201.89-.59%201.012-.364%201.867-.515%202.568-.455%201.897.153%203.323.9%204.271%202.249-1.697%201.028-2.536%202.468-2.52%204.316.015%201.44.538%202.637%201.564%203.588.465.442.984.783%201.562%201.025-.125.363-.258.711-.398%201.046ZM14.249.45c0%201.128-.412%202.182-1.233%203.157-.992%201.159-2.19%201.828-3.491%201.723a3.514%203.514%200%200%201-.026-.428c0-1.083.471-2.242%201.308-3.19.418-.48.95-.878%201.595-1.196C13.045.203%2013.653.03%2014.226%200a4.1%204.1%200%200%201%20.023.451Z%22%2F%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22M18.602%2017.579a12.268%2012.268%200%200%201-1.213%202.18c-.638.91-1.16%201.538-1.562%201.888-.624.574-1.292.867-2.008.884-.514%200-1.133-.146-1.855-.443-.723-.295-1.388-.441-1.996-.441-.638%200-1.322.146-2.053.441-.733.297-1.323.451-1.774.467-.687.03-1.37-.273-2.054-.908-.435-.38-.98-1.032-1.634-1.955-.7-.986-1.276-2.129-1.727-3.432C.242%2014.852%200%2013.49%200%2012.17c0-1.512.327-2.816.98-3.908a5.754%205.754%200%200%201%202.055-2.079A5.527%205.527%200%200%201%205.813%205.4c.545%200%201.26.168%202.148.5.886.332%201.455.5%201.704.5.186%200%20.818-.196%201.89-.59%201.012-.364%201.867-.515%202.568-.455%201.897.153%203.323.9%204.271%202.249-1.697%201.028-2.536%202.468-2.52%204.316.015%201.44.538%202.637%201.564%203.588.465.442.984.783%201.562%201.025-.125.363-.258.711-.398%201.046ZM14.249.45c0%201.128-.412%202.182-1.233%203.157-.992%201.159-2.19%201.828-3.491%201.723a3.514%203.514%200%200%201-.026-.428c0-1.083.471-2.242%201.308-3.19.418-.48.95-.878%201.595-1.196C13.045.203%2013.653.03%2014.226%200a4.1%204.1%200%200%201%20.023.451Z%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2220%22%20height%3D%2222%22%20fill%3D%22none%22%3E%3Cpath%20fill%3D%22%23EA4335%22%20d%3D%22M9.311%2010.508.083%2020.177a2.503%202.503%200%200%200%203.665%201.485l10.384-5.914-4.82-5.24Z%22%2F%3E%3Cpath%20fill%3D%22%23FBBC04%22%20d%3D%22m18.643%208.864-4.49-2.572-5.055%204.436%205.075%205.006%204.456-2.544a2.441%202.441%200%200%200%200-4.326h.014Z%22%2F%3E%3Cpath%20fill%3D%22%234285F4%22%20d%3D%22M.083%201.83A2.38%202.38%200%200%200%200%202.461v17.082c0%20.213.028.426.083.633l9.545-9.422L.083%201.83Z%22%2F%3E%3Cpath%20fill%3D%22%2334A853%22%20d%3D%22m9.38%2011.003%204.773-4.71L3.783.35A2.558%202.558%200%200%200%202.495%200%202.503%202.503%200%200%200%20.083%201.822l9.297%209.18Z%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2232%22%20height%3D%2220%22%20fill%3D%22none%22%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22M3.923%2014.004h1.06v5.23h-1.06V17.11H1.527v2.124H.465v-5.23h1.062v2.11h2.396v-2.11ZM9.9%2017c0%20.85-.422%201.304-1.188%201.304-.772%200-1.196-.469-1.196-1.341v-2.955H6.454v2.99c0%201.47.818%202.314%202.243%202.314%201.44%200%202.263-.86%202.263-2.359v-2.95H9.9v2.997Zm12.262.601-1.188-3.596h-.865L18.92%2017.6l-1.156-3.593h-1.13l1.825%205.227h.877l1.19-3.433%201.189%203.433h.884l1.82-5.227h-1.1L22.162%2017.6Zm4.16-.616h1.93v-.951h-1.93v-1.07h2.803v-.954h-3.848v5.223h3.949v-.954h-2.904v-1.294Zm4.168%202.243h1.048v-5.223H30.49v5.223Zm-17.433-1.085-.476%201.09h-1.084l2.305-5.228h.936l2.295%205.228H15.92l-.47-1.09h-2.394Zm.394-.941h1.605l-.803-1.87-.802%201.87ZM15.999%207.347A6.665%206.665%200%200%201%209.342.687h.941a5.725%205.725%200%200%200%205.719%205.718A5.725%205.725%200%200%200%2021.72.687h.941C22.656%204.36%2019.67%207.347%2016%207.347Z%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://a.wb.ru/sdk/sdk.js', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/cargo-delivery-stores-v2.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/stores-data.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/areas/spa/spabrands/areas-spa-spabrands-templates-ru-ru.6b1b873f1eac12fa.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/services/brandConstructorService/brandConstructorService.min.36f8e0d1b7ab47e1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog/xCatalogData.min.c75b926603c934c1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog/queryHelper.min.6bac190a081e7c94.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog_v2/providers/xCatalogProvider.min.58a10e759ee416a0.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog/sorterModel/sorterModel.min.af87823235575d8f.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/s/desktop/style/views/site/catalog-page-v3.min.c7a9112c27101e28.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/customTags/spa.searchTags.min.0bf2b97365588b23.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/customTags/spa.recentItems.min.97be0984d81711d1.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/customTags/spa.tooltip.min.f447a1358f35fc90.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/models/brandCatalog.min.cb79d7b840f935af.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static.wbstatic.net/data/brands/gigabyte.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/subject-base.json', headers=headers)


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://catalog.wb.ru/brands/g/filters?TestGroup=control&TestID=308&appType=1&brand=28928&curr=rub&dest=-1257786&filters=xsubject&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&spp=32',
    headers=headers,
)


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://catalog.wb.ru/brands/g/catalog?TestGroup=control&TestID=308&appType=1&brand=28928&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&sort=popular&spp=32',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/t/jst/catalogcore-ru-ru.3b83e55f37200321.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/customTags/lazyBlockLoader.min.438ac794505afc54.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog_v2/goodsCatalog/catalogCore.min.9e54e1703dfccae3.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/jst/catalogsitepath-ru-ru.1a699b0d0acaab04.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog_v2/shared/catalogSitePath.min.850c101772c6d8f9.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/jst/catalogbrandlikes-ru-ru.b9e9a85c677b029e.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog_v2/brands/catalogBrandLikes.min.0310c4efe8416e89.js',
    headers=headers,
)


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.136',
}

json_data = {
    'statusCode': 200,
    'path': '/brands/gigabyte',
    'queryString': '',
    'urlReferrer': '',
    'deviceId': '4879320731695920388',
    'address': 'Москва',
    'latitude': 55.753737,
    'longitude': 37.6201,
}

response = requests.post('https://www.wildberries.ru/webapi/stats/pageview', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"statusCode":200,"path":"/brands/gigabyte","queryString":"","urlReferrer":"","deviceId":"4879320731695920388","address":"Москва","latitude":55.753737,"longitude":37.6201}'.encode()
#response = requests.post('https://www.wildberries.ru/webapi/stats/pageview', cookies=cookies, headers=headers, data=data)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2215%22%20height%3D%2216%22%20viewBox%3D%220%200%2015%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M14.5732%2010.5742C13.5436%2013.4872%2010.7655%2015.5742%207.49999%2015.5742C4.23445%2015.5742%201.45635%2013.4872%200.426758%2010.5742H14.5732Z%22%20fill%3D%22%23D90012%22%2F%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M14.5732%2010.5742C14.8496%209.79227%2015%208.95081%2015%208.07422C15%207.19763%2014.8496%206.35617%2014.5732%205.57422H0.426764C0.150386%206.35617%200%207.19763%200%208.07422C0%208.95081%200.150386%209.79227%200.426764%2010.5742H14.5732Z%22%20fill%3D%22%230033A0%22%2F%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M14.5732%205.57422H0.426758C1.45635%202.66124%204.23445%200.574219%207.49999%200.574219C10.7655%200.574219%2013.5436%202.66124%2014.5732%205.57422Z%22%20fill%3D%22%23F8F8F8%22%2F%3E%0A%3C%2Fsvg%3E%0A',
    headers=headers,
)


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.136',
}

response = requests.post('https://www.wildberries.ru/webapi/basket/info', cookies=cookies, headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/searchInput/suggestionsHelper.min.81618059c1b89694.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/jst/onlinechatpopuptmpl-ru-ru.a7a295a19079d4b7.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/onlineChat/onlineChatPopup.min.7732ec6acebc47a5.js',
    headers=headers,
)


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.136',
}

data = {
    'brandId': '28928',
}

response = requests.post(
    'https://www.wildberries.ru/webapi/favorites/brand/getvotesbyid',
    cookies=cookies,
    headers=headers,
    data=data,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol1/sellers/brands/F4C9D65A34FEAC8B.webp', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2214%22%20height%3D%2212%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Crect%20width%3D%2214%22%20height%3D%221.714%22%20rx%3D%22.857%22%20fill%3D%22%23000%22%2F%3E%3Crect%20y%3D%2210.286%22%20width%3D%2214%22%20height%3D%221.714%22%20rx%3D%22.857%22%20fill%3D%22%23000%22%2F%3E%3Crect%20y%3D%225.143%22%20width%3D%2214%22%20height%3D%221.714%22%20rx%3D%22.857%22%20fill%3D%22%23000%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2214%22%20fill%3D%22none%22%3E%3Cpath%20fill%3D%22%23242424%22%20fill-rule%3D%22evenodd%22%20d%3D%22M12%20.5c.406%200%20.735.332.735.74v9.732l2.01-2.027a.73.73%200%200%201%201.04%200%20.745.745%200%200%201%200%201.047l-3.265%203.291a.73.73%200%200%201-1.033.007l-.007-.007-3.265-3.291a.745.745%200%200%201%200-1.047.73.73%200%200%201%201.04%200l2.01%202.027V1.24c0-.41.33-.741.735-.741ZM4%2013.5a.738.738%200%200%200%20.735-.74V3.027l2.01%202.027a.73.73%200%200%200%201.04%200%20.745.745%200%200%200%200-1.047L4.52.717a.73.73%200%200%200-1.04%200L.215%204.008a.745.745%200%200%200%200%201.047.73.73%200%200%200%201.04%200l2.01-2.027v9.731c0%20.41.33.741.735.741Z%22%20clip-rule%3D%22evenodd%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M6.5%204a1.5%201.5%200%201%201-3%200%201.5%201.5%200%200%201%203%200Zm1.459.5a3%203%200%200%201-5.918%200H.75a.75.75%200%200%201%200-1.5h1.42a3.001%203.001%200%200%201%205.66%200h7.42a.75.75%200%200%201%200%201.5H7.959Zm5.87%205.5h1.421a.75.75%200%200%201%200%201.5h-1.291a3%203%200%200%201-5.918%200H.75a.75.75%200%200%201%200-1.5h7.42a3.001%203.001%200%200%201%205.66%200ZM12.5%2011a1.5%201.5%200%201%201-3%200%201.5%201.5%200%200%201%203%200Z%22%20fill%3D%22%23000%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2220%22%20height%3D%2220%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M0%2012.727c0-1.004.814-1.818%201.818-1.818h5.455c1.004%200%201.818.814%201.818%201.818v5.455A1.818%201.818%200%200%201%207.273%2020H1.818A1.818%201.818%200%200%201%200%2018.182v-5.455Zm6.364%200a.91.91%200%200%201%20.909.91v3.636a.91.91%200%200%201-.91.909H2.728a.91.91%200%200%201-.909-.91v-3.636a.91.91%200%200%201%20.91-.909h3.636ZM0%201.818C0%20.814.814%200%201.818%200h5.455C8.277%200%209.09.814%209.09%201.818v5.455A1.818%201.818%200%200%201%207.273%209.09H1.818A1.818%201.818%200%200%201%200%207.273V1.818Zm6.364%200a.91.91%200%200%201%20.909.91v3.636a.91.91%200%200%201-.91.909H2.728a.91.91%200%200%201-.909-.91V2.728a.91.91%200%200%201%20.91-.909h3.636ZM12.727%200a1.818%201.818%200%200%200-1.818%201.818v5.455c0%201.004.814%201.818%201.818%201.818h5.455A1.818%201.818%200%200%200%2020%207.273V1.818A1.818%201.818%200%200%200%2018.182%200h-5.455Zm5.455%202.727a.91.91%200%200%200-.91-.909h-3.636a.91.91%200%200%200-.909.91v3.636c0%20.502.407.909.91.909h3.636a.91.91%200%200%200%20.909-.91V2.728ZM10.91%2012.727c0-1.004.813-1.818%201.817-1.818h5.455c1.004%200%201.818.814%201.818%201.818v5.455A1.818%201.818%200%200%201%2018.182%2020h-5.455a1.818%201.818%200%200%201-1.818-1.818v-5.455Zm6.363%200a.91.91%200%200%201%20.909.91v3.636a.91.91%200%200%201-.91.909h-3.636a.91.91%200%200%201-.909-.91v-3.636a.91.91%200%200%201%20.91-.909h3.636Z%22%20fill%3D%22%23000%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2220%22%20height%3D%2220%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M15.9%201.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V1.9a.4.4%200%200%200-.4-.4h-2.2ZM15%200a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V1a1%201%200%200%200-1-1h-4ZM15.9%208.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V8.9a.4.4%200%200%200-.4-.4h-2.2ZM15%207a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V8a1%201%200%200%200-1-1h-4ZM15.9%2015.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4v-2.2a.4.4%200%200%200-.4-.4h-2.2ZM15%2014a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1v-4a1%201%200%200%200-1-1h-4ZM8.9%2015.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4v-2.2a.4.4%200%200%200-.4-.4H8.9ZM8%2014a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1v-4a1%201%200%200%200-1-1H8ZM1.9%2015.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4v-2.2a.4.4%200%200%200-.4-.4H1.9ZM1%2014a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1v-4a1%201%200%200%200-1-1H1ZM1.9%208.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V8.9a.4.4%200%200%200-.4-.4H1.9ZM1%207a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V8a1%201%200%200%200-1-1H1ZM8.9%208.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V8.9a.4.4%200%200%200-.4-.4H8.9ZM8%207a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V8a1%201%200%200%200-1-1H8ZM8.9%201.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V1.9a.4.4%200%200%200-.4-.4H8.9ZM8%200a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V1a1%201%200%200%200-1-1H8ZM1.9%201.5a.4.4%200%200%200-.4.4v2.2c0%20.22.18.4.4.4h2.2a.4.4%200%200%200%20.4-.4V1.9a.4.4%200%200%200-.4-.4H1.9ZM1%200a1%201%200%200%200-1%201v4a1%201%200%200%200%201%201h4a1%201%200%200%200%201-1V1a1%201%200%200%200-1-1H1Z%22%20fill%3D%22%23000%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-12.wb.ru/vol1704/part170432/170432952/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-12.wb.ru/vol1759/part175999/175999904/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-10.wb.ru/vol1352/part135218/135218627/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-10.wb.ru/vol1512/part151219/151219501/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-04.wb.ru/vol554/part55475/55475041/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-11.wb.ru/vol1642/part164223/164223802/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-09.wb.ru/vol1232/part123212/123212754/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-04.wb.ru/vol486/part48658/48658918/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-03.wb.ru/vol396/part39643/39643932/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://basket-05.wb.ru/vol940/part94014/94014311/images/c516x688/1.webp', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/lazyBlockLoader.min.c70ca552331c68fe.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/jst/recommendationslist-ru-ru.ccd4bfb3cd52d1a7.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/recommendations/recommendationsList.min.4324f8f847db23ac.js',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2223%22%20height%3D%2221%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20opacity%3D%22.6%22%20d%3D%22M12.113%2019.777a.98.98%200%200%201-1.246%200C5.327%2015.102.85%2010.749%201.004%206.985c0-2.764%202.093-5.693%205.743-5.973%201.274-.071%203.22.194%204.741%201.542%201.55-1.352%203.65-1.632%204.735-1.537%203.216.187%205.776%202.77%205.776%205.968.082%203.87-4.32%208.125-9.886%2012.792Z%22%20fill%3D%22%23fff%22%2F%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M12.781%2020.524a1.965%201.965%200%200%201-2.563%200c-2.47-2.126-4.956-4.323-6.825-6.462C1.593%2012.002%200%209.6%200%207.066%200%203.057%203.216%200%207.208%200A7.77%207.77%200%200%201%2011.5%201.322%207.77%207.77%200%200%201%2015.792%200C19.784%200%2023%203.057%2023%207.065c0%202.534-1.592%204.937-3.393%206.997-1.869%202.14-4.356%204.336-6.825%206.463ZM11.5%202.512A6.825%206.825%200%200%201%2015.792.955c3.484%200%206.25%202.651%206.25%206.11%200%202.16-1.375%204.331-3.158%206.37-1.817%202.081-4.255%204.237-6.73%206.367a1.003%201.003%200%200%201-1.309%200c-2.474-2.13-4.911-4.286-6.73-6.366C2.334%2011.396.959%209.225.959%207.066c0-3.46%202.765-6.111%206.25-6.111%201.555%200%203.102.574%204.292%201.557ZM7.208%203.92c-1.919%200-3.283%201.395-3.283%203.146%200%20.993.696%202.442%202.425%204.421%201.369%201.566%203.162%203.222%205.15%204.96%201.988-1.738%203.781-3.394%205.15-4.96%201.73-1.979%202.425-3.428%202.425-4.42%200-1.752-1.364-3.147-3.283-3.147-1.053%200-2.134.496-2.81%201.274a1.964%201.964%200%200%201-2.964%200c-.676-.778-1.757-1.274-2.81-1.274ZM11.5%2017.714c-2.237-1.94-4.313-3.816-5.873-5.601-1.746-1.999-2.66-3.68-2.66-5.048%200-2.297%201.812-4.1%204.241-4.1%201.332%200%202.677.616%203.534%201.603a1.004%201.004%200%200%200%201.515%200c.858-.987%202.203-1.604%203.535-1.604%202.429%200%204.242%201.804%204.242%204.101%200%201.368-.915%203.05-2.661%205.048-1.56%201.785-3.636%203.662-5.873%205.6Z%22%20fill%3D%22%23fff%22%2F%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M7.225%203C4.805%203%203%204.796%203%207.082c0%201.36.91%203.034%202.65%205.023%201.554%201.777%203.621%203.644%205.85%205.574%202.229-1.93%204.296-3.797%205.85-5.574C19.09%2010.116%2020%208.443%2020%207.081%2020%204.796%2018.194%203%2015.775%203c-1.326%200-2.666.614-3.52%201.597a1%201%200%200%201-1.51%200C9.892%203.614%208.552%203%207.226%203ZM1%207.082C1%203.639%203.754%201%207.225%201c1.55%200%203.09.572%204.275%201.55A6.802%206.802%200%200%201%2015.775%201C19.245%201%2022%203.639%2022%207.082c0%202.149-1.37%204.31-3.145%206.34-1.81%202.07-4.238%204.215-6.703%206.336a1%201%200%200%201-1.304%200c-2.465-2.12-4.892-4.266-6.703-6.336C2.369%2011.392%201%209.23%201%207.082Z%22%20fill%3D%22%23242424%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2226%22%20height%3D%2226%22%20fill%3D%22%23C8C8D1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20clip-rule%3D%22evenodd%22%20d%3D%22m13.568%201.395%203.052%207.577%207.816.704c.542.05.762.758.35%201.132l-5.927%205.386%201.776%208.012c.123.557-.452.995-.918.699l-6.716-4.248-6.717%204.248c-.467.294-1.04-.144-.918-.7l1.777-8.011-5.93-5.387c-.411-.374-.192-1.083.352-1.132L9.38%208.97l3.053-7.576a.605.605%200%200%201%201.135%200Z%22%20stroke%3D%22%23C8C8D1%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2226%22%20height%3D%2226%22%20fill%3D%22%23FCA95D%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20clip-rule%3D%22evenodd%22%20d%3D%22m13.568%201.395%203.052%207.577%207.816.704c.542.05.762.758.35%201.132l-5.927%205.386%201.776%208.012c.123.557-.452.995-.918.699l-6.716-4.248-6.717%204.248c-.467.294-1.04-.144-.918-.7l1.777-8.011-5.93-5.387c-.411-.374-.192-1.083.352-1.132L9.38%208.97l3.053-7.576a.605.605%200%200%201%201.135%200Z%22%20stroke%3D%22%23FCA95D%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wildberries.ru',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://catalog.wb.ru/brands/g/v4/filters?TestGroup=control&TestID=308&appType=1&brand=28928&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&spp=32',
    headers=headers,
)


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.136',
}

params = {
    'targetUrl': '%2Fbrands%2Fgigabyte',
}

response = requests.get(
    'https://www.wildberries.ru/webapi/spa/brands/metatags/gigabyte',
    params=params,
    cookies=cookies,
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2216%22%20height%3D%2224%22%20viewBox%3D%220%200%2016%2024%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M16%208.10988C16%2011.7119%2010.826%2019.7973%208.79995%2022.8253C8.41424%2023.4018%207.58576%2023.4018%207.20005%2022.8253C5.17398%2019.7973%200%2011.7119%200%208.10988C0%203.63092%203.58172%200%208%200C12.4183%200%2016%203.63092%2016%208.10988ZM11.7333%208.10981C11.7333%2010.2%2010.0618%2011.8944%207.99994%2011.8944C5.93807%2011.8944%204.2666%2010.2%204.2666%208.10981C4.2666%206.01962%205.93807%204.3252%207.99994%204.3252C10.0618%204.3252%2011.7333%206.01962%2011.7333%208.10981Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E%0A',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2219%22%20height%3D%2220%22%20viewBox%3D%220%200%2019%2020%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M14.0207%204.78873C14.0207%207.55869%2011.9361%209.70657%209.50596%209.70657C7.07586%209.70657%204.99117%207.55869%204.99117%204.81221C4.97931%202.10094%207.08777%200%209.50596%200C11.9241%200%2014.0207%202.05399%2014.0207%204.78873ZM0%2018.4977C0%2019.4836%200.64326%2020%202.44201%2020H16.558C18.3567%2020%2019%2019.4836%2019%2018.4977C19%2015.6338%2015.3429%2011.6901%209.50596%2011.6901C3.65705%2011.6901%200%2015.6338%200%2018.4977Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E%0A',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/t/jst/onlinechattmpl-ru-ru.f2f3bcea86579c83.json',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/s/desktop/style/modules/popups/chatSlider.min.3a968b0cffb0deed.css',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/j/swiper.min.13014c18a46a95ce.js', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/customTags/spa.contextMenu.min.0650f8e1a2c788bd.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/onlineChat/onlineChat.min.f6008ab0859767c2.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/t/jst/filteritem-ru-ru.f0768b4effdb7bf6.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/modules/catalog_v2/filtres/filterItem.min.d1cf98b4c1a5a74b.js',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2221%22%20height%3D%2219%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M6.225%202C3.805%202%202%203.796%202%206.082c0%201.36.91%203.034%202.65%205.023%201.554%201.777%203.621%203.644%205.85%205.574%202.229-1.93%204.296-3.797%205.85-5.574C18.09%209.116%2019%207.443%2019%206.081%2019%203.796%2017.194%202%2014.775%202c-1.326%200-2.666.614-3.52%201.597a1%201%200%200%201-1.51%200C8.892%202.614%207.552%202%206.226%202ZM0%206.082C0%202.639%202.754%200%206.225%200c1.55%200%203.09.572%204.275%201.55A6.802%206.802%200%200%201%2014.775%200C18.245%200%2021%202.639%2021%206.082c0%202.149-1.37%204.31-3.145%206.34-1.81%202.07-4.238%204.215-6.703%206.336a1%201%200%200%201-1.304%200c-2.465-2.12-4.892-4.266-6.703-6.336C1.369%2010.392%200%208.23%200%206.082Z%22%20fill%3D%22%23313132%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://static-basket-01.wb.ru/vol0/j/spa/services/storageService.min.150c397a26780ace.js',
    headers=headers,
)


headers = {
    'authority': 'chat-prod.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'basketuid': '7e60deba-9539-4429-89b3-3c8de5e06672',
    'cache-control': 'max-age=0',
    'locale': 'ru',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://chat-prod.wildberries.ru/api/support/v1/unauth/messages', headers=headers)


headers = {
    'authority': 'chat-prod.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'access-control-request-headers': 'basketuid,locale',
    'access-control-request-method': 'GET',
    'cache-control': 'max-age=0',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.options('https://chat-prod.wildberries.ru/api/support/v1/unauth/messages', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M7.361.238a.977.977%200%20011.278%200l7.097%206.377a.755.755%200%20010%201.147.977.977%200%2001-1.278%200L8%201.96%201.542%207.762a.977.977%200%2001-1.277%200%20.755.755%200%20010-1.147L7.36.238z%22%20fill%3D%22%23000%22%2F%3E%3Crect%20width%3D%222%22%20height%3D%2216%22%20rx%3D%221%22%20transform%3D%22matrix(-1%200%200%201%209%200)%22%20fill%3D%22%23000%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{}}'

response = requests.post('https://a.wb.ru/e/pageview', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"country":"ru"}}'

response = requests.post('https://a.wb.ru/e/pageview', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"name":"Gigabyte","id":"38928","link":"https://www.wildberries.ru/brands/gigabyte","country":"ru"}}'

response = requests.post('https://a.wb.ru/e/BrandPage_V', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"name":"Brand","country":"ru"}}'

response = requests.post('https://a.wb.ru/e/Screen_V', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{}}'

response = requests.post('https://a.wb.ru/e/user_id', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Категория","filter_id":"xsubject","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Продавец","filter_id":"ftopsupplier","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Цвет","filter_id":"fcolor","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Срок доставки","filter_id":"fdlvr","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Цена","filter_id":"priceU","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Скидка","filter_id":"discount","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_D', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Категория","filter_id":"xsubject","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_S', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Продавец","filter_id":"ftopsupplier","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_S', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Цвет","filter_id":"fcolor","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_S', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Срок доставки","filter_id":"fdlvr","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_S', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"cp":{"type":"Brand","type_info":"38928","filter_name":"Цена","filter_id":"priceU","parent_id":"0","subject_id":"5320|2009|3128|3274|525|765|519|742|5806|2875|4066|3690|3357|2892|788|593|2290|5174|4075","country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/Filter_S', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x406',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"action":{"type":"view_item_list","currency":"RUB"},"products":[{"utcTime":"2023-09-28 21:38:03","id":"170432952","nm":170432952,"chrt":null,"name":"Ноутбук AORUS 17H","brand":"Gigabyte","price":183218,"inListIndex":1,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"175999904","nm":175999904,"chrt":null,"name":"Ноутбук G5 KF-E3KZ313SD","brand":"Gigabyte","price":83015,"inListIndex":2,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"135218627","nm":135218627,"chrt":null,"name":"Видеокарта PCIE16 GT1030 2GB GDDR5 GV-N1030OC-2GI","brand":"Gigabyte","price":8735,"inListIndex":3,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"15|4.7"},{"utcTime":"2023-09-28 21:38:03","id":"151219501","nm":151219501,"chrt":null,"name":"SSD диск GP-GSM2NE3256GNTD M.2, 256Gb, PCI-E 3.0x4","brand":"Gigabyte","price":1892,"inListIndex":4,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"5320","category3":"6238","coupon":"2|5"},{"utcTime":"2023-09-28 21:38:03","id":"55475041","nm":55475041,"chrt":null,"name":"Внешний бокс с видеокартой NVIDIA GeForce RTX 3090","brand":"Gigabyte","price":279696,"inListIndex":5,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"2|3"},{"utcTime":"2023-09-28 21:38:03","id":"164223802","nm":164223802,"chrt":null,"name":"RTX4090 AERO OC 24GB GDDR6X 384-bit HDMI 3xDP RTL","brand":"Gigabyte","price":186105,"inListIndex":6,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"123212754","nm":123212754,"chrt":null,"name":"Материнская плата Z690 1.1","brand":"Gigabyte","price":19653,"inListIndex":7,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"48658918","nm":48658918,"chrt":null,"name":"SSD накопитель 120 ГБ (GP-GSTFS31120GNTD) SSD SSD 120 GB ОРИ…","brand":"Gigabyte","price":2262,"inListIndex":8,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"5320","category3":"6238","coupon":"1|1"},{"utcTime":"2023-09-28 21:38:03","id":"39643932","nm":39643932,"chrt":null,"name":"GeForce RTX 3080 XTREME EDITION LHR GV-N3080AORUS X-10GD 2.0","brand":"Gigabyte","price":133944,"inListIndex":9,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"3|5"},{"utcTime":"2023-09-28 21:38:03","id":"94014311","nm":94014311,"chrt":null,"name":"Материнская плата H410M H V3 (LGA 1200, 2xDDR4-2933 МГц, 1xP…","brand":"Gigabyte","price":141810,"inListIndex":10,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"173448103","nm":173448103,"chrt":null,"name":"Материнская плата H310M D3H (rev. 1.0)","brand":"Gigabyte","price":6351,"inListIndex":11,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|1"},{"utcTime":"2023-09-28 21:38:03","id":"39991970","nm":39991970,"chrt":null,"name":"RTX 3080 GAMING OC WATERFORCE WB","brand":"Gigabyte","price":153137,"inListIndex":12,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75792090","nm":75792090,"chrt":null,"name":"Материнская плата AMD A520 SAM4 MATX A520M S2H","brand":"Gigabyte","price":7836,"inListIndex":13,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"2|4.5"},{"utcTime":"2023-09-28 21:38:03","id":"40942716","nm":40942716,"chrt":null,"name":"GeForce RTX 3060 EAGLE OC LHR [GV-N3060EAGLE OC-12GD 2.0]","brand":"Gigabyte","price":45782,"inListIndex":14,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"24|4.5"},{"utcTime":"2023-09-28 21:38:03","id":"41159365","nm":41159365,"chrt":null,"name":"Видеокарта Radeon RX 6900XT AMD 16 Gb GDDR6 256 bit RTL [GV-…","brand":"Gigabyte","price":152698,"inListIndex":15,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171262537","nm":171262537,"chrt":null,"name":"Видеокарта GeForce RTX 4090 GAMING OC 24G","brand":"Gigabyte","price":204537,"inListIndex":16,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"40944191","nm":40944191,"chrt":null,"name":"Видеокарта RTX 3080 AORUSX WB [GV-N3080AORUSX WB-10GD 2.0]","brand":"Gigabyte","price":134423,"inListIndex":17,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"42600407","nm":42600407,"chrt":null,"name":"GeForce RTX 3080 AORUS MASTER LHR [GV-N3080AORUS M-10GD 3.0]","brand":"Gigabyte","price":123531,"inListIndex":18,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"2|5"},{"utcTime":"2023-09-28 21:38:03","id":"173726278","nm":173726278,"chrt":null,"name":"G5 MF (MF-E2KZ313SD)","brand":"Gigabyte","price":75232,"inListIndex":19,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"139241818","nm":139241818,"chrt":null,"name":"Модуль памяти GP-GR26C16S8K1HU408 DDR4, 8Gb","brand":"Gigabyte","price":2175,"inListIndex":20,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3357","category3":"6238","coupon":"2|5"},{"utcTime":"2023-09-28 21:38:03","id":"153945083","nm":153945083,"chrt":null,"name":"Материнская плата GA-A520M-DS3H","brand":"Gigabyte","price":8845,"inListIndex":21,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"170432954","nm":170432954,"chrt":null,"name":"Ноутбук AORUS 17X","brand":"Gigabyte","price":268879,"inListIndex":22,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432938","nm":170432938,"chrt":null,"name":"Ноутбук AORUS 17X","brand":"Gigabyte","price":261741,"inListIndex":23,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432950","nm":170432950,"chrt":null,"name":"Ноутбук AORUS 17X","brand":"Gigabyte","price":218910,"inListIndex":24,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432944","nm":170432944,"chrt":null,"name":"Ноутбук AORUS 17X","brand":"Gigabyte","price":211772,"inListIndex":25,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432948","nm":170432948,"chrt":null,"name":"Ноутбук AORUS 17H","brand":"Gigabyte","price":180714,"inListIndex":26,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432947","nm":170432947,"chrt":null,"name":"Ноутбук AORUS 15X","brand":"Gigabyte","price":175829,"inListIndex":27,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432937","nm":170432937,"chrt":null,"name":"Ноутбук AORUS 15X","brand":"Gigabyte","price":156293,"inListIndex":28,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432951","nm":170432951,"chrt":null,"name":"Ноутбук AORUS 15","brand":"Gigabyte","price":140488,"inListIndex":29,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432939","nm":170432939,"chrt":null,"name":"Ноутбук AERO 14 OLED","brand":"Gigabyte","price":134677,"inListIndex":30,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170432942","nm":170432942,"chrt":null,"name":"Ноутбук AERO 14 OLED","brand":"Gigabyte","price":127539,"inListIndex":31,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171541063","nm":171541063,"chrt":null,"name":"Видеокарта RTX4070Ti AORUS ELITE 12GB","brand":"Gigabyte","price":95919,"inListIndex":32,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"174064139","nm":174064139,"chrt":null,"name":"32\\" Монитор AORUS FI32Q X-EK, IPS, 2560x1440, 240Hz","brand":"Gigabyte","price":90010,"inListIndex":33,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2892","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"142043689","nm":142043689,"chrt":null,"name":"Материнская плата Z690M Aorus","brand":"Gigabyte","price":21965,"inListIndex":34,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"40936858","nm":40936858,"chrt":null,"name":"Видеокарта Radeon RX 6900 XT GAMING","brand":"Gigabyte","price":151090,"inListIndex":35,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"158761238","nm":158761238,"chrt":null,"name":"Видеокарта GeForce RTX 3080 GAMING OC LHR 10Gb","brand":"Gigabyte","price":69790,"inListIndex":36,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"62054974","nm":62054974,"chrt":null,"name":"GeForce RTX 3080 EAGLE 12Gb [GV-N3080EAGLE-12GD]","brand":"Gigabyte","price":118993,"inListIndex":37,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"3|2"},{"utcTime":"2023-09-28 21:38:03","id":"55478072","nm":55478072,"chrt":null,"name":"GeForce RTX 3070TI AORUS [GV-N307TAORUS M-8GD]","brand":"Gigabyte","price":76409,"inListIndex":38,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"4|5"},{"utcTime":"2023-09-28 21:38:03","id":"171239617","nm":171239617,"chrt":null,"name":"Блок питания ATX 1000W","brand":"Gigabyte","price":14479,"inListIndex":39,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"70008266","nm":70008266,"chrt":null,"name":"Видеокарта RTX 2060 GV-N2060D6-12GD, 12ГБ","brand":"Gigabyte","price":72462,"inListIndex":40,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"34349348","nm":34349348,"chrt":null,"name":"Материнская плата GigabyteZ490 AORUS XTREME WF Extended ATX…","brand":"Gigabyte","price":88729,"inListIndex":41,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"141332060","nm":141332060,"chrt":null,"name":"Видеокарта PCI-E 4.0 GV-IA380GAMING","brand":"Gigabyte","price":20793,"inListIndex":42,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"1|3"},{"utcTime":"2023-09-28 21:38:03","id":"164137893","nm":164137893,"chrt":null,"name":"RTX4070 WINDFORCE OC 12GB","brand":"Gigabyte","price":64647,"inListIndex":43,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"1|4"},{"utcTime":"2023-09-28 21:38:03","id":"166212757","nm":166212757,"chrt":null,"name":"Видеокарта RTX4070 AORUS MASTER 12GB [GV-N4070AORUS M-12GD]","brand":"Gigabyte","price":78420,"inListIndex":44,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"177229747","nm":177229747,"chrt":null,"name":"Видеокарта PCI-E 4.0 GV-N4060WF2OC-8GD NV RTX4060 8","brand":"Gigabyte","price":39379,"inListIndex":45,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"170246495","nm":170246495,"chrt":null,"name":"Видеокарта GeForce RTX 4060Ti EAGLE OC 8G","brand":"Gigabyte","price":43755,"inListIndex":46,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"171541075","nm":171541075,"chrt":null,"name":"Видеокарта RTX4060 EAGLE OC 8GB","brand":"Gigabyte","price":34786,"inListIndex":47,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"174960824","nm":174960824,"chrt":null,"name":"Видеокарта RTX3050 WINDFORCE OC 8GB","brand":"Gigabyte","price":26565,"inListIndex":48,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"167113090","nm":167113090,"chrt":null,"name":"Материнская плата Z790 AORUS ELITE AX (LGA1700, ATX)","brand":"Gigabyte","price":29088,"inListIndex":49,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"160113104","nm":160113104,"chrt":null,"name":"Материнская плата Z590 UD AC","brand":"Gigabyte","price":15811,"inListIndex":50,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171260685","nm":171260685,"chrt":null,"name":"Монитор 27\\" M27Q P черный IPS LED 0.5ms 16 9","brand":"Gigabyte","price":36071,"inListIndex":51,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2892","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"177229743","nm":177229743,"chrt":null,"name":"Видеокарта PCI-E 4.0 GV-N4060EAGLE OC-8GD NV RTX406","brand":"Gigabyte","price":34842,"inListIndex":52,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171261234","nm":171261234,"chrt":null,"name":"Монитор 23.8\\" G24F 2, 1920х1080","brand":"Gigabyte","price":19671,"inListIndex":53,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2892","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"108408908","nm":108408908,"chrt":null,"name":"Материнская плата B550M DS3H","brand":"Gigabyte","price":8967,"inListIndex":54,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171250143","nm":171250143,"chrt":null,"name":"Материнская плата B550M DS3H Soc-AM4 AMD","brand":"Gigabyte","price":10440,"inListIndex":55,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"2|5"},{"utcTime":"2023-09-28 21:38:03","id":"75792243","nm":75792243,"chrt":null,"name":"Материнская плата H510M H (H510M H)","brand":"Gigabyte","price":8727,"inListIndex":56,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|2"},{"utcTime":"2023-09-28 21:38:03","id":"52587635","nm":52587635,"chrt":null,"name":"Кабель SATA 2 шт. угловой+прямой","brand":"Gigabyte","price":155,"inListIndex":57,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"519","category3":"6258","coupon":"106|4.7"},{"utcTime":"2023-09-28 21:38:03","id":"174531912","nm":174531912,"chrt":null,"name":"Материнская плата Z790 UD AX, LGA 1700, ATX","brand":"Gigabyte","price":25273,"inListIndex":58,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"177229789","nm":177229789,"chrt":null,"name":"Видеокарта PCI-E GV-N1030D5-2GL NV GT1030 2048Mb 64","brand":"Gigabyte","price":7997,"inListIndex":59,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"177229777","nm":177229777,"chrt":null,"name":"Видеокарта PCI-E 4.0 GV-N4060GAMING OC-8GD NV RTX40","brand":"Gigabyte","price":39672,"inListIndex":60,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3274","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160112547","nm":160112547,"chrt":null,"name":"Материнская плата H470M K, LGA1200","brand":"Gigabyte","price":7067,"inListIndex":61,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160112937","nm":160112937,"chrt":null,"name":"Материнская плата Z590 D (Z590 D)","brand":"Gigabyte","price":14164,"inListIndex":62,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171250149","nm":171250149,"chrt":null,"name":"Материнская плата A520M S2H Soc-AM4 AMD","brand":"Gigabyte","price":6960,"inListIndex":63,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"2|5"},{"utcTime":"2023-09-28 21:38:03","id":"172587341","nm":172587341,"chrt":null,"name":"Блок питания GP-P450B, 450Вт, 80+ Bronze","brand":"Gigabyte","price":3847,"inListIndex":64,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75792379","nm":75792379,"chrt":null,"name":"Материнская плата B560M H ( B560M H)","brand":"Gigabyte","price":9542,"inListIndex":65,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"171239604","nm":171239604,"chrt":null,"name":"Блок питания ATX 850W","brand":"Gigabyte","price":12300,"inListIndex":66,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171239602","nm":171239602,"chrt":null,"name":"Блок питания ATX 750W","brand":"Gigabyte","price":10191,"inListIndex":67,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"122334206","nm":122334206,"chrt":null,"name":"Материнская плата B560M H Socket 1200, IntelB560","brand":"Gigabyte","price":7292,"inListIndex":68,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|1"},{"utcTime":"2023-09-28 21:38:03","id":"171910137","nm":171910137,"chrt":null,"name":"Материнская плата A520M K V2, AM4, Micro-ATX","brand":"Gigabyte","price":6230,"inListIndex":69,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75568265","nm":75568265,"chrt":null,"name":"Корпус MIDITOWER ATX W O PSU GB-C200G BLACK","brand":"Gigabyte","price":8011,"inListIndex":70,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"4066","category3":"6238","coupon":"1|4"},{"utcTime":"2023-09-28 21:38:03","id":"163368315","nm":163368315,"chrt":null,"name":"Корпус AORUS C500G ST (28300-AC500-1CKR), Black","brand":"Gigabyte","price":19064,"inListIndex":71,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"4066","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"130883295","nm":130883295,"chrt":null,"name":"Блок питания GP-P850GM","brand":"Gigabyte","price":9644,"inListIndex":72,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"177195486","nm":177195486,"chrt":null,"name":"Материнская плата H610M S2H V2 DDR4 Soc-1700 Intel","brand":"Gigabyte","price":7821,"inListIndex":73,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"176392007","nm":176392007,"chrt":null,"name":"Материнская плата A520M K V2 AM4 mATX","brand":"Gigabyte","price":6786,"inListIndex":74,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171250104","nm":171250104,"chrt":null,"name":"Материнская плата H410M S2H V2 Soc-1200 Intel","brand":"Gigabyte","price":6351,"inListIndex":75,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171260682","nm":171260682,"chrt":null,"name":"Монитор 27\\" G27Q черный IPS LED 1ms 16 9","brand":"Gigabyte","price":29520,"inListIndex":76,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2892","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75792224","nm":75792224,"chrt":null,"name":"Материнская плата (GA-G41M-COMBO)","brand":"Gigabyte","price":7893,"inListIndex":77,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"4|5"},{"utcTime":"2023-09-28 21:38:03","id":"171250152","nm":171250152,"chrt":null,"name":"Материнская плата A620M H SocketAM5 AMD","brand":"Gigabyte","price":11013,"inListIndex":78,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171239618","nm":171239618,"chrt":null,"name":"Блок питания ATX 650W","brand":"Gigabyte","price":6176,"inListIndex":79,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171250174","nm":171250174,"chrt":null,"name":"Материнская плата A520M H Soc-AM4 AMD A520","brand":"Gigabyte","price":7203,"inListIndex":80,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"150449617","nm":150449617,"chrt":null,"name":"Мышь проводная M5050V2-BLACK","brand":"Gigabyte","price":938,"inListIndex":81,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"788","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75792357","nm":75792357,"chrt":null,"name":"Материнская плата AMD B550 SAM4 ATX B550 GAMING X V2","brand":"Gigabyte","price":13665,"inListIndex":82,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171250168","nm":171250168,"chrt":null,"name":"Материнская плата B550M DS3H AC Soc-AM4 AMD","brand":"Gigabyte","price":13920,"inListIndex":83,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"75792230","nm":75792230,"chrt":null,"name":"Материнская плата AMD B550 SAM4 MATX B550M DS3H","brand":"Gigabyte","price":11330,"inListIndex":84,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"171250115","nm":171250115,"chrt":null,"name":"Материнская плата A520M K V2 Soc-AM4 AMD","brand":"Gigabyte","price":7830,"inListIndex":85,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"1|5"},{"utcTime":"2023-09-28 21:38:03","id":"72685879","nm":72685879,"chrt":null,"name":"Блок питания ATX2.31 550W GP-P550B","brand":"Gigabyte","price":6053,"inListIndex":86,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2009","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"174670309","nm":174670309,"chrt":null,"name":"Ноутбук для учебы G5 MF-E2KZ313SD","brand":"Gigabyte","price":76373,"inListIndex":87,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2290","category3":"6238","coupon":"4|3.8"},{"utcTime":"2023-09-28 21:38:03","id":"177172719","nm":177172719,"chrt":null,"name":"Монитор 34\\" M34WQ IPS 2K чер 1ms HDMI DP USB M M HA","brand":"Gigabyte","price":42664,"inListIndex":88,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"2892","category3":"6237","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160113289","nm":160113289,"chrt":null,"name":"Материнская плата Z690 AORUS ULTRA","brand":"Gigabyte","price":36293,"inListIndex":89,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"159980975","nm":159980975,"chrt":null,"name":"Материнская плата B650 AORUS ELITE AX Socket AM5 4xDDR5","brand":"Gigabyte","price":27121,"inListIndex":90,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"74040457","nm":74040457,"chrt":null,"name":"AORUS WATERFORCE 280, 2 x 140mm ARGB Fan, RTL (6) (552367)","brand":"Gigabyte","price":18179,"inListIndex":91,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"5174","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160113013","nm":160113013,"chrt":null,"name":"Материнская плата Z590 GAMING X","brand":"Gigabyte","price":16637,"inListIndex":92,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"171071876","nm":171071876,"chrt":null,"name":"960 ГБ Внутренний SSD, 2.5\\", SATA (GP-GSTFS31960GNTD-V)","brand":"Gigabyte","price":10694,"inListIndex":93,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"5320","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160112730","nm":160112730,"chrt":null,"name":"Материнская плата H610M S2H DDR4, LGA1700","brand":"Gigabyte","price":9192,"inListIndex":94,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160111932","nm":160111932,"chrt":null,"name":"Материнская плата B560M H ( B560M H)","brand":"Gigabyte","price":8680,"inListIndex":95,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160112845","nm":160112845,"chrt":null,"name":"Материнская плата H610M H DDR4, Intel B660, 2xDDR4-3200","brand":"Gigabyte","price":8630,"inListIndex":96,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"159980682","nm":159980682,"chrt":null,"name":"Материнская плата A520 MS 2H","brand":"Gigabyte","price":7811,"inListIndex":97,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"159980765","nm":159980765,"chrt":null,"name":"Материнская плата AMD A520 SAM4 MATX A520M H","brand":"Gigabyte","price":7593,"inListIndex":98,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"160112201","nm":160112201,"chrt":null,"name":"Материнская плата H410M H V2","brand":"Gigabyte","price":6928,"inListIndex":99,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"},{"utcTime":"2023-09-28 21:38:03","id":"159980931","nm":159980931,"chrt":null,"name":"Материнская плата B550M DS3H","brand":"Gigabyte","price":11756,"inListIndex":100,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"|","category":"regular","category2":"3690","category3":"6238","coupon":"0|0"}],"cp":{"page":1,"link":"/brands/gigabyte","goods":431,"country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/ec', params=params, headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.wildberries.ru/manifestv2.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.wildberries.ru/favicon.ico', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.wildberries.ru/android-icon-144x144.png', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3Csvg%20width%3D%2224%22%20height%3D%2226%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M10.12.12c6.408-.918%2012.315%203.51%2013.194%209.891.879%206.381-3.603%2012.299-10.01%2013.217-2.233.32-6.325-.844-6.325-.844l-3.224%202.867-.793-5.76S.438%2015.72.11%2013.338C-.769%206.957%203.713%201.04%2010.12.121zM8.56%2012.214a1.6%201.6%200%2011-3.2%200%201.6%201.6%200%20013.2%200zm3.2%201.6a1.6%201.6%200%20100-3.2%201.6%201.6%200%20000%203.2zm6.4-1.6a1.6%201.6%200%2011-3.2%200%201.6%201.6%200%20013.2%200z%22%20fill%3D%22%23fff%22%2F%3E%3C%2Fsvg%3E',
    headers=headers,
)


cookies = {
    '_wbauid': '4879320731695920388',
    'BasketUID': '7e60deba-9539-4429-89b3-3c8de5e06672',
    '__wba_s': '1',
    '___wbu': '48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389',
    '___wbs': '3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': '_wbauid=4879320731695920388; BasketUID=7e60deba-9539-4429-89b3-3c8de5e06672; __wba_s=1; ___wbu=48d1a453-6a47-4953-b34a-447e81d1e3e4.1695920389; ___wbs=3cc188ec-b2e0-4d89-931b-8425d04fe8ab.1695920389',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.136',
}

json_data = {
    'pageViewGuid': '22f60db6-7bd7-48af-aac0-fbad966b01e9',
    'path': '/brands/gigabyte',
    'queryString': '',
    'urlReferrer': '',
    'deviceId': '4879320731695920388',
    'statisticEvents': [
        {
            'EventName': 'CTO',
            'EventParams': [
                {
                    'ParamName': 'LCTN',
                    'ParamValue': None,
                },
                {
                    'ParamName': 'LONG',
                    'ParamValue': '37.6201',
                },
                {
                    'ParamName': 'LAT',
                    'ParamValue': '55.753737',
                },
                {
                    'ParamName': 'WUId',
                    'ParamValue': '0',
                },
                {
                    'ParamName': 'MId',
                    'ParamValue': None,
                },
                {
                    'ParamName': 'SORT',
                    'ParamValue': 'popular',
                },
                {
                    'ParamName': 'Page',
                    'ParamValue': '1',
                },
                {
                    'ParamName': 'PS',
                    'ParamValue': '100',
                },
                {
                    'ParamName': 'CS',
                    'ParamValue': 'c516x688',
                },
                {
                    'ParamName': 'TURL',
                    'ParamValue': '/brands/gigabyte',
                },
                {
                    'ParamName': 'NMS',
                    'ParamValue': '[170432952,175999904,135218627,151219501,55475041,164223802,123212754,48658918,39643932,94014311,173448103,39991970,75792090,40942716,41159365,171262537,40944191,42600407,173726278,139241818,153945083,170432954,170432938,170432950,170432944,170432948,170432947,170432937,170432951,170432939,170432942,171541063,174064139,142043689,40936858,158761238,62054974,55478072,171239617,70008266,34349348,141332060,164137893,166212757,177229747,170246495,171541075,174960824,167113090,160113104,171260685,177229743,171261234,108408908,171250143,75792243,52587635,174531912,177229789,177229777,160112547,160112937,171250149,172587341,75792379,171239604,171239602,122334206,171910137,75568265,163368315,130883295,177195486,176392007,171250104,171260682,75792224,171250152,171239618,171250174,150449617,75792357,171250168,75792230,171250115,72685879,174670309,177172719,160113289,159980975,74040457,160113013,171071876,160112730,160111932,160112845,159980682,159980765,160112201,159980931]',
                },
            ],
        },
    ],
}

response = requests.post('https://www.wildberries.ru/webapi/stats/events', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageViewGuid":"22f60db6-7bd7-48af-aac0-fbad966b01e9","path":"/brands/gigabyte","queryString":"","urlReferrer":"","deviceId":"4879320731695920388","statisticEvents":[{"EventName":"CTO","EventParams":[{"ParamName":"LCTN","ParamValue":null},{"ParamName":"LONG","ParamValue":"37.6201"},{"ParamName":"LAT","ParamValue":"55.753737"},{"ParamName":"WUId","ParamValue":"0"},{"ParamName":"MId","ParamValue":null},{"ParamName":"SORT","ParamValue":"popular"},{"ParamName":"Page","ParamValue":"1"},{"ParamName":"PS","ParamValue":"100"},{"ParamName":"CS","ParamValue":"c516x688"},{"ParamName":"TURL","ParamValue":"/brands/gigabyte"},{"ParamName":"NMS","ParamValue":"[170432952,175999904,135218627,151219501,55475041,164223802,123212754,48658918,39643932,94014311,173448103,39991970,75792090,40942716,41159365,171262537,40944191,42600407,173726278,139241818,153945083,170432954,170432938,170432950,170432944,170432948,170432947,170432937,170432951,170432939,170432942,171541063,174064139,142043689,40936858,158761238,62054974,55478072,171239617,70008266,34349348,141332060,164137893,166212757,177229747,170246495,171541075,174960824,167113090,160113104,171260685,177229743,171261234,108408908,171250143,75792243,52587635,174531912,177229789,177229777,160112547,160112937,171250149,172587341,75792379,171239604,171239602,122334206,171910137,75568265,163368315,130883295,177195486,176392007,171250104,171260682,75792224,171250152,171239618,171250174,150449617,75792357,171250168,75792230,171250115,72685879,174670309,177172719,160113289,159980975,74040457,160113013,171071876,160112730,160111932,160112845,159980682,159980765,160112201,159980931]"}]}]}'
#response = requests.post('https://www.wildberries.ru/webapi/stats/events', cookies=cookies, headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/t/jst/menutoptmpl-ru-ru.2ccf4a9052db985c.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:34:55 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-v6.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:34:55 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-v6.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:34:58 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-fr-v6.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:40:18 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-v6.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:40:21 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-fr-v6.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/cargo-delivery-stores-v2.json', headers=headers)


headers = {
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/stores-data.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:45:41 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-v6.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:45:44 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-fr-v6.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:51:05 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-v6.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Thu, 28 Sep 2023 17:51:08 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-fr-v6.json', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'static-basket-01.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 28 Sep 2023 12:33:04 GMT',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://static-basket-01.wb.ru/vol0/data/settings-front-ru.json.hash', headers=headers)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x683',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"action":{"type":"view_item_in_list","currency":"RUB"},"products":[{"utcTime":"2023-09-28 22:06:29","id":"170432952","nm":170432952,"chrt":null,"name":"Ноутбук AORUS 17H","brand":"Gigabyte","price":183218,"inListIndex":1,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"1312586|","category":"regular","category2":"2290","category3":"6238","coupon":"0|0"}],"cp":{"country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/ec', params=params, headers=headers, data=data)


headers = {
    'authority': 'a.wb.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/brands/gigabyte',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

params = {
    't': 'Gigabyte - каталог 2022-2023 в интернет магазине WildBerries.ru',
    'u': 'https://www.wildberries.ru/brands/gigabyte',
    'cid': '4',
    's': '1920x1080x24',
    'w': '1920x683',
    'user_id': '4879320731695920388',
    'vbn': '324',
}

data = '{"action":{"type":"view_item_in_list","currency":"RUB"},"products":[{"utcTime":"2023-09-28 22:06:29","id":"175999904","nm":175999904,"chrt":null,"name":"Ноутбук G5 KF-E3KZ313SD","brand":"Gigabyte","price":83015,"inListIndex":2,"listName":"SNS||popular|видеокарта|preset=600000946|preset|","variant":"","quantity":1,"affiliation":"796975|","category":"regular","category2":"2290","category3":"6238","coupon":"1|5"}],"cp":{"country":"ru"}}'.encode()

response = requests.post('https://a.wb.ru/e/ec', params=params, headers=headers, data=data)

print(response.status_code)
print(response.text)
