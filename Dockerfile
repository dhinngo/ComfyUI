FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/ComfyUI

# 既存のComfyUIファイルをコンテナにコピー
COPY . .

# 必要なPythonパッケージをインストール
RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# ポート8188を公開
EXPOSE 8188

# ComfyUIを起動
CMD ["python3", "main.py", "--listen", "0.0.0.0"]