from flask import Flask, render_template, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "OK"


@app.route('/customer_info', methods=['GET', 'POST'])
def customer_info():
    customer_info = None
    error = None
    
    # 從各種可能的來源獲取手機號碼
    phone = None
    
    # 檢查 POST 表單數據
    if request.method == 'POST' and request.form:
        phone = request.form.get('phone')
    
    # 檢查 GET 查詢參數
    if not phone and request.args:
        phone = request.args.get('phone')
    
    # 檢查 JSON 數據
    if not phone and request.is_json:
        json_data = request.get_json()
        phone = json_data.get('phone')
    
    # 檢查 POST 數據但非表單格式
    if not phone and request.method == 'POST' and request.data:
        try:
            json_data = json.loads(request.data)
            if isinstance(json_data, dict):
                phone = json_data.get('phone')
        except:
            pass
    
    # 記錄請求資訊，方便調試
    app.logger.info(f"請求方法: {request.method}")
    app.logger.info(f"表單數據: {request.form}")
    app.logger.info(f"查詢參數: {request.args}")
    app.logger.info(f"JSON數據: {request.is_json}")
    app.logger.info(f"獲取到的手機號碼: {phone}")
    
    if not phone:
        error = '未提供手機號碼，請確保請求中包含 phone 參數'
    else:
        try:
            # 呼叫 API 取得客戶資訊
            api_url = 'https://api.uspace.city/api/3rd-party/onmichatbot/customer_info'
            
            # 取得 API Token
            api_token = os.getenv('USPACE_API_TOKEN')
            
            # 設定標頭
            headers = {
                'Authorization': f'Bearer {api_token}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(api_url, json={'phone': phone}, headers=headers)
            
            if response.status_code == 200:
                customer_info = response.json()
            else:
                error = f'API 錯誤: {response.status_code}'
        except Exception as e:
            error = f'發生錯誤: {str(e)}'
    
    return render_template('index.html', customer_info=customer_info, error=error)

if __name__ == '__main__':
    app.run(debug=True)
