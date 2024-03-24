# Горюнов Александр, 14-а когорта - финальный проект, QA+
import data
import stand_request

def creat_new_order():

# создаем заказ
    response = stand_request.order_create()
    assert response.status_code == 201
    return response.json()["track"]

def test_order_info_by_track():

# создание и получение заказа
    track = creat_new_order()
    response = stand_request.get_order_info_by_track(str(track))
    assert response.status_code == 200