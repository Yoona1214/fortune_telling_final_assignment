from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class BirthInfo(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    sex: str = 'M'  # 默认性别为男性

@app.post("/api/analyze")
async def analyze(birth_info: BirthInfo):
    # 发送请求到外部 URL
    url = 'https://www.dearmoney.com.tw/eightwords/result_eight_words_page'
    payload = {
        '_Year': birth_info.year,
        '_Month': birth_info.month,
        '_Day': birth_info.day,
        '_Hour': birth_info.hour,
        '_sex': birth_info.sex,
        '_earth': 'N',
        '_method': 'A'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.post(url, data=payload, headers=headers, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取结果
        results = []
        font_elements = soup.find_all('font', color='#111111')
        for element in font_elements:
            results.append(element.get_text(strip=True))

        div_elements = soup.find_all('div', class_='row m-0 justify-content-center mt-5 mb-3')
        for element in div_elements:
            text = element.get_text(strip=True)
            if "◎開運方法" in text:
                index = text.find("◎開運方法")
                result = text[index + len("◎開運方法"):]
                results.append("◎開運方法: " + result)

        return JSONResponse(content={'success': True, 'results': results})
    else:
        return JSONResponse(content={'success': False, 'error': f'请求失败，状态码：{response.status_code}'})

# 挂载静态文件目录
app.mount("/", StaticFiles(directory="../fortune-telling-fe/build", html=True), name="static")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv('PORT', '8000')))
