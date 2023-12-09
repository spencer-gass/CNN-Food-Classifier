import numpy as np

from sklearn.metrics import confusion_matrix

import itertools
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt


def plot_precision_recall(y_test, y_score, plt):
    # Compute Precision-Recall and plot curve
    precision = dict()
    recall = dict()
    average_precision = dict()
    for i in range(1):
        precision[i], recall[i], _ = precision_recall_curve(y_test,
                                                            y_score)
        average_precision[i] = average_precision_score(y_test, y_score)

    lw = 2
    # plt.plot(recall[0], precision[0], lw=lw, color='navy',
    #          label='Precision-Recall curve')
    plt.plot(recall[0], precision[0], lw=lw, color='navy')

    plt.set_xlabel('Recall')
    plt.set_ylabel('Precision')
    plt.set_ylim([0.0, 1.05])
    plt.set_xlim([0.0, 1.0])
    plt.set_title('Precision-Recall: AUC={0:0.2f}'.format(average_precision[0]))
    plt.legend(loc="lower left")


def plot_confusion_matrix(y_test, y_score, iplt):
    cm = confusion_matrix(y_test, y_score)

    classes = [0, 1]
    normalize = False
    title = 'Confusion matrix'
    cmap = plt.cm.Blues

    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    iplt.imshow(cm, interpolation='nearest', cmap=cmap)
    iplt.set_title(title)
    # iplt.set_colorbar()
    tick_marks = np.arange(len(classes))
    iplt.set_xticks(tick_marks, classes)
    iplt.set_yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        iplt.text(j, i, cm[i, j],
                  horizontalalignment="center",
                  color="white" if cm[i, j] > thresh else "black")

    # iplt.set_tight_layout()
    iplt.set_ylabel('True label')
    iplt.set_xlabel('Predicted label')


def plot_auc(y_test, y_score, iplt):
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(1):
        fpr[i], tpr[i], _ = roc_curve(y_test[:], y_score[:])
        roc_auc[i] = auc(fpr[i], tpr[i])

    lw = 2
    iplt.plot(fpr[0], tpr[0], color='darkorange',
              lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[0])
    iplt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    iplt.set_xlim([0.0, 1.0])
    iplt.set_ylim([0.0, 1.05])
    iplt.set_xlabel('False Positive Rate')
    iplt.set_ylabel('True Positive Rate')
    iplt.set_title('Receiver Operating Characteristic')
    iplt.legend(loc="lower right")


def model_perf_eval(y_test, y_score):

    fig, axes = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=False, figsize=(15, 10))

    plot_auc(y_test, y_score, axes[0])
    plot_precision_recall(y_test, y_score, axes[1])
    y_class = np.round(y_score)
    plot_confusion_matrix(y_test, y_class, axes[2])
    plt.xticks([], [])
    plt.yticks([], [])
    plt.tight_layout()
    plt.show()

