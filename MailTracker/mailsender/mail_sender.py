from __future__ import print_function

import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import os
from pathlib import Path

import mimetypes
from email.message import EmailMessage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

BASE_DIR = Path(__file__).resolve().parent.parent

# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
def build_file_part(file):
    """Creates a MIME part for a file.

    Args:
      file: The path to the file to be attached.

    Returns:
      A MIME part that can be attached to a message.
    """
    content_type, encoding = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        with open(file, 'rb'):
            msg = MIMEText('r', _subtype=sub_type)
    elif main_type == 'image':
        with open(file, 'rb'):
            msg = MIMEImage('r', _subtype=sub_type)
    elif main_type == 'audio':
        with open(file, 'rb'):
            msg = MIMEAudio('r', _subtype=sub_type)
    else:
        with open(file, 'rb'):
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(file.read())
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    return msg

def gmail_send_message(from_mail=None,to_mail=None,subject=None,mail_body=None,attatchments=None):

    if os.path.exists(os.path.join(BASE_DIR,'mailsender','token.json')):
        creds = Credentials.from_authorized_user_file(os.path.join(BASE_DIR,'mailsender','token.json'))
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()
        message.add_header('Content-Type','text/html')

        # attachment_filename = os.path.join(BASE_DIR,'templates/mail_template/base.html')
        # type_subtype, _ = mimetypes.guess_type(attachment_filename)
        # maintype, subtype = type_subtype.split('/')

        # with open(attachment_filename, 'rb') as fp:
        #     attachment_data = fp.read()


        message['To'] = to_mail
        message['From'] = from_mail
        message['Subject'] = subject
        message.set_payload(mail_body)

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'raw': encoded_message
        }
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def gmail_create_draft_with_attachment():
    """Create and insert a draft email with attachment.
       Print the returned draft's message and id.
      Returns: Draft object, including draft id and message meta data.

      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
    """
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    try:
        # create gmail api client
        service = build('gmail', 'v1', credentials=creds)
        mime_message = EmailMessage()

        # headers
        mime_message['To'] = 'kedernath.mallick.tint022@gmail.com'
        mime_message['From'] = 'kedernath.mallick.tint022@gmail.com'
        mime_message['Subject'] = 'sample with attachment'

        # text
        mime_message.set_content(
            'Hi, this is automated mail with attachment.'
            'Please do not reply.'
        )

        # attachment
        attachment_filename = 'templates/mail_template/base.html'
        # guessing the MIME type
        type_subtype, _ = mimetypes.guess_type(attachment_filename)
        maintype, subtype = type_subtype.split('/')

        with open(attachment_filename, 'rb') as fp:
            attachment_data = fp.read()
        print(attachment_data)
        mime_message.add_attachment(attachment_data, maintype, subtype)

        encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

        create_draft_request_body = {
            'message': {
                'raw': encoded_message
            }
        }
        # pylint: disable=E1101
        # draft = service.users().drafts().create(userId="me",
        #                                         body=create_draft_request_body)\
        #     .execute()
        draft=(service.users().messages().send
                        (userId="me", body=create_draft_request_body).execute())
        print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None
    return draft



if __name__ == '__main__':
    # print(BASE_DIR)
    gmail_send_message()
    # print(build_file_part('templates/mail_template/base.html'))
    # gmail_create_draft_with_attachment()