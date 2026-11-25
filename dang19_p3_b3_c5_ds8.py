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

def bt_dang19_p3_b3_c5_ds8(self):
    # Dạng 19: Tính tổng diện tích mặt nước nuôi trồng thủy sản qua biểu đồ cột kép
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ah20 = random.randint(1200, 1300)
        d_ah = random.randint(200, 280)
        ah25 = ah20 + d_ah
        
        bm20 = random.randint(1500, 1600)
        d_bm = random.randint(220, 320)
        bm25 = bm20 + d_bm
        
        tong20 = ah20 + bm20
        tong25 = ah25 + bm25
        tang = tong25 - tong20
        kq_str = str(tang)
        
        y_ah20 = round(ah20 / 500.0, 2)
        y_ah25 = round(ah25 / 500.0, 2)
        y_bm20 = round(bm20 / 500.0, 2)
        y_bm25 = round(bm25 / 500.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.4,0) node[below] {Huyện};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Diện tích ($\\text{ha}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.5,%s); \\node[above] at (1.15,%s) {$%s$};\n' % (y_ah20, y_ah20, ah20) +
            '\\draw[line width=1pt, fill=black!45] (1.5,0) rectangle (2.2,%s); \\node[above] at (1.85,%s) {$%s$};\n' % (y_ah25, y_ah25, ah25) +
            '\\node[below] at (1.5,0) {Huyện An Hải};\n' +
            '\\draw[line width=1pt, fill=black!15] (3.0,0) rectangle (3.7,%s); \\node[above] at (3.35,%s) {$%s$};\n' % (y_bm20, y_bm20, bm20) +
            '\\draw[line width=1pt, fill=black!45] (3.7,0) rectangle (4.4,%s); \\node[above] at (4.05,%s) {$%s$};\n' % (y_bm25, y_bm25, bm25) +
            '\\node[below] at (3.7,0) {Huyện Bình Minh};\n' +
            '\\draw[line width=1pt, fill=black!15] (5.5,3.2) rectangle (5.9,3.5) node[right, yshift=-4pt] {Năm $2020$};\n' +
            '\\draw[line width=1pt, fill=black!45] (5.5,2.4) rectangle (5.9,2.7) node[right, yshift=-4pt] {Năm $2025$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn diện tích nuôi trồng thủy sản (đơn vị: $\\text{ha}$) của hai huyện ven biển An Hải và Bình Minh trong năm $2020$ và năm $2025$:\n' +
                         tikz_code + '\n' +
                         'Hỏi tổng diện tích nuôi trồng thủy sản của cả hai huyện trong năm $2025$ tăng thêm bao nhiêu hecta ($\\text{ha}$) so với năm $2020$?')
        
        loigiai = ('- Tổng diện tích nuôi trồng thủy sản của cả hai huyện năm $2020$ là: $%s + %s = %s\\text{ (ha)}$.\\\\' +
                   '- Tổng diện tích nuôi trồng thủy sản của cả hai huyện năm $2025$ là: $%s + %s = %s\\text{ (ha)}$.\\\\' +
                   'Vậy tổng diện tích nuôi trồng thủy sản của cả hai huyện năm $2025$ tăng thêm so với năm $2020$ là:\\\\' +
                   '$$%s - %s = %s \\text{ (ha)}.$$'
                   ) % (ah20, bm20, tong20, ah25, bm25, tong25, tong25, tong20, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
