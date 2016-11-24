import numpy as np

def __get_coefficients(y_true, y_pred_a, y_pred_b):
    a, b, c, d = 0, 0, 0, 0
    for i in range(y_true.shape[0]):
        if y_pred_a[i] == y_true[i] and y_pred_b[i] == y_true[i]:
            a = a + 1
        elif y_pred_a[i] != y_true[i] and y_pred_b[i] == y_true[i]:
            b = b + 1
        elif y_pred_a[i] == y_true[i] and y_pred_b[i] != y_true[i]:
            c = c + 1
        else:
            d = d + 1

    return a, b, c, d

def paired_metric_ensemble(ensemble, X, y, paired_metric):
    classifiers = ensemble.classifiers
    size = len(classifiers)
    diversities = []
    for i in range(size):
        for j in range(i):
            y_pred_a = classifiers[i].predict(X)
            y_pred_b = classifiers[j].predict(X)
            diversity = paired_metric(y, y_pred_a, y_pred_b)
            diversities = diversities + [diversity]

    return np.mean(diversities)

def q_statistics(y_true, y_pred_a, y_pred_b):
    a, b, c, d = __get_coefficients(y_true, y_pred_a, y_pred_b)
    q = float(a * d - b * c) / (a * d + b * c)
    return q

def correlation_coefficient_p(y_true, y_pred_a, y_pred_b):
    a, b, c, d = __get_coefficients(y_true, y_pred_a, y_pred_b)
    p = float((a * d - b * c)) / np.sqrt((a + b) * (c + d) * (a + c) * (b + d))
    return p


def disagreement_measure(y_true, y_pred_a, y_pred_b):
    a, b, c, d = __get_coefficients(y_true, y_pred_a, y_pred_b)
    disagreement = float(b + c) / (a + b + c + d)
    return disagreement

def agreement_measure(y_true, y_pred_a, y_pred_b):
    return 1.0 / disagreement_measure(y_true, y_pred_a, y_pred_b)


def double_fault_measure(y_true, y_pred_a, y_pred_b):
    a, b, c, d = __get_coefficients(y_true, y_pred_a, y_pred_b)
    df = float(d) / (a + b + c + d)
    return df

def new_entropy(ensemble, X, y):
    out = ensemble.output(X)
    P = np.sum(out, axis=2) / out.shape[1]
    P = - P * np.log(P + 10e-8)
    entropy = np.mean(np.sum(P, axis=1))

    return entropy

def entropy_measure_e(ensemble, X, y):
    factor = 0
    for j in range(y.shape[0]):
        right, wrong = 0, 0
        for estimator in ensemble.classifiers:
            [c] = estimator.predict(X[j])
            if c == y[j]:
                right = right + 1
            else:
                wrong = wrong + 1

        factor = factor + min(right, wrong)

    e = (1.0 / len(X)) * (1.0 / (len(ensemble) - len(ensemble) / 2)) * factor

    return e

def kohavi_wolpert_variance(ensemble, X, y):
    factor = 0
    for j in range(y.shape[0]):
        right, wrong = 0, 0
        for estimator in ensemble.classifiers:
            [c] = estimator.predict(X[j])
            if c == y[j]:
                right = right + 1
            else:
                wrong = wrong + 1

        factor = factor + right * wrong

    kw = (1.0 / (len(X) * (len(ensemble)**2))) * factor
    return kw

