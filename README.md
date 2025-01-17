# Medical Insurance Cost Prediction Web App

This repository contains a machine learning web application designed to predict medical insurance costs based on user input. The data for this project was collected from Kaggle, and the web app is built using Streamlit for the GUI.

## Features

- Predicts medical insurance costs based on various input features, such as age, sex, bmi, number of children, region, etc.
- Utilizes several machine learning models, with XGBoost selected as the best fit.
- User-friendly interface built with Streamlit.
- Model persistence using the pickle module.

## Models Used

The following models were tested for this project:

- Linear Regression
- Lasso Regression
- Decision Tree
- AdaBoost
- XGBoost
- Random Forest
- CatBoost

After thorough evaluation, XGBoost was found to be the most accurate model and was used for the final prediction model.

## Data

The dataset used for training the models was obtained from Kaggle. It includes the following features:

- `age`: Age of the primary beneficiary.
- `sex`: Gender of the beneficiary (0: male, 1: female).
- `bmi`: Body mass index, a measure of body fat based on height and weight.
- `children`: Number of children covered by the insurance.
- `region`: The beneficiary's residential area in the US (0: 'northeast', 1: 'northwest', 2: 'southeast', 3: 'southwest').
- `smoker`: Whether the beneficiary smokes or not (0: no, 1: yes).
- `charges`: Individual medical costs billed by health insurance.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/RiyanBhargava/ML_Project_2_Medical_Insurance_Cost_Predictor.git
    cd ML_Project_2_Medical_Insurance_Cost_Predictor
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run medical_insurance_webapp.py
    ```

## Usage

Once the app is running, open your browser and go to `http://localhost:8501`. You will see a web interface where you can input the necessary details (age, sex, BMI, children, region, smoker status) to predict the medical insurance cost.

## File Structure

- `medical_insurance_webapp.py`: Main file to run the Streamlit app.
- `medical_insurance.pickle`: Saved XGBoost model using the pickle module.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## Acknowledgements

- The dataset used in this project was obtained from Kaggle.
- Thanks to the authors of the various machine learning libraries used in this project.
