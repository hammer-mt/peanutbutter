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
