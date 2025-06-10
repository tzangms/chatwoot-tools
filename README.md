# Chatwoot tools - 給 chatwoot 的相關配合工具

這是一個簡單的 Flask 網頁應用程式，用於查詢客戶資訊。該應用程式透過 API 從 USpace 系統獲取客戶資料，並以美觀的方式呈現。

## 功能特色

- 透過手機號碼查詢客戶資訊
- 支援多種請求方式：GET、POST、JSON
- 顯示客戶基本資料
- 顯示停車紀錄
- 顯示付款方式
- 顯示訂單資訊
- 提供原始 JSON 資料檢視

## 技術堆疊

- **後端框架**：Flask
- **前端**：HTML、CSS、Font Awesome 圖示
- **API 整合**：USpace API

## 安裝與設定

1. 克隆此專案：
   ```
   git clone <repository-url>
   cd uagent
   ```

2. 安裝相依套件：
   ```
   pip install -r requirements.txt
   ```

3. 設定環境變數：
   建立 `.env` 檔案並加入以下內容：
   ```
   USPACE_API_TOKEN=your_api_token_here
   ```

## 執行應用程式

開發環境執行：
```
python app.py
```

生產環境執行：
```
gunicorn app:app
```

## API 端點

### `/customer_info`

- **方法**：GET、POST
- **參數**：
  - `phone`：客戶手機號碼
- **回應**：返回包含客戶資訊的 HTML 頁面

## 使用範例

1. 透過瀏覽器訪問：`http://localhost:5000/customer_info?phone=0912345678`
2. 透過表單提交：在首頁輸入手機號碼並點擊「查詢」按鈕
3. 透過 API 請求：
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"phone":"0912345678"}' http://localhost:5000/customer_info
   ```

## 開發者

此專案由 USpace 團隊開發與維護。

## 授權

© 2025 USpace. 保留所有權利。
