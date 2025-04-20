import os
from django.shortcuts import redirect, render
from django.conf import settings
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

def authorize(request):
    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, 'contacts_client_secret.json'),
        scopes=['https://www.googleapis.com/auth/contacts.readonly'],
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    request.session['state'] = state
    return redirect(authorization_url)

def oauth2callback(request):
    state = request.session['state']
    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, 'contacts_client_secret.json'),
        scopes=['https://www.googleapis.com/auth/contacts.readonly'],
        state=state,
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)
    return redirect('contacts')

def contacts(request):
    if 'credentials' not in request.session:
        return redirect('authorize')

    credentials = Credentials(**request.session['credentials'])
    service = build('people', 'v1', credentials=credentials)
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='names,emailAddresses'
    ).execute()
    connections = results.get('connections', [])

    return render(request, 'contacts/contacts.html', {'connections': connections})

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
