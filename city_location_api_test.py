# -*- coding: utf-8 -*-

import requests

from lib.datafactory import DataFactory


def city_location_api_test():
    status_code_flag = False
    response_content_flag = False
    data_field_name_flag = False
    pagination_field_name_flag = False

    http_request_header = {'content-type': DataFactory.content_type,
                           'authentication': DataFactory.authentication,
                           'authority': DataFactory.authority,
                           'accept': DataFactory.accept}

    for city in DataFactory.cities:
        params = {'city': city}
        r = requests.get(DataFactory.end_point, headers=http_request_header, params=params)

        if 'OK' != r.status_code:
            status_code_flag = True
        if '' == r.text:
            response_content_flag = True
        if 'data' not in r.json():
            data_field_name_flag = True
        if 'pagination' not in r.json():
            pagination_field_name_flag = True

        if status_code_flag is True and response_content_flag is True and data_field_name_flag is True and pagination_field_name_flag is True:
            print('Test failed')
        else:
            print('Test passed')


if __name__ == "__main__":
    city_location_api_test()
