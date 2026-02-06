from __future__ import annotations

import logging
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QKeySequence, QPalette, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QWidget,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UIConfig:
    WINDOW_WIDTH: int = 650
    WINDOW_HEIGHT: int = 550
    MIN_WIDTH: int = 500
    MIN_HEIGHT: int = 450
    TITLE: str = "Text App"
    MAIN_PADDING: int = 20
    SECTION_PADDING: int = 15
    DISPLAY_PADDING: int = 20
    TEXT_DEFAULT: str = "Sample Text"
    TEXT_FONT_SIZE: int = 36
    TEXT_FONT_WEIGHT: QFont.Weight = QFont.Weight.Bold
    ENTRY_FONT_SIZE: int = 14
    LABEL_FONT_SIZE: int = 13
    BUTTON_FONT_SIZE: int = 13
    SLIDER_MIN: int = 16
    SLIDER_MAX: int = 64
    COLOR_OPTIONS: list[str] = [
        "red",
        "blue",
        "green",
        "black",
        "white",
        "purple",
        "orange",
        "pink",
        "cyan",
        "yellow",
        "magenta",
        "gray",
    ]


# --- Dark / Light Palette Definitions ---

_DARK_COLORS: dict[QPalette.ColorRole, str] = {
    QPalette.ColorRole.Window: "#1e1e1e",
    QPalette.ColorRole.WindowText: "#e0e0e0",
    QPalette.ColorRole.Base: "#2b2b2b",
    QPalette.ColorRole.AlternateBase: "#333333",
    QPalette.ColorRole.Text: "#e0e0e0",
    QPalette.ColorRole.Button: "#333333",
    QPalette.ColorRole.ButtonText: "#e0e0e0",
    QPalette.ColorRole.Highlight: "#3498db",
    QPalette.ColorRole.HighlightedText: "#ffffff",
    QPalette.ColorRole.PlaceholderText: "#888888",
}

_LIGHT_COLORS: dict[QPalette.ColorRole, str] = {
    QPalette.ColorRole.Window: "#f5f5f5",
    QPalette.ColorRole.WindowText: "#1a1a1a",
    QPalette.ColorRole.Base: "#ffffff",
    QPalette.ColorRole.AlternateBase: "#f0f0f0",
    QPalette.ColorRole.Text: "#1a1a1a",
    QPalette.ColorRole.Button: "#e0e0e0",
    QPalette.ColorRole.ButtonText: "#1a1a1a",
    QPalette.ColorRole.Highlight: "#3498db",
    QPalette.ColorRole.HighlightedText: "#ffffff",
    QPalette.ColorRole.PlaceholderText: "#999999",
}


def _build_palette(colors: dict[QPalette.ColorRole, str]) -> QPalette:
    palette = QPalette()
    for role, hex_color in colors.items():
        palette.setColor(role, QColor(hex_color))
    return palette


DARK_PALETTE = _build_palette(_DARK_COLORS)
LIGHT_PALETTE = _build_palette(_LIGHT_COLORS)


# --- Style Sheets ---

_COMMON_BUTTON_STYLE = """
    QPushButton {{
        border: none;
        border-radius: 8px;
        padding: 10px 16px;
        font-size: {font_size}px;
        font-weight: bold;
        color: #ffffff;
        background-color: {bg};
    }}
    QPushButton:hover {{
        background-color: {hover};
    }}
    QPushButton:pressed {{
        background-color: {pressed};
    }}
"""


def _btn_style(bg: str, hover: str, pressed: str | None = None) -> str:
    return _COMMON_BUTTON_STYLE.format(
        font_size=UIConfig.BUTTON_FONT_SIZE,
        bg=bg,
        hover=hover,
        pressed=pressed or hover,
    )


DISPLAY_FRAME_DARK = "QFrame { background-color: #2b2b2b; border-radius: 12px; }"
DISPLAY_FRAME_LIGHT = "QFrame { background-color: #f0f0f0; border-radius: 12px; }"

ENTRY_STYLE = """
    QLineEdit {{
        border: 1px solid {border};
        border-radius: 8px;
        padding: 8px 12px;
        font-size: {font_size}px;
        background-color: {bg};
        color: {fg};
    }}
    QLineEdit:focus {{
        border: 2px solid #3498db;
    }}
"""

COMBO_STYLE = """
    QComboBox {{
        border: 1px solid {border};
        border-radius: 8px;
        padding: 8px 12px;
        font-size: {font_size}px;
        background-color: {bg};
        color: {fg};
    }}
    QComboBox::drop-down {{
        border: none;
        padding-right: 10px;
    }}
    QComboBox QAbstractItemView {{
        background-color: {bg};
        color: {fg};
        selection-background-color: #3498db;
        selection-color: #ffffff;
    }}
"""

