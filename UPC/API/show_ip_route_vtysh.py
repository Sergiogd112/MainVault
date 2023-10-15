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


def split_rows(row):
    data = row.replace("  ", " ").replace("  ", " ").split(" ")
    Code = data[0].strip()
    network = data[1].strip()
    if network == "*":
        Code = "*"
        network = '" " "'
    i = 2
    connected = False
    cost = "x"
    if "[" in row:
        cost = data[2].strip()
        i = 3
    data2 = " ".join(data[i:]).split(",")
    via = (
        data2[0]
        .replace("via ", "")
        .replace("is directly connected", "direct connect")
        .strip()
    )
    interface = data2[1].strip()
    age = "x"
    if ":" in row:
        age = data2[2].strip()
    return [Code, network, cost, via, interface, age]


def format_code(code, p):
    colors = {
        "O": Fore.YELLOW,
        "C": Fore.CYAN,
        "R": Fore.MAGENTA,
        "K": Fore.WHITE,
        "S": Fore.LIGHTBLACK_EX,
        "I": Fore.LIGHTWHITE_EX,
        "B": Fore.LIGHTRED_EX,
        "*": Fore.WHITE,
        ">": Fore.LIGHTMAGENTA_EX,
    }
    res = ""
    l = p
    if ">" in code:
        res += Back.LIGHTBLACK_EX + BOLD
        l += len(Back.LIGHTBLACK_EX + BOLD)
    for c in code:
        res += colors[c] + c
        l += len(colors[c])
    return (res + Style.RESET_ALL).center(l + len(Style.RESET_ALL))


def format_table(table):
    clens = [max(col) for col in zip(*[[len(c) for c in row] for row in table])]
    headers = "Code,Network,Cost,Next-hop,Iface,Age".split(",")
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
    print(separator)
    print(headerstr)
    for n, row in enumerate(table):
        rowstr = "| " + format_code(row[0], lens[0]) + " "
        rowstr += (
            "|"
            + "|".join(
                [
                    " "
                    + BOLD
                    + Back.LIGHTBLACK_EX
                    + c.center(l)
                    + Style.RESET_ALL
                    + " "
                    if ">" in row[0]
                    else " " + c.center(l) + " "
                    for c, l in zip(row[1:], lens[1:])
                ]
            )
            + "|"
        )
        if not ('"' in row[1]):
            print(separator)
        print(rowstr)
    print(separator)


routers = input("Enter the router names separated by a space: ").split(" ")
for router in routers:
    print("=" * 20)
    print("=" * 20)
    print(BOLD + "Router: ", router + Style.RESET_ALL)
    print("=" * 20)
    # the comando to be executed is
    # lxc-attach -n router -- vtysh -c "show ip route"
    # the output of the command is stored in res
    output = run(
        ["lxc-attach", "-n", router, "--", "vtysh", "-c", "show ip route"],
        stdout=PIPE,
        stderr=PIPE,
    ).stdout
    res = output.decode("utf-8")
    guide = "\n".join(res.splitlines()[:3])
    rows = res.splitlines()[4:]
    table = [split_rows(row) for row in rows]

format_table(table)
