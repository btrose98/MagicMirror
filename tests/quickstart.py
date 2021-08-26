#need to install:    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class quickstart:
    
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    calEvent = []
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', calEvent.append(events_result))
    
    event1 = events[0]['start'].get('dateTime', events[0]['start'].get('date')) + " " + events[0]['summary']
    event2 = events[1]['start'].get('dateTime', events[1]['start'].get('date')) + " " + events[1]['summary']
    event3 = events[2]['start'].get('dateTime', events[2]['start'].get('date')) + " " + events[2]['summary']
    event4 = events[3]['start'].get('dateTime', events[3]['start'].get('date')) + " " + events[3]['summary']
    event5 = events[4]['start'].get('dateTime', events[4]['start'].get('date')) + " " + events[4]['summary']
    event6 = events[5]['start'].get('dateTime', events[5]['start'].get('date')) + " " + events[5]['summary']
    event7 = events[6]['start'].get('dateTime', events[6]['start'].get('date')) + " " + events[6]['summary']
    event8 = events[7]['start'].get('dateTime', events[7]['start'].get('date')) + " " + events[7]['summary']
    event9 = events[8]['start'].get('dateTime', events[8]['start'].get('date')) + " " + events[8]['summary']
    event10 = events[9]['start'].get('dateTime', events[9]['start'].get('date')) + " " + events[9]['summary']
    # print(event1)
    # print(event2)
    # print(event3)
    # print(event4)
    # print(event5)
    # print(event6)
    # print(event7)
    # print(event8)
    # print(event9)
    # print(event10)

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])