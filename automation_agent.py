import subprocess
import shlex


def run_command(cmd: str):
    """Run a system command and return the output."""
    try:
        result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        return f"Command failed with return code {exc.returncode}:\n{exc.output}"


def main():
    print("Automation Agent - enter commands to run on your system. Type 'exit' to quit.")
    while True:
        command = input('> ').strip()
        if command.lower() in {'exit', 'quit'}:
            break
        if not command:
            continue
        output = run_command(command)
        print(output)


if __name__ == '__main__':
    main()
