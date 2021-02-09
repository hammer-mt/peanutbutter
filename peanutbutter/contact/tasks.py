from datetime import datetime as dt
from peanutbutter.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """
    print("2. Celery task started")
    ctx = {'email': email, 'message': message}
    print(f"2.1. email sent to {ctx}")

    return None

@celery.task(bind=True)
def deliver_contact_email_cron(self, context):
    """
    Send a contact e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """
    email = context.get('email')
    message = context.get('message')
    
    print("2. Celery task started")
    ctx = {'email': email, 'message': message}
    print(f"2.1. email sent to {ctx}")
    print(f"2.2. this cron executed at {dt.utcnow()}")

    return None