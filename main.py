import requests;
import schedule
import time;
import pytz;
from datetime import datetime
import util
import json
import threading

# The API endpoint
shopId = "815542200"
itemId = "18722279651"
modelId = "181167356824"

responseCheckout = {}

urlAddToCart = "https://shopee.co.id/api/v4/cart/add_to_cart"
urlGetItemsBrief = "https://shopee.co.id/api/v4/cart/get_items_brief"
urlCheckoutGet = "https://shopee.co.id/api/v4/checkout/get"
urlPlaceOrder = "https://shopee.co.id/api/v4/checkout/place_order"
headers = {"Cookie": '__LOCALE__null=ID; _gcl_au=1.1.452601646.1689505958; _med=refer; _fbp=fb.2.1689505958262.105414962; csrftoken=HXn4GL0j5gSIiiX5YFkENehv2cZsCKHI; SPC_SI=atibZAAAAAB6OHA1cjRaT5NeAQEAAAAARU1vWlN5Qmc=; SPC_F=7DooppIaCGCQzkBz87IEFh3rhxyuAiqZ; REC_T_ID=b1d77508-23c9-11ee-bf78-f4ee0828fa05; _QPWSDCXHZQA=ea6bb0b2-2711-4d58-e707-f38ffcd74d20; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.2063080919.1689505964; SPC_CLIENTID=N0Rvb3BwSWFDR0NRdjxratdrrkcjfsem; SPC_IA=1; SPC_ST=.ZUFyU01nQzIzUmJpRzh3egQYlJip6s1IF3jcnsnCZoNOCp7QGISn+PkfIfr0paWaJrOC0BhASpOEmXkH0yBmugGF5sx8+zA8teACg3OGZP2mnhm0ldhnybDN+eymGFyejREJ+5PNtuD6mJBUwjW80wRYuHhE++T5hspISdl1bvQxC6LSrn7Ac9L8/GAcljgu0vJ/epMTQmOCyw1CEgHOGQ==; SPC_U=215271137; SPC_R_T_ID=JaZ4rigW8zlulDUSmohsEQ4xJax04AueJwYy9N2isV8koOgFK3vYxB6mjlVBPApb0Y77zWzDVCEAYWluqjIkqigZaoJ9211DOgNSwssdpTYvFPtI8tUepXssWrtDkE9Fa4Zm//aVvaVrKapAl0SR4Ws2mzlpH5mLojoxULolUp4=; SPC_R_T_IV=N2s5dlh3TmE0RjRsVDJESg==; SPC_T_ID=JaZ4rigW8zlulDUSmohsEQ4xJax04AueJwYy9N2isV8koOgFK3vYxB6mjlVBPApb0Y77zWzDVCEAYWluqjIkqigZaoJ9211DOgNSwssdpTYvFPtI8tUepXssWrtDkE9Fa4Zm//aVvaVrKapAl0SR4Ws2mzlpH5mLojoxULolUp4=; SPC_T_IV=N2s5dlh3TmE0RjRsVDJESg==; _ga=GA1.1.907174497.1689505963; SPC_EC=RnBEc056UEdhR2tBMTdxbL4KI7Bdfmlj2w0DDw6Kxr8W56PUfiQozIGt0zXdRMu8DwgNzeiyc8bju3xIfeub1CeysdG11CAetkYajuj3aoYA7peYwyXMbot0M/bOrg01CSVqseBb0Kye2IDbyRczHhnOmtfzHXD9fbFz4YPdNLs=; shopee_webUnique_ccd=g7jQcEHliRJeDaQH65WodA%3D%3D%7CLtZGdPKskCipP3kNypBiPUk%2BSUnvsbPfwrH9keTt7ElQ7huKAWD4uFDYm%2BixNN5899zwkOXchC4FqX8TqIYv22bhMTPXeeoy5JM%3D%7CYRtzMb1jQnuNwNWs%7C06%7C3; ds=d990ca20e7b69c3583f75bf24c144fb6; _ga_SW6D8G0HXK=GS1.1.1689505962.1.1.1689507942.60.0.0'}

    
def addToCart():
    print("I'm working Add To Cart...")
    requestBody = {
                    "quantity": 1,
                    "checkout": True,
                    "update_checkout_only": False,
                    "donot_add_quantity": False,
                    "source": "{\"refer_urls\":[]}",
                    "client_source": 1,
                    "shopid": int(shopId),
                    "itemid": int(itemId),
                    "modelid": int(modelId)
                }
    # A POST request to the API
    response = requests.post(url=urlAddToCart,headers=headers,json=requestBody)

    # Print the response
    response_json = response.json()
    print("Completed Add To Cart...")

