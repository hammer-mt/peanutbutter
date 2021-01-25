from flask import Blueprint, request # pylint: disable=import-error


contact = Blueprint('contact', __name__, template_folder='templates')


@contact.route('/', methods=['GET', 'POST'])
def index():
    # This prevents circular imports.
    from peanutbutter.contact.tasks import deliver_contact_email

    print("1. Index route started")

    deliver_contact_email.delay("mjt145@gmail.com",
                                "ladies and gentlemen... we got 'em.")

    print("3. Index route finished")    

    return "ok"

