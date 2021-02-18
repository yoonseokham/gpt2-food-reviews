FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .
RUN pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
CMD python3 server.py
