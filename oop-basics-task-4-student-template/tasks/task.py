from collections import deque

class HistoryDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._history = deque(maxlen=5)  # To store the last 5 keys

    def set_value(self, key, value):
        if key not in self or self[key] != value:  # Only track changes
            self._history.append(key)
        self[key] = value

    def get_history(self):
        return list(self._history)
