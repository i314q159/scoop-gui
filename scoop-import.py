import concurrent.futures
import json
import os
import time


def run_cmd(command):
    os.system(command)


if __name__ == '__main__':
    scoop_json_path = "./scoop.json"
    cpu_count = os.cpu_count() or 8
    max_workers = cpu_count * 3

    with open(scoop_json_path, encoding="utf-16", newline="\n") as f:
        data = json.load(f)

    apps = data["apps"]

    commands = []
    for app in apps:
        name = app["Name"]
        source = app["Source"]
        cmd = f"scoop install {source}/{name}"
        commands.append(cmd)

    os.system("scoop update")

    t1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(run_cmd, commands)
    t2 = time.time()
    print(f"{(t2 - t1) * 1000:.2f} ms")
