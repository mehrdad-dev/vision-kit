from tensorflow.keras.callbacks import Callback

class StopMetric(Callback):
    """
    Stop by metric callback
    """
    def __init__(self, metric='val_acc', value=0.9, verbose=False):
        super(StopMetric, self).__init__()
        self.value = value
        self.verbose = verbose
        self.metric = metric

    def on_epoch_end(self, epoch, logs=None):
        if logs.get('val_accuracy') >= self.value:
            self.model.stop_training = True
        if self.verbose:
            val_loss = logs.get('val_loss')
            print(f'\n\n[Training Stop] {self.metric} metric reach {self.value}% in epoch {epoch} with validation loss {val_loss:.3f}\n\n')
            

