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


def bt_dang7_p4_b3_c5_hh9(self):
    # Dạng 7: Liên hệ góc nội tiếp và góc ở tâm để tính độ dài cung và diện tích hình quạt tròn
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([3, 6, 9, 12])
        gocA = random.choice([45, 50, 60])
        gocB = random.choice([65, 70, 75])
        gocC = 180 - gocA - gocB
        sd_BC = 2 * gocA
        sd_AC = 2 * gocB
        sd_AB = 2 * gocC
        l_BC = Rational(sd_BC, 180) * sp.pi * R
        l_AC = Rational(sd_AC, 180) * sp.pi * R
        l_AB = Rational(sd_AB, 180) * sp.pi * R
        S_qAB = Rational(sd_AB, 360) * sp.pi * R**2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O; %s\\text{ cm})$.\\\\
a) Kẻ đường kính $AD$ của $(O)$. Bằng cách xét các tam giác cân $OAB$ và $OAC$, hãy chứng minh rằng $\\widehat{BOC} = 2\\widehat{BAC}$.\\\\
b) Biết $\\widehat{BAC} = %s^\\circ$ và $\\widehat{ABC} = %s^\\circ$. Tính độ dài các cung nhỏ $BC, AC, AB$ và diện tích hình quạt tròn $OAB$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[blue!16] (0,0) -- (95:1.8) arc (95:215:1.8) -- cycle;
\\draw[thick] (0,0) circle (1.8);
\\draw[thick] (95:1.8) -- (215:1.8) -- (-35:1.8) -- cycle;
\\draw[dashed] (95:1.8) -- (-85:1.8) (0,0) -- (215:1.8) (0,0) -- (-35:1.8);
\\fill (0,0) circle (1.5pt) node[right] {$O$};
\\fill (95:1.8) circle (1.5pt) node[above] {$A$};
\\fill (215:1.8) circle (1.5pt) node[left] {$B$};
\\fill (-35:1.8) circle (1.5pt) node[right] {$C$};
\\fill (-85:1.8) circle (1.5pt) node[below] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(gocA), latex(gocB)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $OA = OB = R$ nên $\\Delta OAB$ cân tại $O$, suy ra $\\widehat{OAB} = \\widehat{OBA}$.\\\\
Xét $\\Delta OAB$ có $\\widehat{BOD}$ là góc ngoài tại đỉnh $O$ nên:
$$\\widehat{BOD} = \\widehat{OAB} + \\widehat{OBA} = 2\\widehat{OAB}.$$
Chứng minh tương tự đối với $\\Delta OAC$ cân tại $O$, ta có $\\widehat{COD} = 2\\widehat{OAC}$.\\\\
Vì $\\Delta ABC$ nhọn nên tâm $O$ nằm bên trong $\\Delta ABC$, tia $OD$ nằm giữa hai tia $OB, OC$. Cộng vế theo vế hai đẳng thức trên, ta được:
$$\\widehat{BOC} = \\widehat{BOD} + \\widehat{COD} = 2(\\widehat{OAB} + \\widehat{OAC}) = 2\\widehat{BAC}.$$
\\item Trong $\\Delta ABC$, ta có:
$$\\widehat{ACB} = 180^\\circ - (\\widehat{BAC} + \\widehat{ABC}) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ.$$
Áp dụng kết quả câu a, số đo các góc ở tâm chắn các cung nhỏ $BC, AC, AB$ lần lượt là:
$$\\widehat{BOC} = 2\\widehat{BAC} = %s^\\circ; \\quad \\widehat{AOC} = 2\\widehat{ABC} = %s^\\circ; \\quad \\widehat{AOB} = 2\\widehat{ACB} = %s^\\circ.$$
Độ dài các cung nhỏ $BC, AC, AB$ lần lượt là:
$$l_{BC} = \\dfrac{%s}{180}\\pi \\cdot %s = %s\\text{ (cm)}; \\quad l_{AC} = \\dfrac{%s}{180}\\pi \\cdot %s = %s\\text{ (cm)}; \\quad l_{AB} = \\dfrac{%s}{180}\\pi \\cdot %s = %s\\text{ (cm)}.$$
Diện tích hình quạt tròn $OAB$ ứng với cung nhỏ $AB$ ($%s^\\circ$) là:
$$S_q = \\dfrac{%s}{360}\\pi \\cdot %s^2 = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(gocA), latex(gocB), latex(gocC),
                      latex(sd_BC), latex(sd_AC), latex(sd_AB),
                      latex(sd_BC), latex(R), latex(l_BC),
                      latex(sd_AC), latex(R), latex(l_AC),
                      latex(sd_AB), latex(R), latex(l_AB),
                      latex(sd_AB), latex(sd_AB), latex(R), latex(S_qAB)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
