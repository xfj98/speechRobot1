def main():
    import time
    from readAndSend import reading
    from readAndSend import sending

    read1 = reading()
    print (read1)

    hours = time.localtime(time.time())

        if read1.find(b'Mary') or read1.find(b'mary')!= -1:
            if hours[3] <12:
                send1 = sending('hi, John, good morning!\n')
            elif hours[3] <18:
                send1 = sending('hi, John, good afternoon!\n')
            else:
                send1 = sending('hi, John, good evening!\n')
        read2 = reading()
        print(read2)

        if read2 != b'':
            send2 = sending('OK!\n')

    
    read3 = reading()
    print(read3)


    ##if read1 == 'see you tommorrow' or read1 == 'goodbye'or read1 == 'byebye':
       ## sys.exit()

