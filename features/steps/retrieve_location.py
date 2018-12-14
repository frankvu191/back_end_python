# -*- coding: utf-8 -*-

import requests

from behave import given, when, then
from lib.datafactory import DataFactory

http_request_header = {}


@given('the endpoint is "{end_point}"')
def step_impl(context, end_point):
    context.end_point = end_point


@when('I send GET request with "{city}" parameter')
def step_impl(context, city):
    http_request_header['content-type'] = DataFactory.content_type
    http_request_header['authentication'] = DataFactory.authentication
    http_request_header['authority'] = DataFactory.authority
    http_request_header['accept'] = DataFactory.accept

    params = {'city': city}

    context.r = requests.get(context.end_point, headers=http_request_header, params=params)


@then('I should see status code is {status_code:d}')
def step_impl(context, status_code):
    assert(status_code == context.r.status_code)


@then('I should see the response is not empty')
def step_impl(context):
    assert(context.r.text != '')


@then('I should see "{field_name}" field in the response')
def step_impl(context, field_name):
    if field_name not in context.r.json():
        context.flag = False
    else:
        context.flag = True

    assert context.flag is True
