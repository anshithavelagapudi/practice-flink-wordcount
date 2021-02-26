import json

def wcpretreatment(path):
    #path = r'./Sidewalk_201912.GeoJSON'
    with open(path, 'r') as f:
        jd = json.loads(f.read())
    sb = ''
    for d in jd['vaccinations']:
        if not d['properties']['date'] == None:
            sb += d['properties']['daily_vaccinations_raw'] + d['properties']['daily_vaccinations'] + '\n'
    with open('./tmpfile', 'w', encoding='utf-8') as f:
        f.write(sb)
