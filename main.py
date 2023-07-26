import requests;
import schedule
import time;
import pytz;
from datetime import datetime
import util
import json
import threading

# The API endpoint

# dhimas
shopId1 = "62583853"
itemId1 = "7015652399"
modelId1 = "62277160401"

# pake akri buat iphone
shopId2 = "16729119"
itemId2 = "17986428822"
modelId2 = "107500904560"

qty = 1

responseCheckout = {}

urlAddToCart = "https://shopee.co.id/api/v4/cart/add_to_cart"
urlGetItemsBrief = "https://shopee.co.id/api/v4/cart/get_items_brief"
urlCheckoutGet = "https://shopee.co.id/api/v4/checkout/get"
urlPlaceOrder = "https://shopee.co.id/api/v4/checkout/place_order"

# dhimas
headers1 = {"Cookie": '_gcl_au=1.1.323982851.1683384107; SPC_F=53vX6Uin0PY9XvcOQg0yDGqbwXhDhMD9; REC_T_ID=2010eaaf-ec1c-11ed-a9ce-b47af14b4024; _fbp=fb.2.1683384107146.2091401407; _tt_enable_cookie=1; _ttp=9lq-RwKy9JfbQOgx8ZDlSut3Q8Z; SPC_CLIENTID=NTN2WDZVaW4wUFk5cmokvtbvozvllamo; SC_DFP=NCuPOhNVuNBKyQNUdBOezOOgkUuCKSsf; __stripe_mid=c734be43-ea7b-417b-8c41-d8b0c7e9dda5076e85; _ga_QMX630BLLS=GS1.1.1683993870.1.1.1683993892.38.0.0; _med=refer; SPC_SC_TK=34538a27b223fd83deac051676da17b7; SPC_SC_UD=939697575; SPC_U=939697575; SPC_STK=LepcFNgIgoOOZWnX5+6pwd/N659QCZSTVD8muqhKVXPRrdCjiGFlxXCQJeojiqWd83RFI493U8zfeE6uRS6FEOmxnLcHyF/7P//HrdaejtYXkCn+dRv4RyUmA1lr8J5VqPP3XcbcSFBeMnQAz6uuzv3qSLBkysFLa9M61jC640o1ZjhSdSBb7CRTJVXq1bcr; SPC_ST=.VzhVSDlld3RwVXB1QkZDQU4tvE/lHr4Qw8Vl0h2GBhQTs0Anpg5Okk/WZmOpDdr6FResK3GpHWLlrHsiMNrhu3ZQ9oqZHB7Tb0oAwv1zpI/yN27t/2B7o0yXiHFFqA3UissV1NJOVHh9GZaYQDh+C1N7xE+aijicOzv1ftZSbwvh2eHgKZ7n9iApg070jXqGHoPtX3VPdA5S09eY9yHZR6wc1/5ZYkY6endCS0fGtj0=; SPC_R_T_ID=7gDg4Ggl1aGP5myRJNCQaGtpzmPXetAsqSa9+JytsfWBsjgCNLx1pZdkfk5MSpM0MWVBuNePQ9/4WcCj+R2wAv3r95jfc3w+JPQlO46TwJpFus59HyaNwRgElGPZPTWXYRo9WCK28xmKOahdEk9cxeioeEa6Cj6V4UDOe/f6CvA=; SPC_R_T_IV=dXhqc1BwcVRseHlZR2FDdA==; SPC_T_ID=7gDg4Ggl1aGP5myRJNCQaGtpzmPXetAsqSa9+JytsfWBsjgCNLx1pZdkfk5MSpM0MWVBuNePQ9/4WcCj+R2wAv3r95jfc3w+JPQlO46TwJpFus59HyaNwRgElGPZPTWXYRo9WCK28xmKOahdEk9cxeioeEa6Cj6V4UDOe/f6CvA=; SPC_T_IV=dXhqc1BwcVRseHlZR2FDdA==; __LOCALE__null=ID; csrftoken=vqUCsXFr2BbyU5bBq0RZFywr3nANu2fT; SPC_SI=vzi2ZAAAAAAwMjhVZ0RCZvOHeQAAAAAAWXBIODhGWUY=; SPC_IA=1; _QPWSDCXHZQA=7c7bc09e-4d8c-4807-fe9e-566cfa433ad3; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.2001581681.1690368476; _ga=GA1.1.1562794019.1687671714; shopee_webUnique_ccd=%2F5MuVOPNQs5Xdv0MohNHRA%3D%3D%7ClZfLj6OAKYzRcnIh2hZv8BMbplNVXZjZy%2BpsJgyAEYvLT3SMbtHsyOOaSgR4XryexRm85OSqmps%3D%7C8Q8I2ajrloYQMw1t%7C08%7C3; ds=b091558a406e0cd2db2f4aab7f2a757e; _dc_gtm_UA-61904553-8=1; _ga_SW6D8G0HXK=GS1.1.1690368475.22.1.1690368779.59.0.0; SPC_EC=azZkQlVOTXNabEV0OVp0TFsUvTQvNDnfA1X6RMLGtlGTzG1TOQpVOFZ7UZpWB4VPQ8TDHoAZ3kKvK6UsoVvxqe961s4Yzaep6/nZWLcYsO+73VSSi9U5pEaiusi7AORLUXaMJwx1AAyuwWYK3QuCUByVUpJMnTV3S02tXoDJuI19JWA8hKMScem5Tuq0WAOS'}
fingerprint1 = "8LarcAxs1AWGWAceb2VpOA==|l5fLj6OAKYzRcnIh2hZv8BMbplNVXZjZy+psJnSlE4vLT3SMbtHsyOOaSgR4XryexRm85OSqmps=|8Q8I2ajrloYQMw1t|08|3"

