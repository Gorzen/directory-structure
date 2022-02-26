class NoUnknownDirectories:
    key = 'noUnknownDirectories'

    def check(path):
        return ''


class NoVisibleFiles:
    key = 'noVisibleFiles'

    def check(path):
        return ''


class NoHiddenFiles:
    key = 'noHiddenFiles'

    def check(path):
        return ''


allRules = [NoUnknownDirectories, NoVisibleFiles, NoHiddenFiles]

