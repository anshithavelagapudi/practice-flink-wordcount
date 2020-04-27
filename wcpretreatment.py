import json

def wcpretreatment(path):
    #path = r'./Sidewalk_201912.GeoJSON'
    with open(path, 'r') as f:
        jd = json.loads(f.read())
    sb = ''
    for d in jd['features']:
        if not d['properties']['SW_DIRECT'] == None:
            sb += d['properties']['COUNTY_NA'] + d['properties']['VILL_NAME'] + '\n'
    with open('./tmpfile', 'w', encoding='utf-8') as f:
        f.write(sb)