# akri
headers2 = {"Cookie": '_gcl_au=1.1.737323822.1688458647; SPC_F=P2alWQKgvZdUhoZrsniBQkfILSVyUxtR; REC_T_ID=371b0ac5-1a43-11ee-90cd-f4ee0828fa1d; _fbp=fb.2.1688458649391.1132987222; SPC_CLIENTID=UDJhbFdRS2d2WmRVtjjwsymrazvgmehg; _gcl_aw=GCL.1688458758.Cj0KCQjwho-lBhC_ARIsAMpgMoeJYmvzfavQ-9Ccgi06dlwwSm5huDjoYpPr0Ee9fPKqBIdnHgId3m4aAnj_EALw_wcB; _gac_UA-61904553-8=1.1688458763.Cj0KCQjwho-lBhC_ARIsAMpgMoeJYmvzfavQ-9Ccgi06dlwwSm5huDjoYpPr0Ee9fPKqBIdnHgId3m4aAnj_EALw_wcB; __stripe_mid=31edca55-4163-432f-9679-97f8908cc3d521a38c; _ga_8TJ45E514C=GS1.1.1688699418.1.0.1688699428.50.0.0; SPC_SI=vTi2ZAAAAABKQlR1NGhOMw6vVgAAAAAAUFlXNFlIbDE=; _gid=GA1.3.856017950.1690190405; SPC_ST=.U083U2ozWmg3QVNFRDE0TiKrzQED3mMy/aueKCSEe2Of7pHRbT9on1OrhriCBz7vRUTS4/FP6X4h5OUc5QloDHjtkgSrYokTFq55IMkZns1AeQArHNSkq1a7VQ2Z+jZ2kC0p6uvu3RMuVoyAAXnOI6F8U/cSEyIOZM1cOsliHHVYuZ/W2EkLLDJTVAlRUtuigrjTVlw7H8LO1zvcZCip6uSxzDumjvXtidoH+D2E8gY=; SPC_U=939697575; SPC_T_ID=HBsNQXsGSNqOI9lHzvGEfk1P7waBK5pwRfjmdeoHg6ZDuzYUPTV8TBQ2Xf+xp6Ge6ggZLlflF7nFKCyyT6qCEtuP0c/ZeMvukbzyGCJiatFnRq0Mv22kTYT9vQLQcousQ8QVcGYQgUJKdhub2rTy4jb6OinYXfkPTwsKwgwTrHA=; SPC_T_IV=T2J4T0ZYdjREekh0YVpNWg==; SPC_R_T_ID=HBsNQXsGSNqOI9lHzvGEfk1P7waBK5pwRfjmdeoHg6ZDuzYUPTV8TBQ2Xf+xp6Ge6ggZLlflF7nFKCyyT6qCEtuP0c/ZeMvukbzyGCJiatFnRq0Mv22kTYT9vQLQcousQ8QVcGYQgUJKdhub2rTy4jb6OinYXfkPTwsKwgwTrHA=; SPC_R_T_IV=T2J4T0ZYdjREekh0YVpNWg==; __LOCALE__null=ID; csrftoken=sN2QgdTS4buFLmw1a2w2pVZ69A7fXEps; _QPWSDCXHZQA=1b961bd2-76eb-410e-8970-82076f6094c6; AMP_TOKEN=%24NOT_FOUND; SPC_IA=1; shopee_webUnique_ccd=T5JVgZHarqFJbxtRUzgPHA%3D%3D%7CftVmeiGyN5uHivC6sWN%2F%2BoI3nvC%2F9PzBU1NG85pcxIPzbJ19FP%2F2UrLalDnNbOOWOKlRzFNyeePsOL9ALqb7kucb8D7WUu18WCU%3D%7CsLR68U4jaOyg8G%2Bv%7C06%7C3; ds=2cb02015defcda18495a0f037046481c; _ga=GA1.1.703213286.1688458654; _dc_gtm_UA-61904553-8=1; _ga_SW6D8G0HXK=GS1.1.1690259193.14.1.1690259565.59.0.0; SPC_EC=UFFZZGUyaWFQNXdUQXZPcsBBW/j4c3cpVjA6mD7WIiKE0YcurPSFPC6vEuXmXC8xAzbJXjQqxP9pTftHa7j5KqRQBFDxLMhbC02dBhG3fAHFI+vpzdcfGKNGt6BEyjs4f/ZNN8L+F8UjEGYcl+zlQr4hDTqG7SZVul9xZJ17/qe8pYoqXW34bkeqzupucjdq'}
fingerprint2 = "SMerS7XI7VFRFlbvUDlEhA==|YiBzj3ZxwrjHosbeTEeE0sYZZjeC+eNlg7ZhQId1aPbEljFJce09T56169TzpK24J36HrtjGnpo3wVc0YqK0Xoh6H8leJYuJm10=|2y1XBmmQomNQUxUK|06|3"
    
