from typing import Text, List, Dict, Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from word2number import w2n

# class Save_Order_Action(Action):
#     def name(self) -> Text:
#         return "save_order_action"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         entities = tracker.latest_message.get('entities')
#         entity_val = tracker.get_latest_entity_values("menu_item", None)
#         for entity in entities:
#             b = self.get_answers_from_sheets(str(entity['value']))
#         # Displaying message
#         # dispatcher.utter_message('(You ordered): ' + str(entities[0]['value']))
#
#         return []
#     def get_answers_from_sheets(self, entity_val):
#         with open("myfile.txt", "a") as file:
#             file.write(str(entity_val)+"\n")
#         return True

class action_update_entities(Action):

    def name(self) -> Text:
        return "action_update_entities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # entity_val_update = tracker.get_latest_entity_values("menu_item_update", None)
        entities = tracker.latest_message.get('entities')

        entity_val = tracker.get_latest_entity_values("menu_item", None)

        size_list = ['small', 'medium', 'large']

        entity_val_2 = str(entities[0]['value'])

        with open('myfile.txt') as f:
            for line in f:
                entity_val_2 = entity_val_2 + ' ' + line

        line_split = entity_val_2.split()

        size = 'NA'
        Quantity = 'NA'
        for split in line_split:
            split = split.lower()
            if split in size_list:
                size = split
            else:
                try:
                    if split == 'a':
                        number = 1
                        Quantity = number
                    else:
                        number = w2n.word_to_num(split)
                        Quantity = number
                except:
                    pass
        if size == 'NA':
            # dispatcher.utter_message('NO_SIZE')
            dispatcher.utter_template('utter_ask_size', tracker)
        elif Quantity == 'NA':
            dispatcher.utter_template('utter_ask_quantity', tracker)
        else:
        #     dispatcher.utter_message('(SIZE)')
             dispatcher.utter_template('utter_next', tracker)
        for entity in entities:
            b = self.get_answers_from_sheets(str(entity['value']))

        return [UserUtteranceReverted()]
    def get_answers_from_sheets(self, entity_val):
        with open("myfile.txt", "a") as file:
            file.write(entity_val + ' ')
        return True

class action_clear_file(Action):

    def name(self) -> Text:
        return "action_clear_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return []

    def clear_sheets(self):
        with open("myfile.txt", "a") as file:
            file.truncate(0)
        return True


# rasa run actions --actions actions

# https://www.youtube.com/watch?v=VcbfcsjBBIg
