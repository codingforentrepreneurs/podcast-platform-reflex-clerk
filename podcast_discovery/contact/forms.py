from datetime import datetime
import reflex as rx
from podcast_discovery.contact.models import ContactMessageModel


class ContactFormState(rx.State):
    form_data: dict = {}
    message_id: int = None
    message_timestamp: datetime = None

    @rx.event
    def handle_form_submit(self, form_data:dict):
        self.form_data = form_data
        with rx.session() as session:
            # database session
            instance = ContactMessageModel.model_validate(form_data)

            # prepare to add to db
            session.add(instance)
            # finalize add to db
            session.commit()
            # refresh python instance with db data or simply instance.id
            session.refresh(instance)

            self.message_id = instance.id
            self.message_timestamp = instance.created_at



    
def contact_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Your name",
                    name="name",
                    type="text"
                ),
                rx.text_area(
                    placeholder='Your message',
                    name='message'
                ),
                rx.button("Send message", type='submit'),
            ),
            on_submit=ContactFormState.handle_form_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Input value"),
        rx.text(ContactFormState.message_id.to_string()),
        rx.text(ContactFormState.message_timestamp.to_string())
    )