from pnpimporter.plugnplay.interfaces import PnPTest
from pnpimporter.plugnplay import Plugin


class OneeightyuploadResolver(Plugin, PnPTest):
    implements = [PnPTest]
    name = "180upload"
