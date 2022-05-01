import argparse

from cmd.register import __CMD_REGISTER__


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Example v4")
    parser.add_argument("command", choices=[k for k in __CMD_REGISTER__.keys()])

    args_, _ = parser.parse_known_args()
    command = __CMD_REGISTER__[args_.command]()
    command.add_argument_group(parser)

    args = parser.parse_args()
    command.run(args)
