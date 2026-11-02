# BISECT: AccountPatch disabled to isolate startup crash
# from AccountPatch import AccountPatch
from TelemetryPatch import TelemetryPatch  # RE-ENABLED: testing if safe without AccountPatch
from WindowsPatch import WindowsPatch
from EnablePhotoModePatch import EnablePhotoModePatch
