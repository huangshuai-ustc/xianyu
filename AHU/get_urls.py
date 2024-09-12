import os.path

import pandas as pd
import flickrapi

"""
serach_place_id
key：
e59fa03e0fde7c94f1cd91cd34ddfd0c
密鑰：
c425d213ae335873
"""


def get_data(long_lat, min_upload_date, max_upload_date, file):
    api_key = '9fd6b8eda514d7aea75fe261d5fd3e08'
    api_secret = '596d7663e4802b12'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
    for photo in flickr.walk(tag_mode='any', min_upload_date=min_upload_date, max_upload_date=max_upload_date,
                             extras=['url_o,description,license,date_upload,date_taken,owner_name,icon_server,'
                                     'original_format,last_update,geo,tags,machine_tags,o_dims,views,media,path_alias'],
                             minimum_longitude=long_lat[0], maximum_longitude=long_lat[1],
                             minimum_latitude=long_lat[2], maximum_latitude=long_lat[3]):
        url_c = photo.get('url_o')
        if url_c is None:
            continue
        id = str(photo.get('id'))
        owner = str(photo.get('owner'))
        description = str(photo.get('description'))
        lic = str(photo.get('license'))
        date_upload = str(photo.get('date_upload'))
        date_taken = str(photo.get('date_taken'))
        owner_name = str(photo.get('owner_name'))
        icon_server = str(photo.get('icon_server'))
        original_format = str(photo.get('original_format'))
        last_update = str(photo.get('last_update'))
        geo = str(photo.get('geo'))
        tags = str(photo.get('tags'))
        machine_tags = str(photo.get('machine_tags'))
        o_dims = str(photo.get('o_dims'))
        views = str(photo.get('views'))
        media = str(photo.get('media'))
        path_alias = str(photo.get('path_alias'))
        file.write(','.join(
            [id, owner, url_c, description, lic, date_upload, date_taken, owner_name, icon_server, original_format, last_update,
             geo, tags, machine_tags, o_dims, views, media, path_alias]))
        file.write('\n')


if __name__ == '__main__':
    zone = 'xxxx'  # 填入地区名 change
    # 依次填入minimum_longitude maximum_longitude minimum_latitude maximum_latitude
    long_lat = ['120.51', '122.12', '30.40', '31.53']  # change
    """
    如上海的经纬度信息是这样
    minimum_longitude='120.51', maximum_longitude='122.12',
    minimum_latitude='30.40', maximum_latitude='31.53'
    那么long_lat = ['120.51', '122.12', '30.40', '31.53']
    """
    if os.path.exists('{}.csv'.format(zone)):
        f = open('{}.csv'.format(zone), 'a', encoding='utf-8')
    else:
        f = open('{}.csv'.format(zone), 'a', encoding='utf-8')
        f.write('id,owner,url_o, description, license, date_upload, date_taken, owner_name, icon_server, '
                'original_format,last_update, geo, tags, machine_tags, o_dims, views, media, path_alias\n')
    year = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    dates = []
    for i in year:
        for j in month:
            dates.append(i + '-' + j + '-01')
    count = 60
    for i in range(count, len(dates) - 1):
        print(count)
        print(dates[i], dates[i + 1])
        get_data(long_lat, dates[i], dates[i + 1], f)
        count += 1
