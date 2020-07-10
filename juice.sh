#!/bin/bash


echo "
                 ___                       ___           ___        
    ___         /\  \                     /\__\         /\__\       
   /\__\        \:\  \       ___         /:/  /        /:/ _/_      
  /:/__/         \:\  \     /\__\       /:/  /        /:/ /\__\     
 /::\  \     ___  \:\  \   /:/__/      /:/  /  ___   /:/ /:/ _/_    
 \/\:\  \   /\  \  \:\__\ /::\  \     /:/__/  /\__\ /:/_/:/ /\__\   
    \:\  \  \:\  \ /:/  / \/\:\  \__  \:\  \ /:/  / \:\/:/ /:/  /   
     \:\__\  \:\  /:/  /     \:\/\__\  \:\  /:/  /   \::/_/:/  /    
     /:/  /   \:\/:/  /       \::/  /   \:\/:/  /     \:\/:/  /     
    /:/  /     \::/  /        /:/  /     \::/  /       \::/  /      
    \/__/       \/__/         \/__/       \/__/         \/__/       
      ___           ___           ___           ___                 
     /\__\         /\  \         /\  \         /\  \                
    /:/ _/_        \:\  \       /::\  \       /::\  \               
   /:/ /\  \        \:\  \     /:/\:\  \     /:/\:\__\              
  /:/ /::\  \   ___ /::\  \   /:/  \:\  \   /:/ /:/  /              
 /:/_/:/\:\__\ /\  /:/\:\__\ /:/__/ \:\__\ /:/_/:/  /               
 \:\/:/ /:/  / \:\/:/  \/__/ \:\  \ /:/  / \:\/:/  /                
  \::/ /:/  /   \::/__/       \:\  /:/  /   \::/__/                 
   \/_/:/  /     \:\  \        \:\/:/  /     \:\  \                 
     /:/  /       \:\__\        \::/  /       \:\__\                
     \/__/         \/__/         \/__/         \/__/                


[+] // UPDATING DOCKER // "

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get install docker-ce

echo "[+] // DOCKER INSTALLED //

[+] // RESTARTING DOCKER //"

sudo service docker restart

echo "[+] // PULLING JUICE SHOP //"

docker pull bkimminich/juice-shop

echo "[+] // RUNNING JUICE SHOP //"

docker run --rm -p 3000:3000 bkimminich/juice-shop &	PIDJS=$!
firefox -new-tab 'http://127.0.0.1:3000/' &	PIDFF=$!
wait $PIDJS=$!
wait $PIDFF=$!

