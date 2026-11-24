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


def bt_dang10_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = random.choice([3, 4])
        n = random.choice([2, 3])
        # AD = 1/m AB => DB = (m-1)/m AB => AD/DB = 1/(m-1)
        # AE = 1/n AC => EC = (n-1)/n AC
        # DK // BE => AK / KE = AD / DB = 1 / (m - 1) => KE = (m - 1) AK => AE = m * AK => KE = (m - 1)/m AE
        # EC = (n - 1) AE => KE / EC = (m - 1) / (m * (n - 1))
        # OC / OD = EC / KE = (m * (n - 1)) / (m - 1)
        ts_ak_ke = Rational(1, m - 1)
        ts_ke_ec = Rational(m - 1, m * (n - 1))
        ts_oc_od = Rational(m * (n - 1), m - 1)

        noidungcauhoi = ("""Cho $\\Delta ABC$, trên cạnh $AB$ lấy điểm $D$ sao cho $AD = \\dfrac{1}{%s} AB$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = \\dfrac{1}{%s} AC$. Gọi $O$ là giao điểm của $BE$ và $CD$. Qua $D$ kẻ đường thẳng song song với $BE$ cắt $AC$ tại $K$ (như hình vẽ bên dưới). \\\\
a) Tính tỉ số $\\dfrac{AK}{KE}$ và $\\dfrac{KE}{EC}$. \\\\
b) Tính tỉ số $\\dfrac{OC}{OD}$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at ($(A)!0.25!(B)$);
\\coordinate (E) at ($(A)!0.3333!(C)$);
\\coordinate (O) at (intersection of B--E and C--D);
\\coordinate (K) at ($(A)!0.25!(E)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(E) (C)--(D);
\\draw[line width=1pt, dashed] (D)--(K);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (K) circle (1pt) node[right] {$K$};
\\end{tikzpicture}
\\end{center}"""
                         % (m, n))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Vì $AD = \\dfrac{1}{%s} AB$ nên $DB = \\dfrac{%s}{%s} AB$, suy ra $\\dfrac{AD}{DB} = \\dfrac{1}{%s}$. \\\\
Xét $\\Delta ABE$ có $DK // BE$, theo định lí Thalès trong tam giác ta có: $\\dfrac{AK}{KE} = \\dfrac{AD}{DB} = %s$. \\\\
Từ đó suy ra $KE = %s AK \\Rightarrow AE = AK + KE = %s AK \\Rightarrow KE = \\dfrac{%s}{%s} AE$. \\\\
Mặt khác $AE = \\dfrac{1}{%s} AC \\Rightarrow EC = %s AE$. \\\\
Vậy $\\dfrac{KE}{EC} = \\dfrac{\\dfrac{%s}{%s} AE}{%s AE} = %s$.
\\item Xét $\\Delta CDK$ có $OE // DK$ (vì $BE // DK$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{OC}{OD} = \\dfrac{EC}{KE} = %s$.
\\end{enumEX}"""
                   % (m, m - 1, m, m - 1,
                      latex(ts_ak_ke),
                      m - 1, m, m - 1, m,
                      n, n - 1,
                      m - 1, m, n - 1, latex(ts_ke_ec),
                      latex(ts_oc_od)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
