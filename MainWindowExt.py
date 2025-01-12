import random
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
from PyQt6 import uic


class MainWindowExt(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui", self)

        # Biến lưu các QPushButton
        self.buttons = []

        # Layout để chứa các QPushButton
        self.button_layout = QVBoxLayout(self.scrollAreaWidgetContents)

        # Kết nối các nút chức năng
        self.pushButtonCreaterandom.clicked.connect(self.create_random_buttons)
        self.pushButtonAdd.clicked.connect(self.add_button)
        self.pushButtonUpdate.clicked.connect(self.update_button)
        self.pushButtonDelete.clicked.connect(self.delete_negative_buttons)
        self.pushButtonAscSort.clicked.connect(self.sort_buttons_asc)
        self.pushButtonDescSort.clicked.connect(self.sort_buttons_desc)
        self.pushButtonRemoveall.clicked.connect(self.remove_all_buttons)

    def create_random_buttons(self):
        """Tạo N nút với giá trị ngẫu nhiên từ -100 đến 100"""
        try:
            n = int(self.lineEditN.text())
        except ValueError:
            return  # Nếu giá trị không hợp lệ, thoát

        # Xóa các nút hiện có
        self.remove_all_buttons()

        for _ in range(n):
            value = random.randint(-100, 100)
            btn = QPushButton(str(value))
            btn.clicked.connect(lambda checked, b=btn: self.select_button(b))
            self.buttons.append(btn)
            self.button_layout.addWidget(btn)

    def add_button(self):
        """Thêm một nút với giá trị ngẫu nhiên từ 0 đến 10"""
        value = random.randint(0, 10)
        btn = QPushButton(str(value))
        btn.clicked.connect(lambda checked, b=btn: self.select_button(b))
        self.buttons.append(btn)
        self.button_layout.addWidget(btn)

    def update_button(self):
        """Cập nhật giá trị nút được chọn thành giá trị //10"""
        for btn in self.buttons:
            if btn.isChecked():
                current_value = int(btn.text())
                new_value = current_value // 10
                btn.setText(str(new_value))
                btn.setChecked(False)
                return

    def delete_negative_buttons(self):
        """Xóa các nút có giá trị âm"""
        for btn in self.buttons[:]:
            if int(btn.text()) < 0:
                self.buttons.remove(btn)
                btn.deleteLater()

    def sort_buttons_asc(self):
        """Sắp xếp các nút theo giá trị tăng dần"""
        self.buttons.sort(key=lambda b: int(b.text()))
        for btn in self.buttons:
            self.button_layout.addWidget(btn)

    def sort_buttons_desc(self):
        """Sắp xếp các nút theo giá trị giảm dần"""
        self.buttons.sort(key=lambda b: int(b.text()), reverse=True)
        for btn in self.buttons:
            self.button_layout.addWidget(btn)

    def remove_all_buttons(self):
        """Xóa tất cả các nút"""
        for btn in self.buttons:
            btn.deleteLater()
        self.buttons = []

    def select_button(self, button):
        """Chọn một nút để cập nhật"""
        for btn in self.buttons:
            btn.setChecked(False)
        button.setChecked(True)
