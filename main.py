# Packages with Python
import json
import pprint
from collections import OrderedDict

# Third Party Packages
from requests import Session

# Project's Packages
from constants import *


def scrape_website():
    """
    Function to scrape website

    :return: dict
    """
    with Session() as sess:

        # Login User
        login_data = {"USER": USERNAME, "PASSWORD": PASSWORD}
        url = DOMAIN_NAME + LOGIN_ENDPOINT
        resp = call_api(sess, url, method="post", data=login_data)
        if not resp['status']:
            return {'status': False, 'error': resp['error']}

        # Get Authorization Token
        url = DOMAIN_NAME + GET_TOKEN_ENDPOINT
        resp = call_api(sess, url, method="get")
        if not resp['status']:
            return {'status': False, 'error': resp['error']}
        token = json.loads(resp['data'])['token']

        # Get Billing Info Data
        headers = {"Authorization": "Bearer {}".format(token)}
        url = DOMAIN_NAME + GET_BILLING_INFO_ENDPOINT
        resp = call_api(sess, url, method="get", headers=headers)
        if not resp['status']:
            return {'status': False, 'error': resp['error']}
        billing_info = json.loads(resp['data'])['data']['BillingInfo']
        return {'status': True, 'data': billing_info}


def call_api(session, url, method, **kwargs):
    """
    Function to call api via requests package

    :param session: requests session object
    :param url: url to make request
    :param method: API method to call i.e 'get','post' etc.
    :param kwargs: extra arguments i.e data,headers etc.
    :return: dict
    """
    method_to_call = getattr(session, method)
    try:
        resp = method_to_call(url, **kwargs)
        if resp.status_code != 200:
            return {'status': False, 'error': resp.reason}
    except Exception as e:
        return {'status': False, 'error': str(e)}
    return {'status': True, 'data': resp.content}


def format_bill_info(data):
    """
    Function to format the bill info data

    :param data: dict
    :return: OrderdDict
    """
    return OrderedDict({"Last Payment": data['lastPaymentAmount'],
                        "Received": data['lastPaymentDate'],
                        "Current Bill": data['billDate'],
                        "Due Date": data['dueByDate'],
                        "Total Amount Due": data['currentDueAmount']
                        })


if __name__ == "__main__":

    response = scrape_website()
    if not response['status']:
        print("Some error occurred while scraping.\nError: {}".format(response['error']))
    else:
        result = format_bill_info(data=response['data'])
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(result)
