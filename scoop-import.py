import concurrent.futures
import json
import os
import sys

import tqdm

scoop_json_path = sys.argv[1]

cpu_count = os.cpu_count() or 4
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


def run_cmd(cmd):
    os.system(cmd)


with tqdm.tqdm(total=len(commands)) as pbar:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for result in executor.map(run_cmd, commands):
            pbar.update()

print("Done")
