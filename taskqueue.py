


def taskqueue(batchsize,processingtime,numtasks):
    maxtime=0
    while batchsize:
        currsize=batchsize.pop()
        currprocess=processingtime.pop()
        currnumtask=numtasks.pop()
        processingtime1=0
        while currnumtask>0: 
            currnumtask-=currsize
            processingtime1+=currprocess
        maxtime=max(maxtime,processingtime1)
    return maxtime


if __name__ == "__main__":
    print(taskqueue([4,3],[6,5],[8,8]))

