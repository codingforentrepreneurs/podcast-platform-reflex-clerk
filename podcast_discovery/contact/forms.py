import reflex as rx


class ContactFormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_form_submit(self, form_data:dict):
        self.form_data = form_data
        print(self.form_data)


    
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
        rx.text(ContactFormState.form_data.to_string())
    )