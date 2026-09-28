import os


def run(cmd):
    # load-test probe 06: deliberate command injection
    return os.system("sh -c " + cmd)


if __name__ == "__main__":
    run(input())
