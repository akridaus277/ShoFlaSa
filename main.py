import requests;
import schedule
import time;
import pytz;
from datetime import datetime
import util
import json
import threading

# The API endpoint
shopId1 = "231175464"
itemId1 = "23618204703"
modelId1 = "183719514935"

shopId2 = "231175464"
itemId2 = "11699823758"
modelId2 = "235371337140"

qty = 5

responseCheckout = {}

urlAddToCart = "https://shopee.co.id/api/v4/cart/add_to_cart"
urlGetItemsBrief = "https://shopee.co.id/api/v4/cart/get_items_brief"
urlCheckoutGet = "https://shopee.co.id/api/v4/checkout/get"
urlPlaceOrder = "https://shopee.co.id/api/v4/checkout/place_order"
headers1 = {"Cookie": 'SPC_F=yIdA1j8zUGK3W3dBJNKrfZ50JIZkO6D2; REC_T_ID=530bd343-91c2-11ed-bb71-f4ee082900f8; _gcl_au=1.1.1983448504.1685252020; _fbp=fb.2.1685252020769.1934827536; _tt_enable_cookie=1; _ttp=VXPruNiR0Brpc2se9nNoCbx0F-E; _ga_QMX630BLLS=GS1.1.1686217893.1.1.1686218521.60.0.0; SPC_CLIENTID=eUlkQTFqOHpVR0szagjogfpwtfbehqud; __stripe_mid=ef924d35-e35d-4dda-929f-18cfba9469b2af5eb8; SPC_SI=vzi2ZAAAAAAwMjhVZ0RCZma7EgAAAAAAV21BN3laNDA=; _QPWSDCXHZQA=781d7a26-ed90-4e4b-cdce-256f1e8c1c85; _gid=GA1.3.1009318050.1689828566; SPC_ST=.bnA2UG5aWnNWdU1mUEZZVD0jvDa947/H3LLJIHHBHR+xTMZVX38RybT42BNVo6H+Pjw626T6Y08O5rb2L7j5IQAe7ZH2N54FwMf5ZCRW2UgGOH6/LaxTGM1o6WqrUF+aUcpTyUydaE1JV4Ahx8aPm7JkK8EZBYBQy3O1lc55bJLjhKCVjOgkquJWloThfwHWAewE+dsLSDjKsuV4Ryuc6Q==; SPC_U=334552721; SPC_R_T_ID=uD59J/MxhZJcKEBBMw1m3RTKx0RdhdHl2ITnQZs1e506EQkJUXWuPEwe7KXRzmWOFz65F8oaPjBKQ6Ip0b0CL+heudpbJANeMEbPXVTNpxXW5L1TcbZifQUyCFdvRL2r6CwYV/Fuww2qLZ9+jS++PWny9ukWWhsJs4V0HUSZ+Uo=; SPC_R_T_IV=b2VUN3FzT2tuTkd1bzM2SQ==; SPC_T_ID=uD59J/MxhZJcKEBBMw1m3RTKx0RdhdHl2ITnQZs1e506EQkJUXWuPEwe7KXRzmWOFz65F8oaPjBKQ6Ip0b0CL+heudpbJANeMEbPXVTNpxXW5L1TcbZifQUyCFdvRL2r6CwYV/Fuww2qLZ9+jS++PWny9ukWWhsJs4V0HUSZ+Uo=; SPC_T_IV=b2VUN3FzT2tuTkd1bzM2SQ==; __LOCALE__null=ID; _med=refer; csrftoken=kRvynR0oLA2bKCkdwLBEkbgihjTFNdMp; SPC_IA=1; shopee_webUnique_ccd=NwpExH7gq5RCEH%2FQ6ER4bg%3D%3D%7CqFmR9rx8SFw7y9lYzu%2B9i45zU%2Bf1PeWpSeQOcaauKYqO%2FTXWgp%2FgmuS%2FrYP6t5Q0f4m%2BBZ4cghym0leTe0a%2BSiDMP%2FXNHeeev6Y%3D%7CIAs18T7bVNGCzZCW%7C06%7C3; ds=da2e6cb2fcbb317a8b191d062a76372f; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-61904553-8=1; _ga=GA1.1.988550125.1685252024; _ga_SW6D8G0HXK=GS1.1.1689849365.8.1.1689849414.11.0.0; SPC_EC=TjMwZUtWSVd5bktMelYwQsCZWElbF88487mAvSlJs6x6KsCUAhJCsk2T8dAgvxsSwx/FDs8/YqGTL/4rcl5kvnyKtecrTqGQQs6CJiU8UAHJFaEXXiGrkB4NOM75ORUyw0IMncvy6ubrjhvn7wB4uF/PFYVJNnUCvj/WWcUCmtQ='}
headers2 = {"Cookie": '_gcl_au=1.1.737323822.1688458647; SPC_F=P2alWQKgvZdUhoZrsniBQkfILSVyUxtR; REC_T_ID=371b0ac5-1a43-11ee-90cd-f4ee0828fa1d; _fbp=fb.2.1688458649391.1132987222; SPC_CLIENTID=UDJhbFdRS2d2WmRVtjjwsymrazvgmehg; _gcl_aw=GCL.1688458758.Cj0KCQjwho-lBhC_ARIsAMpgMoeJYmvzfavQ-9Ccgi06dlwwSm5huDjoYpPr0Ee9fPKqBIdnHgId3m4aAnj_EALw_wcB; _gac_UA-61904553-8=1.1688458763.Cj0KCQjwho-lBhC_ARIsAMpgMoeJYmvzfavQ-9Ccgi06dlwwSm5huDjoYpPr0Ee9fPKqBIdnHgId3m4aAnj_EALw_wcB; __stripe_mid=31edca55-4163-432f-9679-97f8908cc3d521a38c; _ga_8TJ45E514C=GS1.1.1688699418.1.0.1688699428.50.0.0; __LOCALE__null=ID; csrftoken=rTEppOIagUChF0mssX3MwnNL6nahAGz6; SPC_SI=wji2ZAAAAABoaHZ5c1BSWPzKEQAAAAAAcXd5ZzZLelQ=; _QPWSDCXHZQA=1b961bd2-76eb-410e-8970-82076f6094c6; _gid=GA1.3.1278959166.1689820074; SPC_ST=.eHl3QXROWkdCU1J0NWFQUYmAs5Fn6rll4mnpGNIdQhxDvJ/kupKleFEo3w5DdlYjeXlCDOQGf2yUPsjgl6ckOR/l1ygNiuiMzytqXBg810vueMZqwoLBZQ3t3ZVlv8NuGAYM0iiplAxiKFDfi+O2C1cuR2iufnJatacCH3j1L+GRjKmD0j4xGoUwUNC9M6oUvynJMVmCcOdCJMPvhJllUQ==; SPC_U=508807733; SPC_R_T_ID=/tfcqCihpJXUoKFF5jPyn/4hGqwLAnDyBD6MN5iLzZWfF2v6T0/iQnXLnSVUnrMZKFcyDYg3aCrQXD82YwEtK57Kl1T45Fzj6C3BN+4i+bmCW2yba639K+jfk7co1YiUDcsHf+EYZrp4enXvajV8fPlfAT77mlT6miOMVdnknNM=; SPC_R_T_IV=cEZNZ0RnOVRicWRaQUFZWA==; SPC_T_ID=/tfcqCihpJXUoKFF5jPyn/4hGqwLAnDyBD6MN5iLzZWfF2v6T0/iQnXLnSVUnrMZKFcyDYg3aCrQXD82YwEtK57Kl1T45Fzj6C3BN+4i+bmCW2yba639K+jfk7co1YiUDcsHf+EYZrp4enXvajV8fPlfAT77mlT6miOMVdnknNM=; SPC_T_IV=cEZNZ0RnOVRicWRaQUFZWA==; SPC_IA=1; shopee_webUnique_ccd=iOVqVhEzY6KsC37D6g615Q%3D%3D%7Cp89r0LkBzwac1X6cGV4MayW%2BTYAEEOyoXnfir61wglJuM3exm8mCLIF%2BRej%2BLvgaA0JHgT1o8QsCFpYZoSmYL5w6%2FwvTmiQCjMo%3D%7ClS%2FgzzDxJBucFh%2BO%7C06%7C3; ds=03ae5d8694f6cd0f37ef82b4f16b9c61; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.703213286.1688458654; _dc_gtm_UA-61904553-8=1; _ga_SW6D8G0HXK=GS1.1.1689849542.10.1.1689849605.58.0.0; SPC_EC=dHNHWXJkbFU1QzFhczFYZn8XcN7SxtFfJIVk2sZDRCT1D3d2ElyFAHG1dU1VZz3c/SelCHV/GWQ9YlaitHLxrQFN50vXxOs0CnxePzHyx0GiN2Q9iSuCyeJg5dcrF3QD1PswfrKRIa+J0m4GE0EovdMMI+AHZ7GE6vvz0KEWxtzJpM56MDul9JqggHpFO88k'}

    
def addToCart(headers,shop,item,model):
    print("I'm working Add To Cart...")
    requestBody = {
                    "quantity": qty,
                    "checkout": True,
                    "update_checkout_only": False,
                    "donot_add_quantity": False,
                    "source": "{\"refer_urls\":[]}",
                    "client_source": 1,
                    "shopid": int(shop),
                    "itemid": int(item),
                    "modelid": int(model)
                }
    # A POST request to the API
    response = requests.post(url=urlAddToCart,headers=headers,json=requestBody)

    # Print the response
    response_json = response.json()
    print("Completed Add To Cart...")

