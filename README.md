# Dos-Detection-python3
## Dos Detection with Python3
- A simple python3 script that utilizes logging and resource monitoring to deduce if there's a DOS attack happening on the machine

### Installation (Ubuntu)
    git clone https://github.com/BiLLY-J03l/Dos-Detection-python3.git
    chmod +x dos_detect.py
    dos2unix dos_detect.py
    ./dos_detect.py

### Execution

- I installed an nginx server on my Ubuntu instance and I will use hping3 to launch a dos attack upon it

- Kali:

        hping3 --count 15000 --data 120 --syn -p 80 192.168.8.150 --win 64 --flood


- Nginx Server:
    - As we can see, the server gets slower by time.
![image](https://github.com/user-attachments/assets/4d39777b-4e9a-4c4e-946a-b585d94a71d1)
![image](https://github.com/user-attachments/assets/d38f77e3-2754-4849-a9a8-e94d3852cddd)



  
