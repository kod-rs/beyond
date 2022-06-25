import os
import pathlib
import subprocess
import sys


def main():
    base_dir = pathlib.Path(os.getcwd()).parent.parent

    result = subprocess.run(
        ["git", "-C", base_dir, "status"],
        capture_output=True, text=True
    )

    to_be_c_flag = False
    to_be_c = []

    not_staged_to_c_flag = False
    not_staged_to_c = []

    for line in result.stdout.split("\n"):
        if (line in [
            '  (use "git add <file>..." to update what will be committed)',
            '  (use "git restore <file>..." to discard changes in working directory)',
            '  (use "git restore --staged <file>..." to unstage)',
            ''
        ]):
            continue

        if line.startswith("Changes to be committed"):
            to_be_c_flag = True
            continue

        if line.startswith("Changes not staged for commit:"):
            to_be_c_flag = False
            not_staged_to_c_flag = True
            continue

        if line.startswith("Untracked files:"):
            break

        if to_be_c_flag:
            line = line.split(":")[1].strip()
            if line in [to_be_c, not_staged_to_c]:
                continue

            to_be_c.append(line)

        if not_staged_to_c_flag:
            line = line.split(":")[1].strip()
            if line in [to_be_c, not_staged_to_c]:
                continue

            not_staged_to_c.append(line)

    sh_script_content = []

    print("enter messages")

    for file in set(to_be_c + not_staged_to_c):
        desc = input(f"{file}\n")

        message = "git commit -m " + f'\"{" ".join(file.split("/"))} - {desc}\"'

        file_full_path = base_dir / file
        sh_script_content.append(f"git add {file_full_path}")
        sh_script_content.append(message)

    with open('git.sh', 'w+') as f:
        [f.write(f"{i}\n") for i in sh_script_content]


if __name__ == '__main__':
    main()
