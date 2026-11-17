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


def bt_dang3_p4_b3_c5_hh9(self):
    # Dạng 3: Tính số đo cung và diện tích phần hình phẳng giới hạn bởi tiếp tuyến chung ngoài và hai cung tròn tiếp xúc ngoài
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(2, 6)
        R = 3 * r
        O1O2 = R + r
        O1H = R - r
        BC_sym = 2 * r * sqrt(3)
        S_thang = Rational(1, 2) * (R + r) * BC_sym
        S_q1 = Rational(60, 360) * sp.pi * R**2
        S_q2 = Rational(120, 360) * sp.pi * r**2
        S_tong_q = S_q1 + S_q2
        S_conlai = S_thang - S_tong_q

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ tiếp xúc ngoài tại $A$. Kẻ tiếp tuyến chung ngoài $BC$ của hai đường tròn ($B \\in (O_1)$, $C \\in (O_2)$).\\\\
a) Tính số đo các góc ở tâm $\\widehat{BO_1A}$ và $\\widehat{CO_2A}$.\\\\
b) Tính diện tích phần hình phẳng giới hạn bởi đoạn thẳng $BC$ và hai cung nhỏ $AB, AC$.
\\begin{center}
\\begin{tikzpicture}[scale=0.75, >=stealth, line join=round, line cap=round, font=\\footnotesize]
\\fill[orange!20] (60:2.1) -- (3.15,0.606) arc (60:180:0.7) arc (0:60:2.1) -- cycle;
\\draw[thick] (0,0) circle (2.1);
\\draw[thick] (2.8,0) circle (0.7);
\\draw[thick] (60:2.1) -- (3.15,0.606);
\\draw[dashed] (0,0) -- (2.8,0) (0,0) -- (60:2.1) (2.8,0) -- (3.15,0.606);
\\fill (0,0) circle (1.5pt) node[left] {$O_1$};
\\fill (2.8,0) circle (1.5pt) node[right] {$O_2$};
\\fill (2.1,0) circle (1.5pt) node[below left] {$A$};
\\fill (60:2.1) circle (1.5pt) node[above] {$B$};
\\fill (3.15,0.606) circle (1.5pt) node[above right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(R), latex(r)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì hai đường tròn tiếp xúc ngoài tại $A$ nên $O_1, A, O_2$ thẳng hàng và $O_1O_2 = R + r = %s + %s = %s\\text{ (cm)}$.\\\\
Vì $BC$ là tiếp tuyến chung ngoài nên $O_1B \\perp BC$ và $O_2C \\perp BC$, suy ra $O_1B \\parallel O_2C$.\\\\
Kẻ $O_2H \\perp O_1B$ tại $H$, khi đó $O_2HBC$ là hình chữ nhật nên $BH = O_2C = %s\\text{ cm}$ và $O_1H = O_1B - BH = %s - %s = %s\\text{ (cm)}$.\\\\
Trong $\\Delta O_1HO_2$ vuông tại $H$, ta có:
$$\\cos \\widehat{HO_1O_2} = \\dfrac{O_1H}{O_1O_2} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{BO_1A} = 60^\\circ.$$
Vì $O_1B \\parallel O_2C$ nên hai góc trong cùng phía bù nhau:
$$\\widehat{CO_2A} = 180^\\circ - 60^\\circ = 120^\\circ.$$
\\item Áp dụng định lí Pythagore trong $\\Delta O_1HO_2$ vuông tại $H$, ta có:
$$BC = O_2H = \\sqrt{O_1O_2^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Diện tích hình thang vuông $O_1BCO_2$ là:
$$S_{O_1BCO_2} = \\dfrac{(O_1B + O_2C) \\cdot BC}{2} = \\dfrac{(%s + %s) \\cdot %s}{2} = %s\\text{ (cm}^2\\text{)}.$$
Tổng diện tích hai hình quạt tròn $O_1BA$ và $O_2CA$ là:
$$S_{q_1} + S_{q_2} = \\dfrac{60}{360}\\pi \\cdot %s^2 + \\dfrac{120}{360}\\pi \\cdot %s^2 = %s + %s = %s\\text{ (cm}^2\\text{)}.$$
Vậy diện tích phần hình phẳng cần tìm là:
$$S = S_{O_1BCO_2} - (S_{q_1} + S_{q_2}) = %s\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (latex(R), latex(r), latex(O1O2),
                      latex(r), latex(R), latex(r), latex(O1H),
                      latex(O1H), latex(O1O2),
                      latex(O1O2), latex(O1H), latex(BC_sym),
                      latex(R), latex(r), latex(BC_sym), latex(S_thang),
                      latex(R), latex(r), latex(S_q1), latex(S_q2), latex(S_tong_q),
                      latex(S_conlai)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