def getItemsBrief():
    print("I'm working Get Items Brieff...")
    # A POST request to the API
    requestBody = {
            "shoporders": [
                {
                    "shopid": int(shopId),
                    "itemids": [
                        int(itemId)
                    ]
                }
        ]
    }


    # A POST request to the API
    response = requests.post(url=urlGetItemsBrief,headers=headers,json=requestBody)
   
    # Print the response
    response_json = response.json()
    # add_on_deal_id = response_json['data']['']['add_on_deal_id']
    print(response_json)

    addOnDealId = response_json['data']['shoporders'][0]['iteminfos'][0]['add_on_deal_id']
    itemGroupId = response_json['data']['shoporders'][0]['iteminfos'][0]['item_group_id']

    responseArray = [addOnDealId, itemGroupId]
    
    return responseArray
    
   
    
def checkoutGet(itemsBriefResponse):
    addOnDealId = itemsBriefResponse[0]
    itemGroupId = itemsBriefResponse[1]
    print(addOnDealId is None)
    print(itemGroupId is None)
    print("I'm working Checkout Get...")
    requestBody = {
        "_cft": [],
        "shoporders": [
            {
                "shop": {
                    "shopid": int(shopId)
                },
                "items": [
                    {
                        "itemid": int(itemId),
                        "modelid": int(modelId),
                        "quantity": 1,
                        "add_on_deal_id": 0 if addOnDealId is None else int(addOnDealId),
                        "is_add_on_sub_item": False,
                        "item_group_id": "null" if itemGroupId is None else itemGroupId,
                        "insurances": []
                    }
                ]
            }
        ],
        "selected_payment_channel_data": {
            "version": 2,
            "option_info": "",
            "channel_id": 8005200,
            "channel_item_option_info": {
                "option_info": "89052002"
            },
            "text_info": {}
        },
        "promotion_data": {
            "use_coins": False,
            "free_shipping_voucher_info": {
                "free_shipping_voucher_id": 0,
                "disabled_reason": "",
                "description": ""
            },
            "platform_vouchers": [],
            "shop_vouchers": [],
            "check_shop_voucher_entrances": True,
            "auto_apply_shop_voucher": False
        },
        "device_info": {
            "device_id": "",
            "device_fingerprint": "",
            "tongdun_blackbox": "",
            "buyer_payment_info": {}
        },
        "tax_info": {
            "tax_id": ""
        }
    }

    # A POST request to the API
    response = requests.post(url=urlCheckoutGet,headers=headers,json=requestBody)

    # Print the response
    response_json = response.json()

    print(response_json)
    
    print("Completed Checkout Get...")
    return response_json

def placeOrder(requestBody):
    print("I'm working Place Order...")
    requestPlaceOrder = {}
    requestBody['_cft'] = []
    requestBody['captcha_version'] = 1
    device_sz_fingerprint = {
        'device_sz_fingerprint': "wNbHSsMpMuy378FQVM8ftA==|ORTcntEe14cWp9r8yj5+3LeIAzbFOJLk2TT+SymgVuenrFmwuExbRsoyutTIsmhGg6XCPmzuTNR4UUITf9JK5M/Mdnlgx7HDHK8=|OlbwLX3ZSG+stKBk|06|3"
    }
    requestBody['device_info'] = device_sz_fingerprint
    with open('request.json') as source_file:
        requestPlaceOrder = json.load(source_file)
    util.map(responseCheckout,requestPlaceOrder)
    # A POST request to the API
    response = requests.post(url=urlPlaceOrder,headers=headers,json=requestBody)
    # print(requestBody)
    # Print the response
    response_json = response.json()
    print(response_json)
    print("Completed Place Order...")


def buyShopee():
    addToCart()
    placeOrder(checkoutGet(getItemsBrief()))
    return schedule.CancelJob

def startMultiThread():
    t1 = threading.Thread(target=buyShopee, args=())
    # t2 = threading.Thread(target=buyShopee, args=())
    # t3 = threading.Thread(target=buyShopee, args=())
    # t4 = threading.Thread(target=buyShopee, args=())
    # t5 = threading.Thread(target=buyShopee, args=())
    # t6 = threading.Thread(target=buyShopee, args=())

    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()

    t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()

startMultiThread()

# schedule.every().day.at('13:29','Asia/Jakarta').do(startMultiThread)


# while True:
#     fmt = '%Y-%m-%d %H:%M:%S %Z%z'
#     jakartaTz = pytz.timezone('Asia/Jakarta')
#     timeInJakarta = datetime.now(jakartaTz)
#     currentTimeInJakarta = timeInJakarta.strftime(fmt)

#     print("The current time in Jakarta is:", currentTimeInJakarta)
#     schedule.run_pending()
#     time.sleep(1)



