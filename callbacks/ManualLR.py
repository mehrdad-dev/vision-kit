from tensorflow.keras.callbacks import LearningRateScheduler

def get_learning_rate_from_file(filename, epoch):
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split('#', 1)[0]
            if line:
                par = line.strip().split(':')
                e = int(par[0])
                lr = float(par[1])
                if e <= epoch and lr > 0:
                    learning_rate = lr
                else:
                    return learning_rate
        return learning_rate
        

def get_scheduler(lr_schedule_file):
    def scheduler(epoch):
        lr = get_learning_rate_from_file(lr_schedule_file, epoch)
        return lr
    return scheduler

def ManualLR(filepath, verbose=1):
    LR_scheduler = get_scheduler(filepath)
    return LearningRateScheduler(LR_scheduler, verbose=verbose)            

