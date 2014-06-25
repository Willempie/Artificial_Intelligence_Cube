from logic.handling.panel_create import CreatePanel
from logic.handling.panel_action import ActionPanel


class PanelHandling:

    def __init__(self, display):
        self.current_panel = None

        self.edit = CreatePanel(display)
        self.edit_panel = self.edit.panel

        self.action = ActionPanel(display)
        self.action_panel = self.action.panel

    def _hide_current_panel(self):
        if self.current_panel is not None:
            self.current_panel.Hide()

    def switch_to_create(self):
        self._hide_current_panel()
        self.current_panel = self.edit_panel
        self.current_panel.Show()

    def switch_to_action(self):
        self._hide_current_panel()
        self.current_panel = self.action_panel
        self.current_panel.Show()