SLIDER_STYLE = """
    QSlider::groove:horizontal {
        border: none;
        height: 6px;
        background: %(groove)s;
        border-radius: 3px;
    }
    QSlider::handle:horizontal {
        background: #3498db;
        width: 18px;
        height: 18px;
        margin: -6px 0;
        border-radius: 9px;
    }
    QSlider::handle:horizontal:hover {
        background: #2980b9;
    }
    QSlider::sub-page:horizontal {
        background: #3498db;
        border-radius: 3px;
    }
"""

THEME_BUTTON_STYLE = """
    QPushButton {{
        border: 2px solid {border};
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 12px;
        background-color: transparent;
        color: {fg};
    }}
    QPushButton:hover {{
        background-color: {hover_bg};
    }}
"""


class App(QMainWindow):
    """GUI application for text manipulation with PySide6.

    Features:
    - Text input and display
    - Color customization
    - Text reversal
    - Dark/Light theme toggle
    - Keyboard shortcuts
    """

    def __init__(self) -> None:
        super().__init__()
        self.text_history: list[str] = []
        self._is_dark = True

        self._configure_window()
        self._build_layout()
        self._setup_shortcuts()
        self._apply_theme()

    # ---- setup ---------------------------------------------------------- #

    def _configure_window(self) -> None:
        self.setWindowTitle(UIConfig.TITLE)
        self.resize(UIConfig.WINDOW_WIDTH, UIConfig.WINDOW_HEIGHT)
        self.setMinimumSize(UIConfig.MIN_WIDTH, UIConfig.MIN_HEIGHT)

    def _build_layout(self) -> None:
        central = QWidget(self)
        self.setCentralWidget(central)

        outer = QGridLayout(central)
        outer.setContentsMargins(
            UIConfig.MAIN_PADDING,
            UIConfig.MAIN_PADDING,
            UIConfig.MAIN_PADDING,
            UIConfig.MAIN_PADDING,
        )

        # Main container frame
        self.mainframe = QFrame(central)
        outer.addWidget(self.mainframe, 0, 0)

        layout = QGridLayout(self.mainframe)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setColumnStretch(0, 3)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)

        pad = UIConfig.SECTION_PADDING

        # --- Row 0: display area ----------------------------------------- #
        self.display_frame = QFrame(self.mainframe)
        layout.addWidget(self.display_frame, 0, 0, 1, 2)
        layout.setContentsMargins(pad, pad, pad, pad)

        display_layout = QGridLayout(self.display_frame)
        display_layout.setContentsMargins(
            UIConfig.DISPLAY_PADDING,
            UIConfig.DISPLAY_PADDING,
            UIConfig.DISPLAY_PADDING,
            UIConfig.DISPLAY_PADDING,
        )

        self.text_font = QFont()
        self.text_font.setPixelSize(UIConfig.TEXT_FONT_SIZE)
        self.text_font.setWeight(UIConfig.TEXT_FONT_WEIGHT)

        self.text_label = QLabel(UIConfig.TEXT_DEFAULT, self.display_frame)
        self.text_label.setFont(self.text_font)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setWordWrap(True)
        display_layout.addWidget(self.text_label, 0, 0)

        # --- Row 1: input label ------------------------------------------ #
        input_label = QLabel("Text Input", self.mainframe)
        bold_label_font = QFont()
        bold_label_font.setPixelSize(UIConfig.LABEL_FONT_SIZE)
        bold_label_font.setWeight(QFont.Weight.Bold)
        input_label.setFont(bold_label_font)
        layout.addWidget(input_label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        # --- Row 2: text entry + set text button ------------------------- #
        self.set_text_field = QLineEdit(self.mainframe)
        self.set_text_field.setPlaceholderText("Enter text here...")
        entry_font = QFont()
        entry_font.setPixelSize(UIConfig.ENTRY_FONT_SIZE)
        self.set_text_field.setFont(entry_font)
        self.set_text_field.setFixedHeight(40)
        self.set_text_field.returnPressed.connect(self.set_text)
        layout.addWidget(self.set_text_field, 2, 0)

        self.set_text_button = QPushButton("Set Text", self.mainframe)
        self.set_text_button.setFixedHeight(40)
        self.set_text_button.setStyleSheet(_btn_style("#3498db", "#2980b9"))
        self.set_text_button.clicked.connect(self.set_text)
        layout.addWidget(self.set_text_button, 2, 1)

        # --- Row 3: color label ------------------------------------------ #
        color_label = QLabel("Text Color", self.mainframe)
        color_label.setFont(bold_label_font)
        layout.addWidget(color_label, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        # --- Row 4: color combo + set color button ----------------------- #
        self.set_color_field = QComboBox(self.mainframe)
        self.set_color_field.addItem("Select a color")
        self.set_color_field.addItems(UIConfig.COLOR_OPTIONS)
        combo_font = QFont()
        combo_font.setPixelSize(UIConfig.ENTRY_FONT_SIZE)
        self.set_color_field.setFont(combo_font)
        self.set_color_field.setFixedHeight(40)
        self.set_color_field.currentTextChanged.connect(self._on_color_selected)
        layout.addWidget(self.set_color_field, 4, 0)

        self.set_color_button = QPushButton("Set Color", self.mainframe)
        self.set_color_button.setFixedHeight(40)
        self.set_color_button.setStyleSheet(_btn_style("#9b59b6", "#8e44ad"))
        self.set_color_button.clicked.connect(self.set_color)
        layout.addWidget(self.set_color_button, 4, 1)

        # --- Row 5: font size label + display ---------------------------- #
        font_label = QLabel("Font Size", self.mainframe)
        font_label.setFont(bold_label_font)
        layout.addWidget(font_label, 5, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.font_size_display = QLabel(str(UIConfig.TEXT_FONT_SIZE), self.mainframe)
        self.font_size_display.setFont(bold_label_font)
        layout.addWidget(
            self.font_size_display, 5, 1, 1, 1, Qt.AlignmentFlag.AlignRight
        )

        # --- Row 6: font slider ----------------------------------------- #
        self.font_slider = QSlider(Qt.Orientation.Horizontal, self.mainframe)
        self.font_slider.setMinimum(UIConfig.SLIDER_MIN)
        self.font_slider.setMaximum(UIConfig.SLIDER_MAX)
        self.font_slider.setValue(UIConfig.TEXT_FONT_SIZE)
        self.font_slider.setTickInterval(1)
        self.font_slider.valueChanged.connect(self._on_font_size_change)
        layout.addWidget(self.font_slider, 6, 0, 1, 2)

        # --- Row 7: reverse + undo -------------------------------------- #
        self.reverse_button = QPushButton("Reverse Text", self.mainframe)
        self.reverse_button.setFixedHeight(40)
        self.reverse_button.setStyleSheet(_btn_style("#e74c3c", "#c0392b"))
        self.reverse_button.clicked.connect(self.reverse)
        layout.addWidget(self.reverse_button, 7, 0)

        self.undo_button = QPushButton("Undo", self.mainframe)
        self.undo_button.setFixedHeight(40)
        self.undo_button.setStyleSheet(_btn_style("#555555", "#444444"))
        self.undo_button.clicked.connect(self.undo)
        layout.addWidget(self.undo_button, 7, 1)

        # --- Row 8: reset + copy ----------------------------------------- #
        self.reset_button = QPushButton("Reset", self.mainframe)
        self.reset_button.setFixedHeight(40)
        self.reset_button.setStyleSheet(_btn_style("#555555", "#444444"))
        self.reset_button.clicked.connect(self.reset)
        layout.addWidget(self.reset_button, 8, 0)

        self.copy_button = QPushButton("Copy Text", self.mainframe)
        self.copy_button.setFixedHeight(40)
        self.copy_button.setStyleSheet(_btn_style("#27ae60", "#1e8449"))
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button, 8, 1)

        # --- Row 9: theme toggle ----------------------------------------- #
        self.theme_button = QPushButton("Toggle Theme", self.mainframe)
        self.theme_button.setFixedHeight(35)
        self.theme_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.theme_button, 9, 0, 1, 2)

    def _setup_shortcuts(self) -> None:
        shortcuts: list[tuple[str, object]] = [
            ("Alt+T", self.set_text),
            ("Alt+C", self.focus_color_dropdown),
            ("Alt+R", self.reverse),
            ("Alt+U", self.undo),
            ("Alt+X", self.reset),
            ("Alt+Y", self.copy_to_clipboard),
            ("Escape", self._clear_focus),
        ]
        for key, callback in shortcuts:
            shortcut = QShortcut(QKeySequence(key), self)
            shortcut.activated.connect(callback)  # type: ignore[arg-type]

    # ---- theming -------------------------------------------------------- #

    def _apply_theme(self) -> None:
        app = QApplication.instance()
        assert isinstance(app, QApplication)

        palette = DARK_PALETTE if self._is_dark else LIGHT_PALETTE
        app.setPalette(palette)

        # Display frame
        self.display_frame.setStyleSheet(
            DISPLAY_FRAME_DARK if self._is_dark else DISPLAY_FRAME_LIGHT
        )

        # Entry
        if self._is_dark:
            entry_ss = ENTRY_STYLE.format(
                border="#444444",
                font_size=UIConfig.ENTRY_FONT_SIZE,
                bg="#2b2b2b",
                fg="#e0e0e0",
            )
        else:
            entry_ss = ENTRY_STYLE.format(
                border="#cccccc",
                font_size=UIConfig.ENTRY_FONT_SIZE,
                bg="#ffffff",
                fg="#1a1a1a",
            )
        self.set_text_field.setStyleSheet(entry_ss)

        # Combo box
        if self._is_dark:
            combo_ss = COMBO_STYLE.format(
                border="#444444",
                font_size=UIConfig.ENTRY_FONT_SIZE,
                bg="#2b2b2b",
                fg="#e0e0e0",
            )
        else:
            combo_ss = COMBO_STYLE.format(
                border="#cccccc",
                font_size=UIConfig.ENTRY_FONT_SIZE,
                bg="#ffffff",
                fg="#1a1a1a",
            )
        self.set_color_field.setStyleSheet(combo_ss)

        # Slider
        groove = "#444444" if self._is_dark else "#cccccc"
        self.font_slider.setStyleSheet(SLIDER_STYLE % {"groove": groove})

        # Theme toggle button
        if self._is_dark:
            theme_ss = THEME_BUTTON_STYLE.format(
                border="#555555", fg="#e0e0e0", hover_bg="#333333"
            )
        else:
            theme_ss = THEME_BUTTON_STYLE.format(
                border="#cccccc", fg="#1a1a1a", hover_bg="#e0e0e0"
            )
        self.theme_button.setStyleSheet(theme_ss)

    def toggle_theme(self) -> None:
        try:
            self._is_dark = not self._is_dark
            self._apply_theme()
        except Exception:
            logger.exception("Error toggling theme")

    # ---- callbacks ------------------------------------------------------ #

    def _clear_focus(self) -> None:
        self.setFocus()

    def focus_color_dropdown(self) -> None:
        self.set_color_field.showPopup()

    def _on_color_selected(self, text: str) -> None:
        if text and text != "Select a color":
            self.set_color()

    def _on_font_size_change(self, value: int) -> None:
        try:
            self.font_size_display.setText(str(value))
            self.text_font.setPixelSize(value)
            self.text_label.setFont(self.text_font)
        except Exception:
            logger.exception("Error updating font size")

    # ---- text operations ------------------------------------------------ #

    def _push_history(self, value: str) -> None:
        if value:
            self.text_history.append(value)

    def _set_text(self, value: str, *, record_history: bool = True) -> None:
        current_text = self.text_label.text()
        if record_history and value != current_text:
            self._push_history(current_text)
        self.text_label.setText(value)

    def set_text(self) -> None:
        try:
            new_text = self.set_text_field.text().strip()
            if new_text:
                self._set_text(new_text)
                self.set_text_field.clear()
        except Exception:
            logger.exception("Error setting text")

    def set_color(self) -> None:
        try:
            new_color = self.set_color_field.currentText().lower()
            if new_color and new_color != "select a color":
                self.text_label.setStyleSheet(f"color: {new_color};")
        except Exception:
            logger.exception("Error setting color")

    def reverse(self) -> None:
        try:
            current_text = self.text_label.text()
            self._set_text(current_text[::-1])
        except Exception:
            logger.exception("Error reversing text")

    def undo(self) -> None:
        try:
            if not self.text_history:
                return
            previous = self.text_history.pop()
            self._set_text(previous, record_history=False)
        except Exception:
            logger.exception("Error undoing text")

    def reset(self) -> None:
        try:
            self._set_text(UIConfig.TEXT_DEFAULT)
            self.text_label.setStyleSheet("")
            self.font_slider.setValue(UIConfig.TEXT_FONT_SIZE)
            self.set_color_field.setCurrentIndex(0)
        except Exception:
            logger.exception("Error resetting UI")

    def copy_to_clipboard(self) -> None:
        try:
            clipboard = QApplication.clipboard()
            if clipboard is not None:
                clipboard.setText(self.text_label.text())
        except Exception:
            logger.exception("Error copying text to clipboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
