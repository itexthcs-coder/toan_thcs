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


def bt_dang10_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nA = 40
        nB = 40
        hs_A = (nA * 60) // 100
        hs_B = (nB * 45) // 100

        noidungcauhoi = ('''Cho hai bảng tần số tương đối ghép nhóm về điểm thi môn Lịch sử (thang điểm $10$) của hai lớp $9\\text{A}$ và $9\\text{B}$ (mỗi lớp đều có $40$ học sinh):
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Điểm thi & $[4; 5,5)$ & $[5,5; 7)$ & $[7; 8,5)$ & $[8,5; 10]$ \\\\
\\hline
Lớp $9\\text{A}$ & $10\\%%$ & $30\\%%$ & $40\\%%$ & $20\\%%$ \\\\
\\hline
Lớp $9\\text{B}$ & $20\\%%$ & $35\\%%$ & $30\\%%$ & $15\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
a) Tính số học sinh đạt điểm từ $7$ trở lên ở mỗi lớp.\\
b) Nhận xét và so sánh kết quả thi môn Lịch sử của hai lớp dựa trên bảng tần số tương đối trên.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Ở lớp $9\\text{A}$, tỉ lệ học sinh đạt điểm từ $7$ trở lên là $40\\%% + 20\\%% = 60\\%%$, tương ứng $40 \\cdot 60\\%% = %s$ (học sinh).\\
Ở lớp $9\\text{B}$, tỉ lệ học sinh đạt điểm từ $7$ trở lên là $30\\%% + 15\\%% = 45\\%%$, tương ứng $40 \\cdot 45\\%% = %s$ (học sinh).
\\item Nhận xét và so sánh:
\\begin{itemize}
\\item Tỉ lệ học sinh đạt điểm khá, giỏi (từ $7$ trở lên) của lớp $9\\text{A}$ ($60\\%%$) cao hơn lớp $9\\text{B}$ ($45\\%%$).
\\item Tỉ lệ học sinh có điểm dưới trung bình hoặc trung bình thấp ($[4; 5,5)$) của lớp $9\\text{A}$ ($10\\%%$) thấp hơn một nửa so với lớp $9\\text{B}$ ($20\\%%$).
\\item Nhìn chung, kết quả thi môn Lịch sử của lớp $9\\text{A}$ tốt và đồng đều ở mức cao hơn lớp $9\\text{B}$.
\\end{itemize}
\\end{enumEX}''' % (hs_A, hs_B))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
