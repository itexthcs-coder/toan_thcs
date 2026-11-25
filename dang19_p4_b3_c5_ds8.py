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

def bt_dang19_p4_b3_c5_ds8(self):
    # Dạng 19: Phân tích dữ liệu y tế - Chỉ số BMI của học sinh qua biểu đồ cột ghép (Liên môn Sinh học)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_nam, n_nu = 250, 250
        tc_nam, bt_nam, bp_nam = 20, 175, 55
        tc_nu, bt_nu, bp_nu = 30, 185, 35
        
        pct_bp_nam = int(bp_nam * 100 // n_nam) # 22%
        pct_bp_nu = int(bp_nu * 100 // n_nu)    # 14%
        
        tong_all = n_nam + n_nu # 500
        pct_tc_all = int((tc_nam + tc_nu) * 100 // tong_all) # 10%
        pct_bt_all = int((bt_nam + bt_nu) * 100 // tong_all) # 72%
        pct_bp_all = int((bp_nam + bp_nu) * 100 // tong_all) # 18%
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.8,0) node[below] {Tình trạng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số học sinh};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.6,0) rectangle (1.2,0.4); \\node[above] at (0.9,0.4) {$20$};\n' +
            '\\draw[line width=1pt, fill=black!45] (1.2,0) rectangle (1.8,0.6); \\node[above] at (1.5,0.6) {$30$};\n' +
            '\\node[below] at (1.2,0) {Thiếu cân};\n' +
            '\\draw[line width=1pt, fill=black!15] (2.6,0) rectangle (3.2,3.5); \\node[above] at (2.9,3.5) {$175$};\n' +
            '\\draw[line width=1pt, fill=black!45] (3.2,0) rectangle (3.8,3.7); \\node[above] at (3.5,3.7) {$185$};\n' +
            '\\node[below] at (3.2,0) {Bình thường};\n' +
            '\\draw[line width=1pt, fill=black!15] (4.6,0) rectangle (5.2,1.1); \\node[above] at (4.9,1.1) {$55$};\n' +
            '\\draw[line width=1pt, fill=black!45] (5.2,0) rectangle (5.8,0.7); \\node[above] at (5.5,0.7) {$35$};\n' +
            '\\node[below] at (5.2,0) {Thừa cân – Béo phì};\n' +
            '\\draw[line width=1pt, fill=black!15] (6.8,3.2) rectangle (7.2,3.5) node[right, yshift=-4pt] {Nam ($250$ em)};\n' +
            '\\draw[line width=1pt, fill=black!45] (6.8,2.4) rectangle (7.2,2.7) node[right, yshift=-4pt] {Nữ ($250$ em)};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây thống kê tình trạng dinh dưỡng (dựa trên chỉ số BMI) của $250$ học sinh nam và $250$ học sinh nữ khối $8$ tại một trường THCS:\n' +
                         tikz_code + '\n' +
                         'a) Tính tỉ lệ phần trăm học sinh bị Thừa cân – Béo phì ở nhóm học sinh nam và ở nhóm học sinh nữ. Nhóm nào có tỉ lệ thừa cân – béo phì cao hơn?\\\n' +
                         'b) Nếu gộp chung toàn bộ $500$ học sinh khối $8$ để vẽ một biểu đồ hình quạt tròn thể hiện cơ cấu tình trạng dinh dưỡng của cả khối, hãy tính tỉ lệ phần trăm của từng nhóm (Thiếu cân, Bình thường, Thừa cân – Béo phì).')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item - Tỉ lệ học sinh nam bị Thừa cân – Béo phì là: $\\dfrac{55}{250} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Tỉ lệ học sinh nữ bị Thừa cân – Béo phì là: $\\dfrac{35}{250} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   'Vậy nhóm học sinh nam có tỉ lệ thừa cân – béo phì cao hơn nhóm học sinh nữ ($%s\\%% > %s\\%%$).\n' +
                   '\\item Khi gộp chung toàn bộ $500$ học sinh khối $8$, số lượng và tỉ lệ phần trăm của từng nhóm là:\\\\' +
                   '- Nhóm Thiếu cân: $20 + 30 = 50$ (học sinh), chiếm $\\dfrac{50}{500} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Nhóm Bình thường: $175 + 185 = 360$ (học sinh), chiếm $\\dfrac{360}{500} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Nhóm Thừa cân – Béo phì: $55 + 35 = 90$ (học sinh), chiếm $\\dfrac{90}{500} \\cdot 100\\%% = %s\\%%$.\n' +
                   '\\end{enumEX}'
                   ) % (pct_bp_nam, pct_bp_nu, pct_bp_nam, pct_bp_nu, pct_tc_all, pct_bt_all, pct_bp_all)

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
