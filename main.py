import requests;
import schedule
import time;
import pytz;
from datetime import datetime
import util
import json

# The API endpoint
shopId = "142804872"
itemId = "2243939219"
modelId = "4267732324"

promotionId = ""
price = 0
addressId = ""

responseCheckout = {}



urlGetAddress = "https://shopee.co.id/api/v4/account/address/get_user_address_list?with_warehouse_whitelist_status=true"
urlGetProduct = "https://shopee.co.id/api/v4/product/get_purchase_quantities_for_selected_model?itemId={itemId}&modelId={modelId}&quantity=1&shopId={shopId}".format(itemId=itemId, modelId=modelId, shopId=shopId)
urlAddToCart = "https://shopee.co.id/api/v4/cart/add_to_cart"
urlCheckoutGet = "https://shopee.co.id/api/v4/checkout/get"
urlPlaceOrder = "https://shopee.co.id/api/v4/checkout/place_order"
headers = {"Cookie": "__LOCALE__null=ID; _gcl_au=1.1.883725504.1689169744; csrftoken=7Z8hYpZ0rStgXUr2lQ76GipRsVekH19q; SPC_R_T_ID=WyM0Ny/kFRwhoDilWhp1O9nfThR3WNEYZ1Kzq3d9oj9DfjTisL79UWYbNWNaduCXHc4dV+96QMgzrpVSg5pqRteXfeuTGcyntQTexDjI+NWsKLKgx9Ku9dyvTHGqynbkznx6vOEvknvqz0qUtpxqf6GCphkQ0jbcNGvHxbmUQP8=; SPC_R_T_IV=cmJxM2o1cklxTUREU01aag==; SPC_T_ID=WyM0Ny/kFRwhoDilWhp1O9nfThR3WNEYZ1Kzq3d9oj9DfjTisL79UWYbNWNaduCXHc4dV+96QMgzrpVSg5pqRteXfeuTGcyntQTexDjI+NWsKLKgx9Ku9dyvTHGqynbkznx6vOEvknvqz0qUtpxqf6GCphkQ0jbcNGvHxbmUQP8=; SPC_T_IV=cmJxM2o1cklxTUREU01aag==; SPC_SI=F62aZAAAAABIOHRnVzRTOKyOZgAAAAAAcGdTekVxa0w=; SPC_F=6UDULxda53gK12M9llnHVX7oOHuoyhXk; REC_T_ID=dc3775c0-20ba-11ee-8315-2cea7fa4f854; _fbp=fb.2.1689169745475.619477051; _QPWSDCXHZQA=2c313eae-b382-4cdf-c698-810c637a9579; _ga_SW6D8G0HXK=GS1.1.1689169748.1.1.1689169838.33.0.0; _ga=GA1.3.129087050.1689169749; shopee_webUnique_ccd=LDwge%2BjDaF8oUZjrgLExQg%3D%3D%7CbVLLhXwkahHWhJevdXivcisseEK6ymtrC3Iv3Z86j4tcGY0utDDdSq%2F4VEChNrJyKExoA7OkPl6A2lzvQ7gZ6Tb5vLtig%2FBjkA%3D%3D%7Cfjfcf0zlpSbXzOMQ%7C06%7C3; ds=37984356c6600f4b45c8f40b34788503; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.1582871121.1689169750; SPC_CLIENTID=NlVEVUx4ZGE1M2dLvqqlklbroqhsvhcf; SPC_EC=N2VxZlBtejdYWUJsTDZaaA0P1ohzAbr5acK0LJYFrixKsGKjGljb8X+Z9uZqn9dDZI+cXz/bc4C6BUBazWl8ynBf4yynNyiG+qLwNYbvLvHIuonmV0s0gjRfu/xJkHaHcUaRcIu4JxbzXphlr9BqbQzidU/g4Ytre6uevXFHBTf/jPpywkbAJSg0otuUFvY3; SPC_ST=.R2lWWWZWcFF5anQzbEN0MiFdgprFan9qijw9InRrNarPmLGz6zadUFfRyog1tjU2FX1cMuSCtQcpx9u7/u3Sl9xy3qhAEE4/LoJDQnpuU7Rg/uvfNsMSdcvhaiqGNDgfpQDjvpu+/afvYc/sIgm7oYODaf91VeyEs9+8mwXs/4P+/oZSvZmxrIiX2ACj890xMO9HgBxIWbmDtMgjj+jn1Q==; SPC_U=508807733; SPC_IA=1; _dc_gtm_UA-61904553-8=1"}

# print(pytz.all_timezones)

def getProduct():
    print("I'm working Get Product...")
    # A GET request to the API
    response = requests.get(url=urlGetProduct,headers=headers)

    # Print the response
    response_json = response.json()
    promotionId = response_json['selected_price_and_stock']['promotion_id']
    price = response_json['selected_price_and_stock']['display_price']

    print("Completed Get Product...")
    
def getAddress():
    print("I'm working Get Address...")
    # A GET request to the API
    response = requests.get(url=urlGetAddress,headers=headers)

    # Print the response
    response_json = response.json()
    addressId = response_json['data']['addresses'][0]['id']
    print(addressId)

    print("Completed Get Product...")
    
    
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
    
def checkoutGet():
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
                        "add_on_deal_id": 0,
                        "is_add_on_sub_item": False,
                        "item_group_id": "null",
                        "insurances": []
                    }
                ]
            }
        ],
        "selected_payment_channel_data": {},
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

    # Print the response
    response_json = response.json()
    print(response_json)
    print("Completed Place Order...")


def buyShopee():
    getProduct()
    addToCart()
    placeOrder(checkoutGet())
    return schedule.CancelJob


schedule.every().day.at('21:15','Asia/Jakarta').do(buyShopee)


while True:
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    jakartaTz = pytz.timezone('Asia/Jakarta')
    timeInJakarta = datetime.now(jakartaTz)
    currentTimeInJakarta = timeInJakarta.strftime(fmt)

    print("The current time in Jakarta is:", currentTimeInJakarta)
    schedule.run_pending()
    time.sleep(1)