def getItemsBrief(headers,shop,item):
    print("I'm working Get Items Brieff...")
    # A POST request to the API
    requestBody = {
            "shoporders": [
                {
                    "shopid": int(shop),
                    "itemids": [
                        int(item)
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
    
   
    
def checkoutGet(headers, itemsBriefResponse, shop, item, model):
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
                    "shopid": int(shop)
                },
                "items": [
                    {
                        "itemid": int(item),
                        "modelid": int(model),
                        "quantity": qty,
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

def placeOrder(headers, requestBody):
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


def buyShopee(headers,shop,item,model):
    addToCart(headers,shop,item,model)
    placeOrder(headers, checkoutGet(headers, getItemsBrief(headers,shop,item), shop, item, model))
    return schedule.CancelJob

def startMultiThread():
    t1 = threading.Thread(target=buyShopee, args=(headers1,shopId1,itemId1,modelId1))
    t2 = threading.Thread(target=buyShopee, args=(headers2,shopId2,itemId2,modelId2))
    # t2 = threading.Thread(target=buyShopee, args=())
    # t3 = threading.Thread(target=buyShopee, args=())
    # t4 = threading.Thread(target=buyShopee, args=())
    # t5 = threading.Thread(target=buyShopee, args=())
    # t6 = threading.Thread(target=buyShopee, args=())

    t1.start()
    t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()

    t1.join()
    t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()

# startMultiThread()

schedule.every().day.at('18:09','Asia/Jakarta').do(startMultiThread)


while True:
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    jakartaTz = pytz.timezone('Asia/Jakarta')
    timeInJakarta = datetime.now(jakartaTz)
    currentTimeInJakarta = timeInJakarta.strftime(fmt)

    print("The current time in Jakarta is:", currentTimeInJakarta)
    schedule.run_pending()
    time.sleep(0.6)



