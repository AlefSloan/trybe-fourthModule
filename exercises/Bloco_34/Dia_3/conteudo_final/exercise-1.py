class Log:
    def dispara_log(message):
        return message


class LogError:
    def __init__(self, log):
        self.log = log

    def dispara_log(self, message):
        return f"\033[91m{self.log.dispara_log(message)}\033[0m"


class LogWarning:
    def __init__(self, log):
        self.log = log

    def dispara_log(self, message):
        return f"\033[93m{self.log.dispara_log(message)}\033[0m"


class LogSuccess:
    def __init__(self, log):
        self.log = log

    def dispara_log(self, message):
        return f"\033[92m{self.log.dispara_log(message)}\033[0m"
