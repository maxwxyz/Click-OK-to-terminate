"""Install Click OK to Terminate into FreeCAD's existing View toolbar."""

# SPDX-License-Identifier: GPL-3.0-or-later

import FreeCAD as App

from . import command


class WorkbenchManipulator:
    """Add the command to existing workbenches without defining a new workbench."""

    _instance = None

    def modifyMenuBar(self):
        """Do not add a menu entry."""
        return []

    def modifyContextMenu(self, recipient):
        """Do not add a context-menu entry."""
        return []

    def modifyToolBars(self):
        """Append the command to FreeCAD's standard View toolbar."""
        return [{"append": "ClickOKToTerminate", "toolBar": "View"}]

    @classmethod
    def install(cls):
        """Register the manipulator once during GUI startup."""
        if App.GuiUp and cls._instance is None:
            cls._instance = cls()
            App.Gui.addWorkbenchManipulator(cls._instance)


WorkbenchManipulator.install()
