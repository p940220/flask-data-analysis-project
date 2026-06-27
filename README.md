# 專題專案：動態網頁爬蟲與資料分析平台

本專案是一個結合 Flask 後端、動態網頁爬蟲與數學資料分析的完整 Web 應用。旨在分析特定群體的行為模式，並將其分類為「谷型人」或「山型人」。

## 主要功能

*   **動態爬蟲:** 使用 Selenium 模擬瀏覽器行為，自動抓取動態渲染的網頁資料。
*   **資料庫整合:** 串接 Render 上的 PostgreSQL，實現資料的持久化儲存。
*   **數學分析:** 運用變異係數 (Coefficient of Variation) 等數學指標進行人格行為分類。
*   **Web 展示:** 提供直觀的網頁介面，展示爬取到的原始資料與分析結果。
*   **軟硬結合 (加分項):** 預留介面與 Nvidia Jetson Orin Nano 進行數據連動。

## 安裝與運行

1.  **複製專案:**
    ```bash
    git clone <your-repo-url>
    cd flask_project
    ```

2.  **安裝依賴:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **環境變數配置:**
    複製 `.env.example` 並重新命名為 `.env`，填入您的資料庫連線字串。

4.  **啟動應用:**
    ```bash
    flask run
    ```

## 專案結構

*   `app/`: Flask 核心應用，包含路由與資料模型。
*   `scraper/`: 負責資料抓取的模組。
*   `analysis/`: 負責數學運算與分類的模組。
*   `docs/`: 存放專題計畫書與相關文件。

## 成員與貢獻

(請在此填寫小組成員及其具體貢獻內容)
