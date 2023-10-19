import requests
import configuration
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


def get_order_body(response):
    return requests.get(configuration.URL_SERVICE + configuration.BEKOMMEN_ORDER_TRACK + str(response.json()['track']))


def test_positive_assert():
    response1 = post_new_order(data.order_body)
    response2 = get_order_body(response1)
    assert response2.status_code == 200
