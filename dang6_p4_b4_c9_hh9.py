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


def bt_dang6_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        he_so = random.choice([1, 2, 3, 4])
        canh_nho_str = "a" if he_so == 1 else "%sa" % (he_so)
        canh_lon_str = "2a" if he_so == 1 else "%sa" % (2 * he_so)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (2.4,0);
\\coordinate (C) at (3.6,2.078);
\\coordinate (D) at (1.2,2.078);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (P) at ($(C)!0.5!(D)$);
\\coordinate (Q) at ($(D)!0.5!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (M)--(Q) (N)--(P);
\\draw[line width=1pt, dashed] (B)--(D);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[above] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho hình thoi $ABCD$ có $\\widehat{A} = 60^\\circ$ và độ dài cạnh bằng $%s$ ($a > 0$). Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$ (như hình vẽ). Chứng minh rằng lục giác $MBNPDQ$ là một lục giác đều và tính bán kính đường tròn ngoại tiếp lục giác đều đó theo $a$. %s'''
                         % (canh_lon_str, hinh_tikz))

        loigiai = ('''Hình thoi $ABCD$ có $AB = AD = %s$ và $\\widehat{A} = 60^\\circ$ nên $\\triangle ABD$ là tam giác đều cạnh $%s$, suy ra $BD = %s$. \\\\
Vì $M, Q$ lần lượt là trung điểm của $AB, AD$ nên $MQ$ là đường trung bình của $\\triangle ABD$, do đó $MQ = \\frac{1}{2}BD = %s$. Tương tự $NP = \\frac{1}{2}BD = %s$. \\\\
Mặt khác $MB = BN = PD = DQ = \\frac{%s}{2} = %s$, nên lục giác lồi $MBNPDQ$ có $6$ cạnh bằng nhau và đều bằng $%s$. \\\\
Xét $\\triangle AMQ$ có $AM = AQ = %s$ và $\\widehat{A} = 60^\\circ$ nên $\\triangle AMQ$ đều, suy ra $\\widehat{AMQ} = \\widehat{AQM} = 60^\\circ$. \\\\
Từ đó $\\widehat{QMB} = 180^\\circ - 60^\\circ = 120^\\circ$ và $\\widehat{DQM} = 180^\\circ - 60^\\circ = 120^\\circ$. Tương tự $\\widehat{BNP} = \\widehat{DPN} = 120^\\circ$. \\\\
Lại có $\\widehat{B} = \\widehat{D} = 180^\\circ - \\widehat{A} = 120^\\circ$. Vậy $6$ góc trong của lục giác $MBNPDQ$ đều bằng $120^\\circ$, do đó $MBNPDQ$ là một lục giác đều. \\\\
Vì bán kính đường tròn ngoại tiếp lục giác đều bằng độ dài cạnh của nó nên bán kính cần tìm là $R = %s$.'''
                   % (canh_lon_str, canh_lon_str, canh_lon_str, canh_nho_str, canh_nho_str, canh_lon_str, canh_nho_str, canh_nho_str, canh_nho_str, canh_nho_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
