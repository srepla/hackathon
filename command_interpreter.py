class CommandInterpreter:

    @staticmethod
    def process_command(commands):
        commands = [command.lower for command in commands]
        if "temperatur" in commands or "warm" in commands or "kalt" in commands:
            return 0
