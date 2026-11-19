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


def bt_dang12_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_goc = [
            (34, 26),
            (38, 22),
            (42, 18),
            (46, 24),
            (30, 20)
        ]
        bec, dfc = random.choice(bo_goc)
        tong_ef = bec + dfc
        bad = (180 - tong_ef) // 2
        bcd = 180 - bad
        adc = bad + dfc
        abc = 180 - adc

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (155:1.3);
\\coordinate (B) at (245:1.3);
\\coordinate (C) at (-20:1.3);
\\coordinate (D) at (45:1.3);
\\coordinate (E) at (intersection of A--B and D--C);
\\coordinate (F) at (intersection of A--D and B--C);
\\draw[line width=1pt] (O) circle (1.3);
\\draw[line width=1pt] (A)--(E)--(D)--(F)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above] {$D$};
\\fill (E) circle (1pt) node[below] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$ sao cho các tia $AB$ và $DC$ cắt nhau tại $E$, các tia $AD$ và $BC$ cắt nhau tại $F$ (như hình vẽ). Biết rằng $\\widehat{BEC} = %s^\\circ$ và $\\widehat{DFC} = %s^\\circ$. Tính số đo bốn góc trong của tứ giác $ABCD$. %s'''
                         % (bec, dfc, hinh_tikz))

        loigiai = ('''Xét $\\triangle EAD$ có góc ngoài tại đỉnh $D$ là $\\widehat{EDC} = \\widehat{BAD} + \\widehat{BEC} = \\widehat{BAD} + %s^\\circ$. \\
Xét $\\triangle FDC$ có góc ngoài tại đỉnh $C$ là:
$$\\widehat{BCD} = \\widehat{EDC} + \\widehat{DFC} = \\widehat{BAD} + %s^\\circ + %s^\\circ = \\widehat{BAD} + %s^\\circ.$$
Vì tứ giác $ABCD$ nội tiếp đường tròn $(O)$ nên tổng hai góc đối diện bằng $180^\\circ$:
$$\\widehat{BAD} + \\widehat{BCD} = 180^\\circ \\Rightarrow 2\\widehat{BAD} + %s^\\circ = 180^\\circ \\Rightarrow \\widehat{BAD} = %s^\\circ.$$
Suy ra $\\widehat{BCD} = 180^\\circ - %s^\\circ = %s^\\circ$. \\
Mặt khác, $\\widehat{ADC} = 180^\\circ - \\widehat{EDC} = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$. \\
Do đó $\\widehat{ABC} = 180^\\circ - \\widehat{ADC} = 180^\\circ - %s^\\circ = %s^\\circ$. \\
Vậy số đo bốn góc trong của tứ giác $ABCD$ là $\\widehat{BAD} = %s^\\circ$, $\\widehat{ABC} = %s^\\circ$, $\\widehat{BCD} = %s^\\circ$, $\\widehat{ADC} = %s^\\circ$.'''
                   % (bec, bec, dfc, tong_ef, tong_ef, bad, bad, bcd, bad, bec, adc, adc, abc, bad, abc, bcd, adc))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
