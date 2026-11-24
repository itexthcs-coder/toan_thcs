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
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang19_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        oc = random.choice([60, 75, 90])
        oa = oc // 2
        ac = oa + oc
        bd = random.choice([60, 72, 84])
        ob = bd // 2
        oh = oc // 3
        ch = oc - oh
        mh = (2 * ob) // 3
        mn = 2 * mh

        noidungcauhoi = ("""Một khung cánh diều được làm bởi hai thanh tre thẳng vuông góc với nhau tại $O$ (trục dọc $AC = %s\\text{ cm}$ và thanh ngang $BD = %s\\text{ cm}$, trong đó $O$ là trung điểm của $BD$ và $OA = %s\\text{ cm}$, $OC = %s\\text{ cm}$). Để tăng độ cứng cho phần đuôi diều, người làm diều buộc thêm một thanh tre phụ $MN$ song song với thanh ngang $BD$ ($M \\in BC$, $N \\in DC$) sao cho thanh $MN$ cắt trục dọc $OC$ tại điểm $H$ cách điểm $O$ một khoảng $OH = %s\\text{ cm}$ (như hình vẽ bên dưới). \\\\
a) Tính tỉ số $\\dfrac{CH}{CO}$ và $\\dfrac{CM}{CB}$. \\\\
b) Tính độ dài đoạn thẳng $MH$ và suy ra tổng chiều dài thanh tre phụ $MN$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,3.6);
\\coordinate (O) at (0,2.4);
\\coordinate (C) at (0,0);
\\coordinate (B) at (-1.8,2.4);
\\coordinate (D) at (1.8,2.4);
\\coordinate (H) at (0,1.6);
\\coordinate (M) at ($(C)!0.6667!(B)$);
\\coordinate (N) at ($(C)!0.6667!(D)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D) (M)--(N);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (ac, bd, oa, oc, oh))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Ta có $CH = OC - OH = %s - %s = %s\\text{ (cm)}$, suy ra $\\dfrac{CH}{CO} = \\dfrac{%s}{%s} = \\dfrac{2}{3}$. \\\\
Xét $\\Delta COB$ có $MH // OB$ (vì $MN // BD$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{CM}{CB} = \\dfrac{CH}{CO} = \\dfrac{2}{3}$.
\\item Vì $O$ là trung điểm của $BD$ nên $OB = OD = \\dfrac{BD}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
Xét $\\Delta COB$ có $MH // OB$, theo định lí Thalès ta có: $\\dfrac{MH}{OB} = \\dfrac{CH}{CO} = \\dfrac{2}{3} \\Rightarrow MH = \\dfrac{2}{3} \\cdot %s = %s\\text{ (cm)}$. \\\\
Tương tự, xét $\\Delta COD$ có $NH // OD$, ta cũng có $NH = \\dfrac{2}{3} OD = %s\\text{ cm}$. \\\\
Vậy tổng chiều dài thanh tre phụ $MN$ là: $MN = MH + NH = %s + %s = %s\\text{ (cm)}$.
\\end{enumEX}"""
                   % (oc, oh, ch, ch, oc,
                      bd, ob, ob, mh, mh, mh, mh, mn))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
