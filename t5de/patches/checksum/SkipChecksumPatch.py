from ...patch import ChecksumPatch


class SkipChecksumPatch(ChecksumPatch):
    def __init__(self):
        super(SkipChecksumPatch, self).__init__()
        self.register('SKIP_LIBRARY', 'checksum.txt', 'library')
        self.register('SKIP_IMVUCONTENT', 'checksum.txt', 'imvuContent')
        # DISABLED for IMVU 554.8: keep devicefingerprint checksum entry (TELEMETRY_10 disabled)
        # self.register('SKIP_FINGERPRINT', 'checksum.txt', 'devicefingerprint')
