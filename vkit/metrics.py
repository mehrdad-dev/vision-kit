from tensorflow.keras.metrics import top_k_categorical_accuracy
from tensorflow.keras import backend as K

def top_5_accuracy(in_gt, in_pred):
    """
    top-5 accuracy metric
    """
    return top_k_categorical_accuracy(in_gt, in_pred, k=5)


def dice(y_true, y_pred, smooth=1):
    """
    Dice coefficient metric
    """
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)


