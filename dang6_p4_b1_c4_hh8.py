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


def bt_dang6_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ten = [
            ('A', 'B', 'C', 'I', 'D', 'E', 'M', 'N', 'P', 'Q'),
            ('A', 'B', 'C', 'O', 'H', 'K', 'E', 'F', 'M', 'N')
        ]
        A_t, B_t, C_t, I_t, D_t, E_t, M_t, N_t, P_t, Q_t = random.choice(bo_ten)

        noidungcauhoi = ('''Cho $\\Delta %s%s%s$, lấy điểm $%s$ bất kì nằm trong tam giác. Qua $%s$ kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$ và cắt $%s%s$ tại $%s$; kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$ và cắt $%s%s$ tại $%s$; kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$ và cắt $%s%s$ tại $%s$ (như hình vẽ bên dưới). Chứng minh rằng: \\\\
$\\dfrac{%s%s}{%s%s} + \\dfrac{%s%s}{%s%s} + \\dfrac{%s%s}{%s%s} = 2$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (I) at (2.2,1.2);
\\coordinate (P) at (1.25,2.0);
\\coordinate (Q) at (3.05,2.0);
\\coordinate (D) at (1.45,0);
\\coordinate (E) at (2.7,2.08);
\\coordinate (M) at (2.875,0);
\\coordinate (N) at (0.875,1.4);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (P)--(Q) (D)--(E) (M)--(N);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (I) circle (1pt) node[above left] {$%s$};
\\fill (D) circle (1pt) node[below] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\fill (M) circle (1pt) node[below] {$%s$};
\\fill (N) circle (1pt) node[left] {$%s$};
\\fill (P) circle (1pt) node[left] {$%s$};
\\fill (Q) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}'''
                         % (A_t, B_t, C_t, I_t, I_t, A_t, B_t, B_t, C_t, D_t, A_t, C_t, E_t,
                            A_t, C_t, B_t, C_t, M_t, A_t, B_t, N_t,
                            B_t, C_t, A_t, B_t, P_t, A_t, C_t, Q_t,
                            P_t, Q_t, B_t, C_t, D_t, E_t, A_t, B_t, M_t, N_t, A_t, C_t,
                            A_t, B_t, C_t, I_t, D_t, E_t, M_t, N_t, P_t, Q_t))

        s_template = '''Ta có các tứ giác $BDIP$ và $CMIQ$ là các hình bình hành (có các cặp cạnh đối song song), suy ra $PI = BD$ và $IQ = MC$. \\\\
Do đó: $\\dfrac{PQ}{BC} = \\dfrac{PI + IQ}{BC} = \\dfrac{BD}{BC} + \\dfrac{MC}{BC}$ (1). \\\\
Tương tự, với các hình bình hành $BNID$, $APIE$, $CEIM$, $AQIN$, ta cũng có: \\\\
$\\dfrac{DE}{AB} = \\dfrac{DI + IE}{AB} = \\dfrac{BN}{AB} + \\dfrac{AP}{AB}$ (2) và $\\dfrac{MN}{AC} = \\dfrac{MI + IN}{AC} = \\dfrac{CE}{AC} + \\dfrac{AQ}{AC}$ (3). \\\\
Mặt khác, theo định lí Thalès trong $\\Delta ABC$: \\\\
- Với $PQ // BC$: $\\dfrac{AP}{AB} = \\dfrac{IM}{BC}$ và $\\dfrac{AQ}{AC} = \\dfrac{ID}{BC}$; \\\\
- Với $DE // AB$: $\\dfrac{CE}{AC} = \\dfrac{IN}{AB}$ và $\\dfrac{CD}{BC} = \\dfrac{IE}{AB}$; \\\\
- Với $MN // AC$: $\\dfrac{BN}{AB} = \\dfrac{IP}{BC}$ và $\\dfrac{BM}{BC} = \\dfrac{IQ}{AC}$. \\\\
Từ (1), (2), (3), tách mỗi đoạn trên cạnh của $\\Delta ABC$ theo phần bù: \\\\
- Trên cạnh $BC$: $BD = BC - CD$ và $MC = BC - BM$, nên $\\dfrac{PQ}{BC} = \\dfrac{BC - CD}{BC} + \\dfrac{BC - BM}{BC} = 2 - \\dfrac{CD}{BC} - \\dfrac{BM}{BC}$. \\\\
- Theo định lí Thalès: $\\dfrac{CD}{BC} = \\dfrac{DE}{AB}$ (vì $DE // AB$) và $\\dfrac{BM}{BC} = \\dfrac{MN}{AC}$ (vì $MN // AC$). \\\\
Thay vào đẳng thức trên, ta được: $\\dfrac{PQ}{BC} = 2 - \\dfrac{DE}{AB} - \\dfrac{MN}{AC}$. \\\\
Chuyển vế, ta có: $\\dfrac{PQ}{BC} + \\dfrac{DE}{AB} + \\dfrac{MN}{AC} = 2$ (điều phải chứng minh).'''

        mapping = {
            'A': A_t, 'B': B_t, 'C': C_t, 'I': I_t,
            'D': D_t, 'E': E_t, 'M': M_t, 'N': N_t, 'P': P_t, 'Q': Q_t
        }
        loigiai = ''.join(mapping.get(ch, ch) for ch in s_template)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
