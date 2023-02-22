import tkinter as tk
from datetime import datetime

from interface.styling import *


class Logging(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logging_title = tk.Text(self, height=1, width=20, state=tk.DISABLED, bg=BG_COLOR, fg=FG_COLOR,
                                    font=BOLD_FONT, highlightthickness=False, bd=0)
        self.logging_title.pack(side=tk.TOP)
        self.logging_title.configure(state=tk.NORMAL)  # Unlocks the tk.Text widgets
        self.logging_title.insert("0.0", "Logging Components") #1.0 means the text added at the beginning of the frame
        self.logging_title.configure(state=tk.DISABLED)  # Locks the tk.Text widget to avoid accidentally inserting in it

        self.logging_text = tk.Text(self, height=10, width=60, state=tk.DISABLED, bg=BG_COLOR, fg=FG_COLOR_2,
                                    font=GLOBAL_FONT, highlightthickness=False, bd=0)
        self.logging_text.pack(side=tk.TOP)


        # self.logging_title = tk.Label(self, text=text_t)
        # self.logging_title.place(x=500, y=0)
        # self.logging_title.pack(side=tk.TOP)
        # self.frames = tk.Frame(self)
        # self.frames.pack(side=tk.TOP)
        # self.logging_title = tk.Label(self.frames, text="hello",  bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
        # self.logging_title.grid(row=1, column=0)

        # self._commands_frame = tk.Frame(self, bg=BG_COLOR)
        # self._commands_frame.pack(side=tk.TOP)
        #
        #
        # self._binance_label = tk.Label(self._commands_frame, text="Binance", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
        # self._binance_label.grid(row=0, column=0)

    def add_log(self, message: str):

        """
        Add a new log message to the tk.Text widget, placed at the top, with the current UTC time in front of it.
        :param message: The new log message.
        :return:
        """

        self.logging_text.configure(state=tk.NORMAL)  # Unlocks the tk.Text widgets
        self.logging_text.insert("1.0", datetime.utcnow().strftime("%a %H:%M:%S :: ") + message + "\n") #1.0 means the text added at the beginning of the frame
        self.logging_text.configure(state=tk.DISABLED)  # Locks the tk.Text widget to avoid accidentally inserting in it
