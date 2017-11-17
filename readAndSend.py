def reading():
    import serial
    import time

    ser = serial.Serial('com1',9600)
    
    
    buffer = b''
    startFlag = False
    
    
    while True:
        num = ser.inWaiting()

        if num > 0:
            
            time1 = time.time()
            buffer = buffer + ser.read(num)
            startFlag = True
            
       
        while startFlag == True:
            num = ser.inWaiting()
            
            if num > 0:
                
                buffer = buffer + ser.read(num)
            

            time2 = time.time()
               
            if (time2 - time1) > 0.1:
                startFlage = False
                break
        

        if buffer != b'':
      
            #print(buffer)
            break
            
        if buffer == b'\r\n':
            break
        else:
            buffer == b''
    ser.close()
    return buffer

def sending(data):
    import serial
    ser = serial.Serial('com1',9600)

    send = ser.write(data.encode('gb2312'))

    ser.close()
    
