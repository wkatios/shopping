#__coding=utf-8__
import requests


prd_dic ={
    "M40712":"pochette-accessoires-monogram-005656",
    "M46203":"carryall-pm-monogram-nvprod3770016v",
    "M81911":"wallet-on-chain-ivy-monogram-nvprod4200020v",
    "M81085":"nano-speedy-monogram-nvprod3430078v",
}

prd_url = "https://www.louisvuitton.cn/zhs-cn/products/"

## 抓取
def get_sku_info():
    ## 构建请求头
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Referer': 'https://www.louisvuitton.cn/zhs-cn/products/carryall-mm-monogram-nvprod3770015v/M46197',
            'origin': 'https://www.louisvuitton.cn',
            'Host': 'api-cn.louisvuitton.cn',
            'Connection':'keep-alive',
            'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }
    response = requests.get('https://api-cn.louisvuitton.cn/api/zhs-cn/catalog/skuavailability/M46203,M40712,M81911,M81085', headers=headers)
    shop_list = response.json().get("skuAvailability")
    for shop_info in shop_list:
        if(shop_info["exists"] is True and shop_info["inStock"] is False ):
            # 构建商品web页面链接
            web_url = prd_url+prd_dic[shop_info["skuId"]]+"/"+shop_info["skuId"]
            send_message(web_url)




# 发送消息通知, 方案wx,dd
# 邮箱时效性太差
def send_message(url):
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="
    payload ={
        "msgtype": "text",
        "text": {
            "content": "这款到货啦!!!   "+ url
        }
    }

    headers ={
        "Content-Type": "application/json"
    }
    response = requests.post(webhook,json=payload,headers=headers)
    print(response.text)

if __name__ == '__main__':
    print("开始启动")
    get_sku_info()
