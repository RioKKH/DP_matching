#!/usr/bin/env python
# coding: utf-8

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# matplotlib.use("TkAgg")


def load(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, delim_whitespace=True, names=("freq", "peak"), index_col=0)
    # df = pd.read_csv(file, sep="\s+", names=("freq", "peak"), index_col=0)
    return df


def load_datas() -> list[pd.DataFrame]:
    xt = load("s_Xt.dat")
    yt = load("s_Yt.dat")
    mt = load("s_Mt.dat")
    nt = load("s_Nt.dat")
    return [xt, yt, mt, nt]


def plot() -> None:
    xt, yt, mt, nt = load_datas()
    fig, ax = plt.subplots()

    xt.plot(y="peak", ax=ax, marker="o", alpha=0.8, label="x")
    yt.plot(y="peak", ax=ax, marker="o", alpha=0.8, label="y")
    mt.plot(y="peak", ax=ax, marker="o", alpha=0.8, label="on")
    nt.plot(y="peak", ax=ax, marker="o", alpha=0.8, label="off")
    plt.legend()
    plt.grid(ls="dashed", color="gray", alpha=0.5)

    plt.show()


if __name__ == "__main__":
    plot()
