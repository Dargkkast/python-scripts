import httpx

URL = "https://time.is/UTC"

for x in range(5):
    page = httpx.get(URL)
    slices1 = page.text.split("<time", 1)
    slices2 = slices1[1].split("time>", 1)
    time = slices2[0]
    print(time[12:20])
