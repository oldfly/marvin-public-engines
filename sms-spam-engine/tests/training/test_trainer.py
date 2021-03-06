#!/usr/bin/env python
# coding=utf-8

try:
    import mock

except ImportError:
    import unittest.mock as mock

from marvin_sms_spam_engine.training import Trainer


@mock.patch('marvin_sms_spam_engine.training.trainer.MultinomialNB.fit')
def test_execute(fit_mocked, mocked_params):

    data_source = {
        "X_train": ["train datas"],
        "X_test": ["test datas"],
        "y_train": ["train labels"],
        "y_test": ["test labels"],
        "vect": "foo"
    }

    ac = Trainer(dataset=data_source)
    ac.execute(params=mocked_params)

    fit_mocked.assert_called_once_with(['train datas'], ['train labels'])
    assert str(ac.marvin_model["vect"]) == "foo"
    assert not ac._params
