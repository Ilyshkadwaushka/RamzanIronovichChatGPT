sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install docker docker.io

cd ..

docker build RamzanIronovichChatGPT -t ramzanironovichchatgpt
docker run -it ramzanironovichchatgpt