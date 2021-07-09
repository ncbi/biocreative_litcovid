# BioCreative VII Track 5- LitCovid track Multi-label topic classification for COVID-19 literature annotation
This repository provides evaluation scripts and samples for [BioCreative VII Track 5](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/track-5/). 

## Track intro
The rapid growth of biomedical literature poses a significant challenge for manual curation and interpretation. This challenge has become more evident during the COVID-19 pandemic: the number of COVID-19-related articles in the literature is growing by about 10,000 articles per month. LitCovid, a literature database of COVID-19-related papers in PubMed, has accumulated more than 100,000 articles, with millions of accesses each month by users worldwide. LitCovid is updated daily, and this rapid growth significantly increases the burden of manual curation. In particular, annotating each article with up to eight possible topics, e.g., Treatment and Diagnosis, has been a bottleneck in the LitCovid curation pipeline.

This track calls for a community effort to tackle automated topic annotation for COVID-19 literature. Topic annotation in LitCovid is a standard multi-label classification task that assigns one or more labels to each article. These topics have been demonstrated to be effective for information retrieval and have been used in many downstream applications related to LitCovid. However, annotating these topics has been a primary bottleneck for manual curation. Increasing the accuracy of automated topic prediction in COVID-19-related literature would be a timely improvement beneficial to curators and researchers worldwide.

For more information, please see [BioCreative VII Track 5](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/track-5/).

## Content of the repository
- **goldstandard_label_samples.csv**: 

  - This file contains gold standard annotations of seven topics randomly sampled PubMed articles in [LitCovid](https://www.ncbi.nlm.nih.gov/research/coronavirus/).
  - For demonstration purpose, the IDs of PubMed articles (the PMID column in the file) are random integers.
  - For each of the seven topics, the annotations are binary: 1 means the topic is present whereas 0 means not.
  
- **prediction_label_samples.csv**:

  - This file contains the predictions of the same PubMed articles.
  - It has the same format as goldstandard_label_samples.csv except that it contains predicted topic probabilities rather than binary labels.
  - **Please ensure your prediction file for the test set has the same format.**

## Instructions to run the evaluation script
### Prerequisites
Have python3.8 installed locally.

### Clone the repository
```
git clone https://github.com/ncbi/biocreative_litcovid.git
cd biocreative_litcovid-main
```

### Create a virtual environment
```
python3.8 -m venv biocreative_litcovid

source biocreative_litcovid/bin/activate 
```
### Install the required libraries
```
pip install -r requirements.txt
```
### Run the evaluation script
```
python biocreative_litcovid_eval.py --gold goldstandard_label_samples.csv --pred prediction_label_samples.csv
```

You should get the following output:

```
validation starts...
validation passes...
label-based measures...
                      precision    recall  f1-score   support

           Treatment     0.9526    0.8142    0.8780      1087
           Diagnosis     0.8895    0.6483    0.7500       472
          Prevention     0.9386    0.9078    0.9230      1280
           Mechanism     0.9180    0.7780    0.8422       518
        Transmission     0.8955    0.7061    0.7896       279
Epidemic Forecasting     0.9328    0.6236    0.7475       178
         Case Report     0.8444    0.7600    0.8000        50

           micro avg     0.9304    0.8028    0.8619      3864
           macro avg     0.9102    0.7483    0.8186      3864
        weighted avg     0.9292    0.8028    0.8590      3864
         samples avg     0.8923    0.8330    0.8435      3864

instance-based measures
mean precision 0.8923
mean recall 0.833
mean f1 0.8616
```
## Contact
Please contact qingyu.chen AT nih.gov with the subject heading "BioCreative Track 5 LitCovid questions" if you have any questions.

## More information
- [BioCreative VII Track 5](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/track-5/) provides detailed information of the track (such as registrations, timelines, and FAQ)
- [BioCreative VII](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/) provides the general information of all the tracks.

## References
- Chen Q, Allot A, Lu Z. [Keep up with the latest coronavirus research](https://www.nature.com/articles/d41586-020-00694-1). Nature. 2020 Mar;579(7798):193-193.
- Chen Q, Allot A, Lu Z. [LitCovid: an open database of COVID-19 literature](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaa952/5964074). Nucleic Acids Research. 2021 Jan 8;49(D1):D1534-40.
