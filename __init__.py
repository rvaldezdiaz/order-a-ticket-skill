from mycroft import MycroftSkill, intent_file_handler


class OrderATicket(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ticket.a.order.intent')
    def handle_ticket_a_order(self, message):
        self.speak_dialog('ticket.a.order')


def create_skill():
    return OrderATicket()

