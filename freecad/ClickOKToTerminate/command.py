"""FreeCAD command and shutdown service for Click OK to Terminate."""

# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtCore, QtWidgets


COMMAND_NAME = "ClickOKToTerminate"
MENU_TEXT = "Click OK to Terminate"
TOOLTIP = "Notorious fatal error dialog. Unsaved work will be lost upon clicking."
DIALOG_TITLE = "Runtime Exception"
DIALOG_TEXT = "Click OK to terminate"


ICON_PATH = str(
    Path(__file__).resolve().parents[2]
    / "Resources"
    / "Icons"
    / "ClickOKToTerminate.svg"
)


def terminate():
    """Discard every open document and end the FreeCAD GUI session.

    Documents are deliberately closed through the FreeCAD application API before
    asking Qt to quit.  This makes the exit deterministic and avoids FreeCAD's
    normal unsaved-document confirmation dialog.
    """
    for document in list(App.listDocuments().values()):
        App.closeDocument(document.Name)
    QtCore.QCoreApplication.quit()


class ClickOKToTerminateCommand:
    """Show the joke error dialog, then immediately terminate FreeCAD."""

    def GetResources(self):
        """Provide FreeCAD with the command's visible UI resources."""
        return {
            "Pixmap": ICON_PATH,
            "MenuText": MENU_TEXT,
            "ToolTip": TOOLTIP,
        }

    def IsActive(self):
        """The command is intentionally available in every GUI state."""
        return True

    def Activated(self):
        """Display the information dialog; any dismissal initiates termination."""
        QtWidgets.QMessageBox.information(
            Gui.getMainWindow(),
            DIALOG_TITLE,
            DIALOG_TEXT,
            QtWidgets.QMessageBox.Ok,
        )
        terminate()


Gui.addCommand(COMMAND_NAME, ClickOKToTerminateCommand())
