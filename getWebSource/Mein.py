import requests
sites = [
    'http://www.dnes.bg',
    'http://www.vesti.bg',
    'http://www.novini.bg',
    'http://www.actualno.bg',
    'http://www.btvnovinite.bg',
    'http://www.nova.bg',
]
for url in sites:
    index = sites.index(url)
    r = requests.get(url)
    page_source = r.text
    page_source = page_source.split('\n')


    print("\nURL:", url)
    print("--------------------------------------")
    # print the first five lines of the page source
    f = open(str(index) + ".txt", "w")
    for row in page_source[:200]:
        if f.mode == 'w':
            f.write(row)
            f.write('\n')
        print(row)
    f.close()
    print("--------------------------------------")




