# Cam-ReID
# CamReID - Local-first Two Camera Person Re-Identification System

**映像は外部に送信せず、ローカルで完結**する2カメラ同一人物検知システムです。

## コンセプト
- 映像データはEdge（ローカル）のみ
- 特徴量のみで同一人物を判定
- 同一人物検知時に自動で比較画像を保存
- 研究・PoC・私有地利用向け

## 特徴
- YOLOv8人物検出 + OpenCV DNN ReID
- RTSP再接続機能
- Streamlitダッシュボード
- Docker対応
- JSONL構造化ログ

## クイックスタート

```bash
git clone <repository>
cd camreid

# 依存関係インストール
pip install -r requirements.txt

# 設定ファイル作成
cp config.yaml.example config.yaml
# ← config.yaml を編集（自分のカメラ情報に書き換え）

# 起動
python detect2cam_reid_v4.py
