class CommandInterpreter:

    @staticmethod
    def process_command(commands):
        commands = commands.lower()
        if "temperatur" in commands or "warm" in commands or "kalt" in commands or "wetter" in commands:
            return 0
        if "witz" in commands or "lustig" in commands or "scherz" in commands:
            return 1
        if "timer" in commands or "wecker" in commands or "alarm" in commands:
            return 2
        if "werte" in commands:
            return 3
        if "musik" in commands:
            return 4
