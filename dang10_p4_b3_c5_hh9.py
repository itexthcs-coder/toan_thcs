# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import qrcode
import glob
import base64
from datetime import datetime, timedelta
from sympy import symbols, solve, Lt
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sympy.abc import x, y, z, t
from math import degrees
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps


def bt_dang10_p4_b3_c5_hh9(self):
    # Dạng 10: Tính quãng đường di chuyển và diện tích quét qua khi quấn sợi dây quanh tam giác đều
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(3, 8)
        L_day = 3 * a
        r1, r2, r3 = 3 * a, 2 * a, a
        l_tong = Rational(120, 180) * sp.pi * (r1 + r2 + r3)
        S_tong = Rational(120, 360) * sp.pi * (r1**2 + r2**2 + r3**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác đều $ABC$ có cạnh bằng $%s\\text{ cm}$. Một sợi dây mảnh không co dãn có chiều dài $%s\\text{ cm}$ được buộc cố định một đầu tại đỉnh $A$, ban đầu sợi dây được căng thẳng dọc theo tia đối của tia $AB$ (đầu tự do $M$ nằm trên tia đối của tia $AB$ sao cho $AM = %s\\text{ cm}$). Người ta quấn sợi dây ngược chiều kim đồng hồ xung quanh tam giác đều $ABC$ cho đến khi đầu dây $M$ chạm vào đỉnh $A$.\\\\
a) Xác định bán kính và số đo góc ở tâm của từng cung tròn tạo nên quỹ đạo của đầu dây $M$.\\\\
b) Tính tổng độ dài quãng đường đầu dây $M$ đã di chuyển và diện tích vùng mặt phẳng mà sợi dây đã quét qua.
\\begin{center}
\\begin{tikzpicture}[scale=0.65, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[green!12] (0,0) -- (-2.4,0) arc (180:60:2.4) -- cycle;
\\fill[blue!12] (0.4,0.693) -- (1.2,2.078) arc (60:-60:1.6) -- cycle;
\\fill[red!12] (0.8,0) -- (1.2,-0.693) arc (-60:-180:0.8) -- cycle;
\\draw[thick, fill=gray!25] (0,0) -- (0.8,0) -- (0.4,0.693) -- cycle;
\\draw[thick, blue!80!black] (-2.4,0) arc (180:60:2.4) arc (60:-60:1.6) arc (-60:-180:0.8);
\\draw[dashed] (0,0) -- (-2.4,0);
\\fill (-2.4,0) circle (1.8pt) node[below] {$M$};
\\node[below] at (0,0) {$A$};
\\node[below right] at (0.8,0) {$B$};
\\node[left] at (0.35,0.85) {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(a), latex(L_day), latex(L_day)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $\\Delta ABC$ đều nên mỗi góc trong bằng $60^\\circ$, suy ra mỗi góc ngoài tại các đỉnh $A, C, B$ đều bằng $180^\\circ - 60^\\circ = 120^\\circ$.\\\\
Khi quấn sợi dây ngược chiều kim đồng hồ quanh $\\Delta ABC$, quỹ đạo của đầu dây $M$ gồm $3$ cung tròn liên tiếp đều có số đo $120^\\circ$:
\\begin{itemize}
\\item Cung thứ nhất có tâm $A$, bán kính $R_1 = %s\\text{ cm}$ (dây chạm vào cạnh $AC$).
\\item Cung thứ hai có tâm $C$, bán kính $R_2 = %s - %s = %s\\text{ cm}$ (dây chạm vào cạnh $CB$).
\\item Cung thứ ba có tâm $B$, bán kính $R_3 = %s - %s = %s\\text{ cm}$ (đầu dây $M$ chạm vào đỉnh $A$).
\\end{itemize}
\\item Tổng độ dài quãng đường đầu dây $M$ đã di chuyển là:
$$l = \\dfrac{120}{180}\\pi(R_1 + R_2 + R_3) = \\dfrac{2}{3}\\pi(%s + %s + %s) = %s\\text{ (cm)}.$$
Tổng diện tích vùng mặt phẳng mà sợi dây đã quét qua bằng tổng diện tích ba hình quạt tròn tương ứng:
$$S = \\dfrac{120}{360}\\pi(R_1^2 + R_2^2 + R_3^2) = \\dfrac{1}{3}\\pi(%s^2 + %s^2 + %s^2) = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(r1),
                      latex(r1), latex(a), latex(r2),
                      latex(r2), latex(a), latex(r3),
                      latex(r1), latex(r2), latex(r3), latex(l_tong),
                      latex(r1), latex(r2), latex(r3), latex(S_tong)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
