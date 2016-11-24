# TODO: add documentation header

import numpy as np


def max_rule(probs):
    """ Implements the max rule as defined by [1].

    This rule only makes sense if the classifiers output
    the posterior probabilities for each class.

    Parameters
    ----------
    probs:  Numpy 2d-array with rows representing each class, columns
            representing each classifier and elements representing
            posterior probabilities. Each column should sum up to
            one as a sanity check that the probabilities are valid.
    """

    return probs.max(axis=1)


def min_rule(probs):
    """ Implements the min rule as defined by [1].

    This rule only makes sense if the classifiers output
    the posterior probabilities for each class.

    Parameters
    ----------
    probs:  Numpy 2d-array with rows representing each class, columns
            representing each classifier and elements representing
            posterior probabilities. Each column should sum up to
            one as a sanity check that the probabilities are valid.
    """

    return probs.min(axis=1)


def mean_rule(probs):
    """
    Implements the first case of the median rule as defined by [1].

    This rule only makes sense if the classifiers output
    the posterior probabilities for each class.

    Parameters
    ----------
    probs:  Numpy 2d-array with rows representing each class, columns
            representing each classifier and elements representing
            posterior probabilities. Each column should sum up to
            one as a sanity check that the probabilities are valid.
    """

    return probs.mean(axis=1)


def median_rule(probs):
    """
    Implements the second case of the median rule as defined by [1].

    This rule only makes sense if the classifiers output
    the posterior probabilities for each class.

    Parameters
    ----------
    probs:  Numpy 2d-array with rows representing each class, columns
            representing each classifier and elements representing
            posterior probabilities. Each column should sum up to
            one as a sanity check that the probabilities are valid.
    """

    # numpy array has no median method
    return np.median(probs, axis=1)
