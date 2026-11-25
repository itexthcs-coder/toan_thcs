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


def bt_dang1_p4_b2_c5_ds8(self):
    # Dạng 1 (Tự luận - Vận dụng): Lựa chọn biểu đồ tối ưu cho bảng số liệu nguyên lớn và dựng biểu đồ cột
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([12500, 13400, 14200])
        b = random.choice([18000, 19500, 20000])
        c = random.choice([15400, 16200, 17800])
        d = random.choice([21200, 22400, 23600])
        
        sa = f"{a:,}".replace(",", "\\,")
        sb = f"{b:,}".replace(",", "\\,")
        sc = f"{c:,}".replace(",", "\\,")
        sd = f"{d:,}".replace(",", "\\,")
        
        ya, yb, yc, yd = a / 10000.0, b / 10000.0, c / 10000.0, d / 10000.0
        
        tikz_ans = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {Số cây};
        \\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[right] {Huyện};
        \\draw[line width=1pt, fill=black!25] (0.6,0) rectangle (1.3,%.2f);
        \\node[above] at (0.95,%.2f) {$%s$};
        \\node[below] at (0.95,0) {Huyện $A$};
        \\draw[line width=1pt, fill=black!25] (1.9,0) rectangle (2.6,%.2f);
        \\node[above] at (2.25,%.2f) {$%s$};
        \\node[below] at (2.25,0) {Huyện $B$};
        \\draw[line width=1pt, fill=black!25] (3.2,0) rectangle (3.9,%.2f);
        \\node[above] at (3.55,%.2f) {$%s$};
        \\node[below] at (3.55,0) {Huyện $C$};
        \\draw[line width=1pt, fill=black!25] (4.5,0) rectangle (5.2,%.2f);
        \\node[above] at (4.85,%.2f) {$%s$};
        \\node[below] at (4.85,0) {Huyện $D$};
        \\end{tikzpicture}
        \\end{center}""" % (ya, ya, sa, yb, yb, sb, yc, yc, sc, yd, yd, sd))
        
        noidungcauhoi = ("""Bảng thống kê dưới đây cho biết số lượng cây xanh được trồng mới tại bốn huyện vùng cao của một tỉnh trong năm $2025$:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Huyện} & Huyện $A$ & Huyện $B$ & Huyện $C$ & Huyện $D$ \\\\
        \\hline
        \\textbf{Số lượng (cây)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        a) Nên chọn biểu đồ tranh hay biểu đồ cột để biểu diễn bảng số liệu trên? Giải thích vì sao.\\\\
        b) Vẽ biểu đồ đã chọn ở câu a) để biểu diễn bảng số liệu trên.""" % (sa, sb, sc, sd))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Nên chọn \textbf{biểu đồ cột} để biểu diễn bảng số liệu trên. Vì các số liệu đều khá lớn và có phần lẻ hàng trăm ($%s$; $%s$; $%s$; $%s$); nếu dùng biểu đồ tranh với quy ước $1$ biểu tượng ứng với $100$ cây thì phải vẽ tới hàng trăm biểu tượng, còn nếu quy ước $1$ biểu tượng ứng với $1\\,000$ cây thì phải chia lẻ biểu tượng khó chính xác.
        \\item Biểu đồ cột biểu diễn số lượng cây xanh trồng mới tại bốn huyện:%s
        \\end{enumEX}""" % (sa, sb, sc, sd, tikz_ans))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
