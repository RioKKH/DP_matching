#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import gaussian, convolve
from scipy.interpolate import interp1d
from dtw import dtw


def load_data(file_path: str) -> pd.DataFrame:
    """ファイルからデータを読み込む関数"""
    df = pd.read_csv(file_path, delim_whitespace=True, names=("freq", "amp"))
    return df


def apply_gaussian_filter(x, y, sigma=2.0):
    """ガウシアンフィルタを適用してノイズを抑制する関数"""
    window_size = int(sigma * 10)