def addToCart(headers,shop,item,model):
    # print("I'm working Add To Cart...")
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
    # print("Completed Add To Cart...")

def getItemsBrief(headers,shop,item):
    # print("I'm working Get Items Brieff...")
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
    # print(response_json)

    addOnDealId = response_json['data']['shoporders'][0]['iteminfos'][0]['add_on_deal_id']
    itemGroupId = response_json['data']['shoporders'][0]['iteminfos'][0]['item_group_id']

    responseArray = [addOnDealId, itemGroupId]
    
    return responseArray
    
   
    
def checkoutGet(headers, itemsBriefResponse, shop, item, model):
    addOnDealId = itemsBriefResponse[0]
    itemGroupId = itemsBriefResponse[1]
  
    # print("I'm working Checkout Get...")
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
        
    # shopeepay : 8001400 , channel_item_option_info kosongkan
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

    # print(response_json)
    
    # print("Completed Checkout Get...")
    return response_json

def placeOrder(headers, requestBody, fingerprint):
    # print("I'm working Place Order...")
    requestPlaceOrder = {}
    requestBody['_cft'] = []
    requestBody['captcha_version'] = 1
    device_sz_fingerprint = {
        'device_sz_fingerprint': fingerprint
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
    # print(response_json)
    print("Completed Place Order...")


def buyShopee(headers,shop,item,model,fingerprint):
    # addToCart(headers,shop,item,model)
    placeOrder(headers, checkoutGet(headers, getItemsBrief(headers,shop,item), shop, item, model), fingerprint)
    return schedule.CancelJob

def startMultiThread():
    buyShopee(headers1,shopId1,itemId1,modelId1,fingerprint1)
    buyShopee(headers2,shopId2,itemId2,modelId2,fingerprint2)
    # t1 = threading.Thread(target=buyShopee, args=(headers1,shopId1,itemId1,modelId1,fingerprint1))
    # t2 = threading.Thread(target=buyShopee, args=(headers2,shopId2,itemId2,modelId2,fingerprint2))
    # t2 = threading.Thread(target=buyShopee, args=())
    # t3 = threading.Thread(target=buyShopee, args=())
    # t4 = threading.Thread(target=buyShopee, args=())
    # t5 = threading.Thread(target=buyShopee, args=())
    # t6 = threading.Thread(target=buyShopee, args=())

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()

    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()

# startMultiThread()

schedule.every().day.at('18:01','Asia/Jakarta').do(startMultiThread)
    # schedule.every().day.at('17:03','Asia/Jakarta').do(buyShopee(headers1,shopId1,itemId1,modelId1,fingerprint1))

while True:
    fmt = '%Y-%m-%d %H:%M:%S:%f %Z%z'
    jakartaTz = pytz.timezone('Asia/Jakarta')
    timeInJakarta = datetime.now(jakartaTz)
    currentTimeInJakarta = timeInJakarta.strftime(fmt)

    print("The current time in Jakarta is:", currentTimeInJakarta)
    schedule.run_pending()
    time.sleep(0.0000001)


