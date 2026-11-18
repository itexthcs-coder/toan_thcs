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


def bt_dang16_p3_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        triples = [(4, 3, 5), (12, 5, 13), (8, 6, 10), (15, 8, 17), (16, 12, 20), (24, 7, 25)]
        base_a, base_b, base_c = random.choice(triples)
        k = randint(2, 6)
        dai = base_a * k
        rong = base_b * k
        cheo = base_c * k
        chu_vi = 2 * (dai + rong)
        nua_cv = dai + rong
        dien_tich = dai * rong
        kq_str = str(dai)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (4,2.5);
\\coordinate (D) at (0,2.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(C);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\node[above, sloped] at (2,1.25) {$%s\\text{ inch}$};
\\end{tikzpicture}
\\end{center}''' %(str(cheo)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một màn hình tivi dạng hình chữ nhật $ABCD$ có đường chéo dài $%s\\text{ inch}$ và chu vi bằng $%s\\text{ inch}$. Tính chiều dài của màn hình tivi đó (đơn vị: $\\text{inch}$). %s'''
                         %(str(cheo), str(chu_vi), hinhve))

        # Nội dung lời giải
        loigiai = ('''Gọi chiều dài và chiều rộng của màn hình tivi lần lượt là $x_1$, $x_2$ ($x_1 > x_2 > 0$, đơn vị: $\\text{inch}$). \\\\
                   Vì chu vi bằng $%s\\text{ inch}$ nên nửa chu vi là $x_1 + x_2 = %s$. \\\\
                   Áp dụng định lí Pythagore cho tam giác vuông $ABC$, ta có $x_1^2 + x_2^2 = %s^2 = %s$. \\\\
                   Ta có $(x_1 + x_2)^2 - 2x_1 x_2 = %s \\Leftrightarrow %s^2 - 2x_1 x_2 = %s \\Leftrightarrow 2x_1 x_2 = %s \\Leftrightarrow x_1 x_2 = %s$. \\\\
                   Khi đó $x_1$, $x_2$ là hai nghiệm của phương trình $x^2 - %sx + %s = 0$. \\\\
                   Giải phương trình trên, ta được $x_1 = %s$ và $x_2 = %s$ (thỏa mãn $x_1 > x_2 > 0$). \\\\
                   Vậy chiều dài của màn hình tivi là $%s\\text{ inch}$.'''
                   %(str(chu_vi), str(nua_cv),
                     str(cheo), str(cheo**2),
                     str(cheo**2), str(nua_cv), str(cheo**2), str(nua_cv**2 - cheo**2), str(dien_tich),
                     str(nua_cv), str(dien_tich),
                     str(dai), str(rong),
                     str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
