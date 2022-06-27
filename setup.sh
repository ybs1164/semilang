#!/bin/zsh

echo "poetry가 설치되어있는지 확인중..."
if ! command -v poetry &> /dev/null; then
  echo "poetry를 찾지 못했습니다"

  if ! command -v python3 &> /dev/null; then
    echo "python3이 설치되어 있지 않습니다"
    echo "먼저 python(>=3.9)을 설치하세요"
  else
    echo "pip를 통해 poetry를 설치합니다"
    python3 -m pip install poetry
  fi
else
  echo "poetry를 찾았습니다"
fi

poetry install
clear
echo "setup.sh 작업이 완료되었습니다"
echo "./run.sh 또는 poetry run semilang을 통해 semilang을 실행할 수 있습니다"