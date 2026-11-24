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


def bt_dang5_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([10, 12])
        mn = 2 * k
        mp = 3 * k
        m_val = (mn // 2 - 2) // 2
        while (mn // 2 - 2) % 2 != 0:
            k = 12
            mn = 24
            mp = 36
            m_val = 5

        noidungcauhoi = ("""Cho $\\Delta MNP$ có $MN = %s\\text{ cm}$, $MP = %s\\text{ cm}$. Trên cạnh $MN$ lấy điểm $E$ sao cho $ME = 2m + 2\\text{ (cm)}$, trên cạnh $MP$ lấy điểm $F$ sao cho $MF = 3m + 3\\text{ (cm)}$ (với $0 < m < %s$). \\\\
a) Chứng minh rằng đường thẳng $EF$ luôn song song với cạnh $NP$ với mọi giá trị $m$ thỏa mãn điều kiện. \\\\
b) Tìm giá trị của $m$ để $EF$ đi qua trung điểm của cạnh $MN$."""
                         % (mn, mp, mn // 2 - 1))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Xét $\\Delta MNP$ có $E \\in MN$, $F \\in MP$, ta có: \\\\
$\\dfrac{ME}{MN} = \\dfrac{2m + 2}{%s} = \\dfrac{2(m + 1)}{%s} = \\dfrac{m + 1}{%s}$ và $\\dfrac{MF}{MP} = \\dfrac{3m + 3}{%s} = \\dfrac{3(m + 1)}{%s} = \\dfrac{m + 1}{%s}$. \\\\
Vì $\\dfrac{ME}{MN} = \\dfrac{MF}{MP}$ với mọi $m$ thỏa mãn điều kiện nên $EF // NP$ (theo định lí Thalès đảo).
\\item Để $EF$ đi qua trung điểm của cạnh $MN$ thì $E$ phải là trung điểm của $MN$, tức là: \\\\
$ME = \\dfrac{MN}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
Suy ra $2m + 2 = %s \\Leftrightarrow 2m = %s \\Leftrightarrow m = %s$ (thỏa mãn điều kiện). \\\\
Vậy $m = %s$ thì $EF$ đi qua trung điểm của cạnh $MN$.
\\end{enumEX}"""
                   % (mn, mn, k, mp, mp, k,
                      mn, mn // 2, mn // 2, mn // 2 - 2, m_val, m_val))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
