# -*- coding: utf-8 -*-
"""Show_ip_route_vtysh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vRrezmZ6fiZQvPeAnes1vNwD6FL5h92L
"""

from colorama import Fore, Back, Style
from subprocess import run
from subprocess import PIPE

BOLD = "\033[1m"
cols = ["Network", "Next Hop", "Metric", "LocPrf", "Weight", "Path"]
idxs = [0] + [
    "   Network          Next Hop            Metric LocPrf Weight Path".find(x)
    for x in cols
]


def split_rows(row):
    return [row[idx:nidx].strip() for idx, nidx in zip(idxs, idxs[1:] + [len(row)])]


def format_code(code, p):
    colors = {
        "i": Fore.YELLOW,
        "*": Fore.MAGENTA,
        ">": Fore.LIGHTGREEN_EX,
        " ": "",
        "?": Fore.RED,
    }
    res = ""
    l = p
    if ">" in code:
        res += Back.BLUE + BOLD
        l += len(Back.BLUE + BOLD)
    for c in code:
        res += colors[c] + c
        l += len(colors[c])
    return (res + Style.RESET_ALL).center(l + len(Style.RESET_ALL))


def format_table(table):
    clens = [max(col) for col in zip(*[[len(c) for c in row] for row in table])]
    headers = ["State"] + cols
    lens = [max(a, len(b)) for a, b in zip(clens, headers)]
    separator = "+" + "+".join(["-" * (l + 2) for l in lens]) + "+"
    headerstr = (
        "|"
        + "|".join(
            [
                " " + BOLD + header.center(l) + Style.RESET_ALL + " "
                for header, l in zip(headers, lens)
            ]
        )
        + "|"
    )
    print(guide)
    print(separator)
    print(headerstr)
    for n, row in enumerate(table):
        rowstr = "| " + format_code(row[0], lens[0]) + " "
        rowstr += (
            "|"
            + "|".join(
                [
                    " " + BOLD + Back.BLUE + c.center(l) + Style.RESET_ALL + " "
                    if ">" in row[0]
                    else " " + c.center(l) + " "
                    for c, l in zip(row[1:], lens[1:])
                ]
            )
            + "|"
        )
        if ">" in row[0]:
            print(separator)
        print(rowstr)
    print(separator)
    print(foot)


routers = input("Enter the router names separated by a space: ").split(" ")
for router in routers:
    print("=" * 60)
    print("=" * 60)
    print(BOLD + ("Router: " + router).center(60) + Style.RESET_ALL)
    print("=" * 60)
    # the comando to be executed is
    # lxc-attach -n router -- vtysh -c "show ip route"
    # the output of the command is stored in res
    output = run(
        ["lxc-attach", "-n", router, "--", "vtysh", "-c", "show ip route"],
        stdout=PIPE,
        stderr=PIPE,
    ).stdout
    res = output.decode("utf-8")
    guide = "\n".join(res.splitlines()[:4])
    rows = "\n".join(res.splitlines()[6:]).split("\n\n")[0].splitlines()
    foot = "\n".join(res.splitlines()[6:]).split("\n\n")[1]
    table = [split_rows(row) for row in rows]

    format_table(table)