# Global Terrorism Attacks

Global Terrorism Attacks - predicting the group responsible using Machine Learning

Global Terrorism Database (http://www.start.umd.edu/gtd/) is an open-source database including information on terrorist events around the world from 1970 through 2014. 

This project explores attempting to predict which group may have been responsible for a terrorist incident based on information such as weapons used, attack type and the country of the incident.

## Requirements

- Written in Python `2.7`, some alterations might be required for `3+`
- `numpy` `pandas` `scikit-learn` `matplotlib`
- Jupyter Notebook
- Global Terrorism Database - to avoid hosting the files on GitHub (file size limits apply), you should [download](http://www.start.umd.edu/gtd/) the latest version of the Global Terrorism Database. The version can be changed in the config.py file if it has been updated.

## Installation

The easiest way to retrieve the requirements for this project is with the [anaconda](https://anaconda.org/)/[miniconda](https://conda.io/miniconda.html) python distribution, as it simplifies the setup process for scientific computation libraries such as `numpy` and `scikit-learn`.

### anaconda/miniconda users

If you use python distribution based on anaconda or miniconda based environment, first, install required packages by `conda` command:

```bash
$ conda install numpy pillow scipy pandas scikit-learn matplotlib pip
```

Jupyter Notebook can be installed with the Conda installer if you have Anaconda or Miniconda installed:

    $ conda install jupyter notebook

### pip
Alternatively you can use pip:

    $ pip install jupyter notebook


To open the notebook, `cd` to the directory that contains your code examples, e.g,.

    $ cd ~/directory/GTA

and launch `jupyter notebook` by executing

    $ jupyter notebook

Jupyter will start in our default browser (typically running at [http://localhost:8888/](http://localhost:8888/)), and you can explore the notebooks from here.

### Steps
1) Run through the steps in 'Data Processing.ipynb' - the CSV files will be created as you step through the notebook
2) Run through the steps in FeatureExtraction.ipynb


## Other tools used
- [Table of Contents (TOC) Generator](https://github.com/minrk/ipython_extensions#table-of-contents)

## Further Reading
- [GTD Codebook](http://www.start.umd.edu/gtd/downloads/Codebook.pdf) - Further information on the GTD data
