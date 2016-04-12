from app import app
from flask import render_template

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

@app.route('/')
def home():
    # credentials = GoogleCredentials.get_application_default()
    # bigquery_service = build('bigquery', 'v2', credentials=credentials)

    # try:
    #     query_request = bigquery_service.jobs()
    #     query_data = {
    #         'query' : 'SELECT DATE(TIMESTAMP(time_ts)) as date, '
    #                   'count(*) FROM [bigquery-public-data:hacker_news.stories] '
    #                   'where time is not null group by date order by date asc'
    #     # }

    #     query_response = query_request.query(
    #         projectId="hnalytics",
    #         body=query_data).execute()

    #     print("Query Results: ")
    #     for row in query_response['rows']:
    #         print('\t'.join(field['v'] for field in row['f']))

    # except HttpError as err:
    #     print('Error: {}'.format(err.content))
    #     raise err

    return render_template('home.html')