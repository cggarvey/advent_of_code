import pathlib

THIS_PATH = pathlib.Path(__file__)
UTILS_DIR = THIS_PATH.parent
ROOT = UTILS_DIR.parent
DATA_DIR = ROOT.joinpath("data")


def get_data(filename, type_conv=str) -> list:

    data_path = DATA_DIR / filename

    with open(data_path, "r") as fh:
        lines = [type_conv(l.strip()) for l in fh.readlines()]

    return lines
