# -*- coding: utf-8 -*-

import requests

from lib.datafactory import DataFactory


def city_location_api_test():
    status_code_flag = True
    response_content_flag = True
    data_field_name_flag = True
    pagination_field_name_flag = True

    http_request_header = {'content-type': DataFactory.content_type,
                           'authentication': DataFactory.authentication,
                           'authority': DataFactory.authority,
                           'accept': DataFactory.accept}

    for city in DataFactory.cities:
        params = {'city': city}
        r = requests.get(DataFactory.end_point, headers=http_request_header, params=params)
        print(r.url)

        if 200 != r.status_code:
            status_code_flag = False
        if '' == r.text:
            response_content_flag = False
        if 'data' not in r.json():
            data_field_name_flag = False
        if 'pagination' not in r.json():
            pagination_field_name_flag = False

        if status_code_flag is False or response_content_flag is False or data_field_name_flag is False or pagination_field_name_flag is False:
            print('Test failed')
        else:
            print('Test passed')


if __name__ == "__main__":
    city_location_api_test()
