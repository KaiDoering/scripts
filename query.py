import sys
from google.auth import compute_engine
from google.cloud import bigquery

def main(id):
    credentials = compute_engine.Credentials(
        service_account_email='bigquery-qwiklab@' + id + '.iam.gserviceaccount.com')
    query = '''
    SELECT
        year,
        COUNT(1) as num_babies
    FROM
        publicdata.samples.natality
    WHERE
        year > 2000
    GROUP BY
        year
    '''
    client = bigquery.Client(
        project=id,
        credentials=credentials)
    print(client.query(query).to_dataframe())

if __name__ == "__main__":
    main(sys.argv[1])
