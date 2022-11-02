import argparse
import re
import subprocess
import urllib.request
from typing import List, NamedTuple

pytorch_index_url = "https://download.pytorch.org/whl/torch_stable.html"


class Version(NamedTuple):
    major: int
    minor: int


def version_of(version_string: str) -> Version:
    match = re.match(r"(\d+)\.(\d+)", version_string)
    return Version(int(match.group(1)), int(match.group(2)))


def fetch(url: str) -> str:
    with urllib.request.urlopen(url) as response:
        return response.read().decode()


def fetch_available_cuda_versions() -> List[Version]:
    document = fetch(pytorch_index_url)
    versions = set(re.findall(r'href="cu(\d+)(\d)', document))
    return sorted(Version(int(major), int(minor)) for major, minor in versions)


def resolve_cuda_version(
    available_cuda_versions: List[Version], current_cuda_version: Version
) -> Version:
    resolved_cuda_version = None

    for available_cuda_version in available_cuda_versions:
        if available_cuda_version <= current_cuda_version:
            resolved_cuda_version = available_cuda_version
        else:
            break

    return resolved_cuda_version


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cuda", required=True)
    parser.add_argument("--torch", required=True)
    parser.add_argument("--torchaudio", required=True)
    parser.add_argument("--torchvision", required=True)
    arguments = parser.parse_args()

    cuda_version = version_of(arguments.cuda)
    available_cuda_versions = fetch_available_cuda_versions()
    reolsved_cuda_version = resolve_cuda_version(available_cuda_versions, cuda_version)

    subprocess.run(
        [
            "pip3",
            "install",
            "--no-cache-dir",
            f"--find-links={pytorch_index_url}",
            f"torch=={arguments.torch}+cu{reolsved_cuda_version.major}{reolsved_cuda_version.minor}",
            f"torchvision=={arguments.torchvision}+cu{reolsved_cuda_version.major}{reolsved_cuda_version.minor}",
            f"torchaudio=={arguments.torchaudio}+cu{reolsved_cuda_version.major}{reolsved_cuda_version.minor}",
        ],
        check=True,
    )
