from gettext import gettext as _
from datetime import datetime

__version__ = '1.0a'
ABOUTPROGRAM = _("Kleiner Helfer für den Telefonsupport")
ABOUTTXT = _(f"""
Mit dem Support-Client kann man einfach bei einem Telefonsupport die Anweisungen folgen und z.B.: die Fernwartung starten.
Ohne dabei mit dem Browser on sonst irgendeinem Tool nach dem Fernwartungsprogramm zu suchen und Herunterladen versuchen.

MIT @ {datetime.now().year} Bailey Solution""")
PROGRAM_NAME = "Support Client"
