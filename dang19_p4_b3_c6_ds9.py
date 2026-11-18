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


def bt_dang19_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            k_ti_le = randint(3, 5)
            r_dat = randint(15, 25)
            d_dat = randint(r_dat + 5, 40)
            S_dat = r_dat * d_dat
            if (S_dat * k_ti_le) % (k_ti_le + 1) == 0:
                S_vuon = (S_dat * k_ti_le) // (k_ti_le + 1)
                S_ao = S_dat - S_vuon
                break
                
        chu_vi = 2 * (d_dat + r_dat)
        nua_chu_vi = d_dat + r_dat
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Bác Minh có một khu đất hình chữ nhật $ABCD$ có chu vi là $%s\\text{ m}$. Bác dự định chia khu đất thành hai phần: một phần để đào ao thả cá và phần còn lại làm vườn trồng cây ăn quả sao cho diện tích ao bằng $\\dfrac{1}{%s}$ diện tích vườn (như hình vẽ). Biết rằng diện tích của phần vườn trồng cây ăn quả là $%s\\text{ m}^{2}$. Hãy tính chiều dài và chiều rộng của khu đất ban đầu.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4.5,0);
\\coordinate (C) at (4.5,2.5);
\\coordinate (D) at (0,2.5);
\\coordinate (M) at (1.2,0);
\\coordinate (N) at (1.2,2.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[above] {$N$};
\\node at (0.6,1.25) {Ao};
\\node at (2.85,1.25) {Vườn};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(chu_vi), latex(k_ti_le), latex(S_vuon)))
        
        # Nội dung lời giải
        loigiai = ('''Vì diện tích ao bằng $\\dfrac{1}{%s}$ diện tích vườn nên diện tích ao là: \\\\
$S_{\\text{ao}} = \\dfrac{1}{%s} \\cdot %s = %s\\text{ (m}^{2}\\text{)}$. \\\\
Tổng diện tích của cả khu đất hình chữ nhật $ABCD$ là: \\\\
$S = S_{\\text{ao}} + S_{\\text{vườn}} = %s + %s = %s\\text{ (m}^{2}\\text{)}$. \\\\
Nửa chu vi của khu đất hình chữ nhật là: $\\dfrac{%s}{2} = %s\\text{ (m)}$. \\\\
Gọi chiều dài và chiều rộng của khu đất lần lượt là $x_{1}$ (m) và $x_{2}$ (m) ($x_{1} > x_{2} > 0$). \\\\
Ta có: $\\begin{cases} x_{1} + x_{2} = %s \\\\ x_{1}x_{2} = %s \\end{cases}$. \\\\
Do đó, $x_{1}$ và $x_{2}$ là hai nghiệm của phương trình bậc hai: $x^{2} - %sx + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0 \\Rightarrow \\sqrt{\\Delta} = %s$. \\\\
Phương trình có hai nghiệm phân biệt là $x_{1} = %s$ và $x_{2} = %s$ (thỏa mãn $x_{1} > x_{2} > 0$). \\\\
Vậy chiều dài của khu đất là $%s\\text{ m}$ và chiều rộng của khu đất là $%s\\text{ m}$.'''
                   % (latex(k_ti_le),
                      latex(k_ti_le), latex(S_vuon), latex(S_ao),
                      latex(S_ao), latex(S_vuon), latex(S_dat),
                      latex(chu_vi), latex(nua_chu_vi),
                      latex(nua_chu_vi), latex(S_dat),
                      latex(nua_chu_vi), latex(S_dat),
                      latex(nua_chu_vi), latex(S_dat), latex((d_dat - r_dat)**2), latex(d_dat - r_dat),
                      latex(d_dat), latex(r_dat),
                      latex(d_dat), latex(r_dat)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
