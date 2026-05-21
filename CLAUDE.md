# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is a **Data Science and Machine Learning learning project** containing Jupyter notebooks covering various DS/ML topics organized by category.

## Project Structure

```
Python/
├── Data Analysis/      - Pandas, NumPy notebooks
├── Data Structures/   - Lists, tuples, sets, dictionaries
├── Data Viz/          - Matplotlib, Seaborn
├── EDA/               - Exploratory Data Analysis
├── Feature Engineering/ - Missing values, SMOTE
├── Data Encoding/     - Label, One-hot, Ordinal, Target encoding
├── Simple Linear Regression/ - Regression tutorials
├── Deep Learning/     - ANN classification/regression
├── NLP For ML/        - Tokenization, POS, NER, Stemming, TF-IDF, BOW, Word2Vec
├── Flask/             - Web deployment
├── Streamlit/         - UI building
└── [other topics]     - OOP, Functions, Decorators, Generators, Logging, etc.
```

## Environment

- Python 3.12+
- Key packages: nltk, tensorflow, scikit-learn, pandas, numpy, xgboost, streamlit
- Run notebooks with Jupyter or VS Code

## Working with Notebooks

- Edit notebooks using NotebookEdit tool or directly in VS Code
- Many notebooks have `*_solution.ipynb` files with answers
- Some directories contain assignment questions and solutions paired together

## Development Notes

- Project uses `pyproject.toml` for dependency management (nlp-for-ml package)
- The root `stemming.ipynb` is a standalone NLP file
- Deep Learning folder contains ANN projects with experiments and prediction notebooks