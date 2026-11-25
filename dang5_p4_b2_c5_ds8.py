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


def bt_dang5_p4_b2_c5_ds8(self):
    # Dạng 5 (Tự luận - Vận dụng): Thiết lập biểu đồ hình quạt tròn từ bảng tần số thô
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2, 3])
        n1, n2, n3, n4 = 70 * k, 40 * k, 60 * k, 30 * k
        tong = n1 + n2 + n3 + n4
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.6);
        \\draw[line width=1pt] (0,0) -- (0:1.6) (0,0) -- (126:1.6) (0,0) -- (198:1.6) (0,0) -- (306:1.6);
        \\node at (63:0.95) {$35\\%$};
        \\node at (162:0.95) {$20\\%$};
        \\node at (252:0.95) {$30\\%$};
        \\node at (333:1.0) {$15\\%$};
        \\node[right] at (2.0, 0.9) {Chơi thể thao: $35\\%$};
        \\node[right] at (2.0, 0.3) {Đọc sách: $20\\%$};
        \\node[right] at (2.0, -0.3) {Nghe nhạc/Xem phim: $30\\%$};
        \\node[right] at (2.0, -0.9) {Chơi trò chơi điện tử: $15\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Khảo sát phương thức giải trí yêu thích nhất sau giờ học của $%s$ học sinh một trường THCS thu được bảng thống kê:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Hoạt động} & Chơi thể thao & Đọc sách & Nghe nhạc/Xem phim & Trò chơi điện tử \\\\
        \\hline
        \\textbf{Số học sinh} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        a) Giải thích vì sao nên dùng biểu đồ hình quạt tròn để biểu diễn cơ cấu lựa chọn của $%s$ học sinh trên.\\\\
        b) Tính tỉ lệ phần trăm và số đo góc ở tâm tương ứng của từng hình quạt, sau đó vẽ hoàn thiện biểu đồ hình quạt tròn."""
                         % (tong, n1, n2, n3, n4, tong))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Nên dùng \\textbf{biểu đồ hình quạt tròn} vì mục đích là biểu diễn tỉ lệ phần trăm của từng nhóm hoạt động yêu thích trong tổng thể $%s$ học sinh ($100\\%%$).
        \\item Tổng số học sinh được khảo sát là: $%s + %s + %s + %s = %s$ (học sinh).\\\\
        - Chơi thể thao: $\\dfrac{%s}{%s} \\cdot 100\\%% = 35\\%%$, góc ở tâm bằng $360^\\circ \\cdot 35\\%% = 126^\\circ$.\\\\
        - Đọc sách: $\\dfrac{%s}{%s} \\cdot 100\\%% = 20\\%%$, góc ở tâm bằng $360^\\circ \\cdot 20\\%% = 72^\\circ$.\\\\
        - Nghe nhạc/Xem phim: $\\dfrac{%s}{%s} \\cdot 100\\%% = 30\\%%$, góc ở tâm bằng $360^\\circ \\cdot 30\\%% = 108^\\circ$.\\\\
        - Chơi trò chơi điện tử: $\\dfrac{%s}{%s} \\cdot 100\\%% = 15\\%%$, góc ở tâm bằng $360^\\circ \\cdot 15\\%% = 54^\\circ$.%s
        \\end{enumEX}""" % (tong, n1, n2, n3, n4, tong, n1, tong, n2, tong, n3, tong, n4, tong, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
