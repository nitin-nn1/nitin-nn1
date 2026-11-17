
<h1 align="center">Hi, I'm Nitin Nagavel</h1>
<p align="center">
  M.S. in Artificial Intelligence student at UT Austin.<br>
  I build projects around LLMs, retrieval, and machine learning pipelines.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/nitin-nagavel/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat" alt="LinkedIn"></a>
  <a href="mailto:home4nit@gmail.com"><img src="https://img.shields.io/badge/Email-home4nit%40gmail.com-555555?style=flat" alt="Email"></a>
</p>

---

### Featured projects

#### [Hybrid AI Prescription Recommender](https://github.com/nitin-nn1/AI-In-HealthCare-HighRisk-Project)
Takes a patient's symptoms in plain language and returns likely diagnoses, suggested prescriptions, and the reasoning behind them.

- Combines a PyTorch MLP classifier (384-dim MiniLM embeddings through 256- and 128-unit hidden layers), FAISS semantic search over past cases, and Azure OpenAI's GPT-5-mini
- Merges two mismatched healthcare datasets (348 patient records, 14,683 disease-to-drug mappings) using string matching, reaching a 92% match rate and 320 clean cases across 96 conditions
- Grounds the LLM with retrieved cases and classifier confidence scores to reduce made-up answers
- FastAPI backend paired with a React 18 frontend, running across four operating modes from full hybrid down to LLM-only if a component fails

`PyTorch` `FAISS` `Azure OpenAI` `FastAPI` `React` `Python`

#### [Nvidia Stock Price Model Comparison](https://github.com/nitin-nn1/CSML-2024-FInal-Project)
Compares a linear regression and a univariate LSTM for forecasting Nvidia's daily closing price on 2023 to 2024 data.

- Full data prep: cleaning, MinMax scaling, 80/20 split, and 3-day sliding windows
- Linear regression beat the LSTM (RMSE 4.56 vs 6.80), and the report explains why: one input feature and a short lookback window
- Includes a research write-up covering limitations and next steps

`Python` `Keras` `scikit-learn` `NumPy`

<!-- PROJECTS:START -->
<!-- PROJECTS:END -->

---

### Tools used across these projects

<table>
  <tr>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="36" height="36"/><br>Python</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" width="36" height="36"/><br>PyTorch</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="36" height="36"/><br>FastAPI</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="36" height="36"/><br>React</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg" width="36" height="36"/><br>Azure</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="36" height="36"/><br>NumPy</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" width="36" height="36"/><br>scikit-learn</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="36" height="36"/><br>Git</td>
  </tr>
</table>
