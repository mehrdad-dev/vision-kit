from tensorflow.keras.metrics import top_k_categorical_accuracy

def top_5_accuracy(in_gt, in_pred):
    return top_k_categorical_accuracy(in_gt, in_pred, k=5)

