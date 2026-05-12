import streamlit as st
from pathlib import Path
from PIL import Image
import os
from datetime import datetime

st.set_page_config(page_title="CamReID Dashboard", layout="wide")
st.title("🛡️ CamReID Dashboard")
st.caption("Local-first Two-Camera Person Re-Identification System")

match_dir = Path("captures/match")

if not match_dir.exists() or not any(match_dir.glob("*.jpg")):
    st.info("まだマッチ画像がありません。検知エンジンを起動して両カメラの前に立ってみてください。")
    st.stop()

# 最新のマッチ画像を表示
matches = sorted(
    match_dir.glob("*.jpg"),
    key=lambda p: p.stat().st_mtime,
    reverse=True
)[:16]

st.subheader(f"最近の同一人物マッチ ({len(matches)}件表示)")

cols = st.columns(4)
for idx, path in enumerate(matches):
    try:
        img = Image.open(path)
        with cols[idx % 4]:
            st.image(img, caption=path.name, use_container_width=True)
    except:
        pass

st.divider()
st.caption(f"ログファイル: logs/reid_log_v4.jsonl | 最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
