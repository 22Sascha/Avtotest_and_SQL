import requests
import data
import configuration


def order_create():
# Создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_create_body)


def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track)