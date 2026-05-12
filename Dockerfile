FROM python:3.11-slim

WORKDIR /app

# システム依存
RUN apt-get update && apt-get install -y \
    curl \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイル
COPY detect2cam_reid_v4.py .
COPY dashboard.py .
COPY config.yaml.example .

# ディレクトリ作成
RUN mkdir -p captures/cam1 captures/cam2 captures/match logs models

# ReIDモデル（ビルド時にダウンロード）
RUN curl -L -o models/youtu_reid_baseline_lite.onnx \
    https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/youtu_reid_baseline_lite.onnx

EXPOSE 8501

# デフォルトは検知エンジン（ダッシュボードは別途起動）
CMD ["python", "detect2cam_reid_v4.py"]
