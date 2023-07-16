import requests;
import schedule
import time;
import pytz;
from datetime import datetime
import util
import json
import threading

# The API endpoint
shopId = "15607053"
itemId = "14861010761"
modelId = "124584001285"

responseCheckout = {}

urlAddToCart = "https://shopee.co.id/api/v4/cart/add_to_cart"
urlGetItemsBrief = "https://shopee.co.id/api/v4/cart/get_items_brief"
urlCheckoutGet = "https://shopee.co.id/api/v4/checkout/get"
urlPlaceOrder = "https://shopee.co.id/api/v4/checkout/place_order"
headers = {"Cookie": '__LOCALE__null=ID; _gcl_au=1.1.452601646.1689505958; _med=refer; _fbp=fb.2.1689505958262.105414962; csrftoken=HXn4GL0j5gSIiiX5YFkENehv2cZsCKHI; SPC_SI=atibZAAAAAB6OHA1cjRaT5NeAQEAAAAARU1vWlN5Qmc=; SPC_F=7DooppIaCGCQzkBz87IEFh3rhxyuAiqZ; REC_T_ID=b1d77508-23c9-11ee-bf78-f4ee0828fa05; _QPWSDCXHZQA=ea6bb0b2-2711-4d58-e707-f38ffcd74d20; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.2063080919.1689505964; SPC_CLIENTID=N0Rvb3BwSWFDR0NRdjxratdrrkcjfsem; SPC_ST=.UERqbHdGd21IbDNja1oyTlqObG09L4N2kGwLPFH7/J6C1xd0vC1EK/MR86hYS5zt+md/4NIHKLaowSp2bdcA3UfbcW4MaggYtkUj4GXzzYvYa5/gxVMCt7Fhku2ycFR1irxzWb27UyTfU3nI512b+eAlbUeS24EY5FmkVjRCKBLbuaxHFvMSW6tbnktn/d24Y/xFnT8B+mjmVWN59YNiFg==; SPC_U=230630720; SPC_IA=1; SPC_R_T_ID=Ep1uaFEOtn8tAe0XuWEbERloKPZIo0QGMLKmo+9TAdA5NF0UwrpbvhVAIALE05gQMK3fQHjMecUBIFi3objuMpcfRs3t9yodX5wGYLn7mMvchvgKXN+1jeq8pk5kmx3eXlOAH8Ty2f7NSMJL6+7AXrJdjdbF3W3Hq1fUZiBkS4c=; SPC_R_T_IV=MmVXTHFnZjdOY3I4d3dqVA==; SPC_T_ID=Ep1uaFEOtn8tAe0XuWEbERloKPZIo0QGMLKmo+9TAdA5NF0UwrpbvhVAIALE05gQMK3fQHjMecUBIFi3objuMpcfRs3t9yodX5wGYLn7mMvchvgKXN+1jeq8pk5kmx3eXlOAH8Ty2f7NSMJL6+7AXrJdjdbF3W3Hq1fUZiBkS4c=; SPC_T_IV=MmVXTHFnZjdOY3I4d3dqVA==; shopee_webUnique_ccd=j7bMZ4yzbzTfDcG0XKiitA%3D%3D%7CLslRc%2FyklS6vM3YOzZdmOUkzREXkpfPblLDxnei26hgAuh6JDjqisAKCm%2BayZYJ29IunkOzRlzkCp34frYAv0GPhMTvIbP996Q%3D%3D%7CYRtzMb1jQnuNwNWs%7C06%7C3; ds=8dfe5c352e05117bf8c89e5a8b696b90; _ga_SW6D8G0HXK=GS1.1.1689505962.1.1.1689506718.55.0.0; _ga=GA1.1.907174497.1689505963; SPC_EC=Rm5xQ0M3OFhET1lRQUpabdVbUee5mOgQ3NC3ypKfRIfbv871sUHy8lRvg2mjaQMm1Y+9I22e5vBA7wddP7yxfN1ABidUg3oFdcRuT7pkNC+a9lSNbs/NKya7yKz9wB/4uYyj9zp0bBm1QHWTe5AD7b4zaVRkYT2gkOLVdcISL6U=; _dc_gtm_UA-61904553-8=1'}

    
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

# startMultiThread()

schedule.every().day.at('13:29','Asia/Jakarta').do(startMultiThread)


while True:
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    jakartaTz = pytz.timezone('Asia/Jakarta')
    timeInJakarta = datetime.now(jakartaTz)
    currentTimeInJakarta = timeInJakarta.strftime(fmt)

    print("The current time in Jakarta is:", currentTimeInJakarta)
    schedule.run_pending()
    time.sleep(1)



