import json
import random

from feather.config import action_file
from feather.managers.input_manager import InputManager


class ActionManager(InputManager):
    def __init__(self, status_manager, output_manager):
        with open(action_file) as json_file:
            self.action_dictionary = json.load(json_file)

        self.status_manager = status_manager
        self.output_manager = output_manager
        InputManager.__init__(self)

    def _choose_action_from_status(self, data, key):
        # check status and return action
        for status, action in data[key].items():
            if status and status != "default":
                if self.status_manager.check_status(status):
                    return action
        if not status or status == "default":
            return action

    def retrieve_action(self, skinned_response):
        # check if response is in dictionary
        if skinned_response in self.action_dictionary:
            key = self.action_dictionary[skinned_response]

            with open(f"data/action/{key}.json", "r") as fp:
                data = json.load(fp)

            if data:
                return self._choose_action_from_status(data, key)
