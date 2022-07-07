class CommandInterpreter:

    @staticmethod
    def process_command(commands):
        commands = commands.lower()
        if "temperatur" in commands or "warm" in commands or "kalt" in commands:
            return 0
        if "witz" in commands or "lustig" in commands or "scherz" in commands:
            return 1
