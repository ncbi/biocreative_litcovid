"""

Evaluates classification results in the test file against
the gold standard for litcovid topics.

Usage:
    biocreative_litcovid_eval.py --gold=<str> --pred=<str>

Options:
    --gold=<str>       the file path of gold standard labels
    --pred=<str>       the file path of gold standard predictions

"""

import sys

import numpy as np
import pandas as pd
from docopt import docopt
from sklearn.metrics import classification_report


def print_label_based_scores(labels, preds, topics, threshold=0.5) -> None:
    labels = labels.sort_values(by=['PMID'])[topics]
    preds = preds.sort_values(by=['PMID'])[topics]
    predictions = (preds > threshold).astype('int32')
    print('label-based measures...')
    print(classification_report(labels, predictions, digits=4,
                                target_names=topics))


def print_instance_based_scores(labels, preds, topics, threshold=0.5) -> None:
    def to_set(elements, size):
        return set([i for i in range(size) if elements[i] == 1])

    labels = labels.sort_values(by=['PMID'])[topics]
    preds = preds.sort_values(by=['PMID'])[topics]
    preds = (preds > threshold).astype('int32')

    prc_list = []
    rec_list = []

    for pred_row, label_row in zip(preds.iterrows(), labels.iterrows()):
        _, pred_row = pred_row
        _, label_row = label_row

        predict_id_set = to_set(pred_row.tolist(), len(topics))
        gold_set = to_set(label_row.tolist(), len(topics))

        uni_set = gold_set.union(predict_id_set)
        if len(uni_set) == 0:
            prc = 1
            rec = 1
        else:
            intersec_set = gold_set.intersection(predict_id_set)
            tt = len(intersec_set)
            if tt == 0:
                prc = 0
                rec = 0
            else:
                prc = tt / len(predict_id_set)
                rec = tt / len(gold_set)

        prc_list.append(prc)
        rec_list.append(rec)

    mean_prc = round(np.mean(prc_list), 4)
    mean_rec = round(np.mean(rec_list), 4)
    f_score_zhou = round(2 * mean_prc * mean_rec / (mean_prc + mean_rec), 4)

    print('instance-based measures')
    print('mean precision', mean_prc)
    print('mean recall', mean_rec)
    print('mean f1', f_score_zhou)


def validate_file(file_name: str, df, header) -> None:
    if df.columns.values.tolist() != header:
        raise Exception(f'The {file_name} file header must be: '
                        + ','.join(header))

    if len(set(df['PMID'])) != len(df):
        raise Exception(f'The {file_name} file contains duplicate pmids')


def validate_file_size(query_df, subject_df):
    if len(query_df) != len(subject_df):
        raise Exception('The files should have the same size')

    if set(query_df['PMID']) != set(subject_df['PMID']):
        raise Exception('The files should have same pmids')


def validate(gold_df, pred_df, header):
    print('validation starts...')
    validate_file('gold', gold_df, header)
    validate_file('pred', pred_df, header)
    validate_file_size(gold_df, pred_df)
    print('validation passes...')


if __name__ == "__main__":
    argv = docopt(__doc__, sys.argv[1:])
    header = ['PMID', 'Treatment', 'Diagnosis', 'Prevention', 'Mechanism',
              'Transmission', 'Epidemic Forecasting', 'Case Report']
    gold_file = argv['--gold']
    pred_file = argv['--pred']

    gold_df = pd.read_csv(gold_file)
    pred_df = pd.read_csv(pred_file)
    validate(gold_df, pred_df, header)

    print_label_based_scores(gold_df, pred_df, header[1:])
    print_instance_based_scores(gold_df, pred_df, header[1:])
