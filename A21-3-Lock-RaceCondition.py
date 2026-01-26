import threading

iCnt=0
lobj=threading.Lock()

def Update():
    global iCnt
    for _ in range(500):
     with lobj:
        iCnt+=1

#def main():
  
if __name__ =="__main__":
    iCnt=0

    t1=threading.Thread(target=Update)
    t2=threading.Thread(target=Update)
    t3=threading.Thread(target=Update)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Value of iCnt is ",iCnt)
