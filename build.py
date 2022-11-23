#!/usr/bin/env python3

import json
import subprocess
import sys
import time
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List


def retry(number_of_attempts: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, number_of_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exception:
                    if attempt >= number_of_attempts:
                        raise exception

                    print("An error occurred:", exception)
                    print("Retry after 15 seconds...")
                    time.sleep(15)

        return wrapper

    return decorator


def load_config(filename: str) -> Dict[str, Any]:
    with open(filename, "r", encoding="utf-8") as input_file:
        config = json.load(input_file)

    for build in config["builds"]:
        build["dockerfile_path"] = Path(build["dockerfile"])

        if "arguments" not in build:
            build["arguments"] = {}

    return config


def generate_readme(filename: str, config: Dict[str, Any]):
    def title_of(dockerfile_path: Path) -> str:
        if dockerfile_path.name == "Dockerfile":
            return str(dockerfile_path.parent)
        elif dockerfile_path.suffix == ".Dockerfile":
            return str(dockerfile_path.with_suffix(""))
        else:
            return str(dockerfile_path)

    tags_by_dockerfile_path = OrderedDict()
    for item in config["builds"]:
        tags_by_dockerfile_path.setdefault(item["dockerfile_path"], []).extend(
            item["tags"]
        )

    with open(filename, "w", encoding="utf-8") as output_file:
        print("# Dockerfiles", file=output_file)

        for dockerfile_path, tags in tags_by_dockerfile_path.items():
            print(f"## {title_of(dockerfile_path)}", file=output_file)
            for tag in tags:
                print(f"- `{tag}`", file=output_file)
            print(file=output_file)


@retry(number_of_attempts=3)
def build(
    dockerfile_path: Path,
    arguments: Dict[str, str],
    tags: List[str],
    options: List[str],
):
    print(f"# Building {', '.join(tags)}")
    command = ["docker", "build"]
    command.append(f"--file={dockerfile_path}")
    command.extend(options)

    for key, value in arguments.items():
        command.append("--build-arg")
        command.append(f"{key}={value}")

    command.extend([f"--tag={tag}" for tag in tags])
    command.append(str(dockerfile_path.parent))

    subprocess.run(command, check=True)
    print()

@retry(number_of_attempts=3)
def push(tags: List[str]):
    for tag in tags:
        print(f"# Pushing {tag}")
        subprocess.run(["docker", "push", tag], check=True, timeout=600)
        print()

if __name__ == "__main__":
    build_options = sys.argv[1:]

    config = load_config("config.json")
    generate_readme("README.md", config)

    for item in config["builds"]:
        build(
            dockerfile_path=item["dockerfile_path"],
            arguments=item["arguments"],
            tags=item["tags"],
            options=build_options,
        )
        push(tags=item["tags"])
