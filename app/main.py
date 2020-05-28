from VirtualAsistant import VirtualAsistant
import time

VA = VirtualAsistant('Duru', 'Alexa', 'tr-TR')

time.sleep(1)
while(1):
    VA.stt()