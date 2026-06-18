# 🤖 Google 會議自動化助理

> **開完會，紀錄與待辦自己長出來。**
> 把錄音丟進 Google Drive → 幾分鐘後自動產出會議紀錄 + Google Tasks 待辦，全程零人工。

---

## 🚀 線上展示

| 版本 | 說明 | 連結 |
|------|------|------|
| **手機直式** | 手機全螢幕自動播放展示 | [點此開啟](./Google會議自動化助理_手機直式.html) |
| **簡報版** | 桌機鍵盤翻頁簡報 | [點此開啟](./Google會議自動化助理_簡報版.html) |

---

## ✨ 核心功能

- 🎙️ **一鍵觸發**：錄音檔丟進 Google Drive 指定資料夾，系統自動偵測
- 🤖 **AI 分析**：Gemini Multi-Agent 產出結構化 JSON（摘要 / 決議 / 待辦）
- 📄 **自動長出 Google Doc**：核心摘要、決策結論、每人待辦全自動寫入
- ✅ **同步到 Google Tasks**：待辦帶截止日、帶負責人，直接進你的 Tasks
- 📧 **完成通知 Email**：處理完自動寄信，摘要/決議/待辦數一眼掌握
- 🔁 **每 5 分鐘自動掃描**：Apps Script 排程，完全無人值守

---

## 🔧 技術棧

```
Google Apps Script   ← 事件驅動排程，每 5 分鐘掃 Drive 資料夾
Gemini API           ← Multi-Agent Prompt，輸出結構化 JSON
Google Drive API     ← 偵測新錄音、建立資料夾結構
Google Docs API      ← 自動寫入會議紀錄文件
Google Tasks API     ← 待辦事項同步（帶截止日）
Gmail API            ← 完成通知寄送
```

> ※ 誠實標示：端到端運行 = Google Workspace 路徑；Microsoft 365 版（Teams + Outlook）架構已設計，整合進行中。

---

## 🔄 運作流程

```
[你的手機/電腦]
     │
     │  拖錄音進 Drive 資料夾
     ▼
[Google Drive]
     │
     │  Apps Script 每 5 分鐘掃描
     ▼
[Google Apps Script]
     │
     │  呼叫 Gemini（Multi-Agent）
     ▼
[Gemini AI]  →  摘要 / 決議 / 待辦（JSON）
     │
     ├──▶ [Google Docs]  會議紀錄文件自動生成
     ├──▶ [Google Tasks] 待辦逐條新增（帶截止日）
     └──▶ [Gmail]        完成通知寄出
```

---

## 📂 檔案結構

```
Google會議自動化助理/
├── Google會議自動化助理_手機直式.html   # 手機全螢幕展示頁（自動播放）
├── Google會議自動化助理_簡報版.html     # 桌機簡報展示頁（鍵盤翻頁）
├── shot1.png                            # 截圖：會議錄音 App
├── shot2.png                            # 截圖：上傳到 Drive
├── shot3.png                            # 截圖：自動產出的 Google Doc
├── shot4.png                            # 截圖：Google Tasks 待辦
├── shot5.png                            # 截圖：完成通知 Email
├── YouTube_標題與說明.md                # YouTube 發布文案
├── 講解腳本_電腦版.md                   # 簡報講解腳本
├── 預覽.py                              # 本機預覽伺服器（python 預覽.py）
└── README.md                            # 本文件
```

---

## 🖥️ 本機預覽

```bash
# 在此資料夾執行（需要 Python 3）
python 預覽.py
# 瀏覽器自動開啟 http://localhost:8000/
# 點選 HTML 檔即可預覽
```

---

## 💡 解決的痛點

| 以前 | 現在 |
|------|------|
| 會後花 30–45 分鐘整理紀錄 | 幾分鐘自動產出 |
| 常漏決議、資訊散落各處 | 決議 / 待辦結構化，不漏接 |
| 換人 / 離職後，知識消失 | 紀錄留在 Drive，永久可查 |
| 需要專屬 IT 伺服器 | 零伺服器，用現有 Google Workspace |

---

## 📌 後續擴充方向

- [ ] Microsoft 365 版（Teams 錄音 → SharePoint → Outlook Tasks）
- [ ] 多語系支援（英日文會議）
- [ ] 自定義輸出模板（法律、醫療、行銷等場景）
- [ ] Slack / LINE 通知整合

---

## 👤 開發者

**Morton Lin（林亞賢）**
全端 / AI 應用開發者（自學）

- Instagram：[@morton17start](https://www.instagram.com/morton17start/)
- LinkedIn：[林亞賢](https://www.linkedin.com/in/%E4%BA%9E%E8%B3%A2-%E6%9E%97-6a1525283/)
- GitHub：[mortonad](https://github.com/mortonad)
- Email：mortonadair@gmail.com

---

*© 2026 Morton Lin · 個人獨立開發 · 可線上試用*
