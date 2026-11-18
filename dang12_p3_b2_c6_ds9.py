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

def bt_dang12_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ba = random.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15)])
        a_canh, b_canh, c_huyen = bo_ba
        hieu = b_canh - a_canh
        chu_vi = a_canh + b_canh + c_huyen
        kq_str = str(chu_vi)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có độ dài cạnh huyền $BC = %s\\text{ cm}$ và hai cạnh góc vuông hơn kém nhau $%s\\text{ cm}$ (như hình vẽ). Tính chu vi của tam giác vuông $ABC$ (đơn vị: $\\text{cm}$).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (B) at (0,2.5);
\\draw[line width=1pt] (A) -- (C) -- (B) -- cycle;
\\draw[line width=1pt] (0,0.35) -- (0.35,0.35) -- (0.35,0);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[above left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\node[left] at (0,1.25) {$x$};
\\node[below] at (2.25,0) {$x + %s$};
\\node[above right] at (2.25,1.25) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}'''
                         %(str(c_huyen), str(hieu), str(hieu), str(c_huyen)
                         ))

        # Nội dung lời giải
        loigiai = ('''Gọi độ dài cạnh góc vuông nhỏ hơn là $x$ ($\\text{cm}$, $x > 0$). \\\\
                   Khi đó độ dài cạnh góc vuông còn lại là $x + %s$ ($\\text{cm}$). \\\\
                   Áp dụng định lí Pythagore vào tam giác $ABC$ vuông tại $A$, ta có phương trình: \\\\
                   $x^2 + (x + %s)^2 = %s^2 \\Leftrightarrow 2x^2 + %sx + %s = %s \\Leftrightarrow x^2 + %sx - %s = 0$. \\\\
                   Tính biệt thức $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt $x_1 = %s$ (thỏa mãn điều kiện) và $x_2 = %s$ (loại). \\\\
                   Suy ra hai cạnh góc vuông có độ dài là $%s\\text{ cm}$ và $%s\\text{ cm}$. \\\\
                   Chu vi tam giác vuông $ABC$ là $%s + %s + %s = %s$ ($\\text{cm}$).'''
                   %(str(hieu),
                     str(hieu), str(c_huyen), str(2*hieu), str(hieu**2), str(c_huyen**2), str(hieu), str((c_huyen**2 - hieu**2)//2),
                     str(hieu), str((c_huyen**2 - hieu**2)//2), str(hieu**2 + 2*(c_huyen**2 - hieu**2)),
                     str(a_canh), str(-b_canh),
                     str(a_canh), str(b_canh),
                     str(a_canh), str(b_canh), str(c_huyen), kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
