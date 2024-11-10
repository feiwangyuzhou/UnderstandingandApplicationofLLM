import requests
import json

# 定义 API 的 URL
url = 'https://open.hunyuan.tencent.com/openapi/v1/agent/chat/completions'

# 定义请求头
headers = {
    'X-Source': 'openapi',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' #在Bearer空格后填写Token
}

# 定义请求体
data = {
    "assistant_id": "",
    "user_id": "", #user_id亲测可以随便填（空着不填也行）
    "stream": False,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "七言绝句，诗里多些对母校的留恋,以及对未来的憧憬"
                }
            ]
        }
    ]
}

# 将请求体转换为 JSON 格式的字符串
json_data = json.dumps(data)

# 发送 POST 请求
response = requests.post(url, headers=headers, json=data)  # 使用 json 参数自动设置正确的 Content-Type

# 打印响应内容
print(response.text)