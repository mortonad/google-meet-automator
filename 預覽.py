# 一鍵預覽：啟動本機伺服器 + 自動開瀏覽器
# 用法：把這個檔放到「HTML 和截圖所在的資料夾」，然後執行  python 預覽.py
# 好處：用 http://localhost 開，截圖/相對路徑/字型都正常載入，網址列也乾淨（適合錄影）
import http.server, socketserver, webbrowser, os, threading, time

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # 切到本腳本所在資料夾

def open_browser():
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}/")        # 開資料夾清單，點你要的 HTML

threading.Thread(target=open_browser, daemon=True).start()
print(f"✅ 伺服器啟動：http://localhost:{PORT}/")
print("   瀏覽器會自動開，點你要展示的 HTML 即可。結束按 Ctrl+C。")
try:
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()
except OSError:
    print(f"⚠️ 連接埠 {PORT} 被佔用，把上面 PORT 改成 8001 再跑一次。")
