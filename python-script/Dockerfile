FROM python:3.9

WORKDIR /usr/app/src

COPY ETL.py ./
COPY DEM_Challenge_Section1_DATASET.xlsx ./
COPY requirements.txt ./

# Install the required libraries
RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]



