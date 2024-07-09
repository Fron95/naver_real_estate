# progressbar_widget.py
from PySide6.QtWidgets import QCheckBox

class CheckBoxWidget(QCheckBox):
    def __init__(self, parent=None, connect=None):
        super().__init__(parent)
        self.setObjectName("checkBox_tradeType_A1")
        if connect:
            self.stateChanged.connect(connect)
        self.setChecked(True)
