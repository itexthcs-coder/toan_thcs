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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D

def bt_dang20_p1_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tam = random.choice(['O', 'I'])
        diem = random.choice([('C', 'D'), ('A', 'B'), ('M', 'N')])
        d1, d2 = diem[0], diem[1]

        # Bộ ba Pythagore cơ bản
        bo_pytago = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
        kc, nua_day, R = bo_pytago[0], bo_pytago[1], bo_pytago[2]
        day = 2 * nua_day

        # Các đáp án trắc nghiệm
        du = ['$%s\\text{ cm}$' % (kc)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}$' % (nua_day),
            '$%s\\text{ cm}$' % (R + kc),
            '$%s\\text{ cm}$' % (abs(R - nua_day) + 1),
            '$\\sqrt{%s}\\text{ cm}$' % (R + nua_day)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(%s; %s\\text{ cm})$ và một dây cung $%s%s = %s\\text{ cm}$ (như hình vẽ). Khoảng cách từ tâm $%s$ đến dây $%s%s$ bằng bao nhiêu?
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (C) at (140:1.6);
        \\coordinate (D) at (40:1.6);
        \\coordinate (H) at (0,1.03);
        \\draw[line width=1pt] (O) circle (1.6);
        \\draw[line width=1pt] (C)--(D) (O)--(C) (O)--(D);
        \\draw[line width=1pt, dashed] (O)--(H);
        \\fill (O) circle (1pt) node[below] {$%s$};
        \\fill (C) circle (1pt) node[above left] {$%s$};
        \\fill (D) circle (1pt) node[above right] {$%s$};
        \\fill (H) circle (1pt) node[above] {$H$};
        \\end{tikzpicture}
        \\end{center}'''
                         % (tam, R, d1, d2, day, tam, d1, d2, tam, d1, d2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Kẻ $%sH \\perp %s%s$ tại $H$.\\\\
        Xét tam giác $%s%s%s$ có $%s%s = %s%s = %s\\text{ cm}$ nên tam giác $%s%s%s$ cân tại $%s$.\\\\
        Do đó đường cao $%sH$ đồng thời là đường trung tuyến, suy ra $H$ là trung điểm của $%s%s$, nên $%sH = \\dfrac{%s%s}{2} = \\dfrac{%s}{2} = %s\\text{ cm}$.\\\\
        Áp dụng định lí Pythagore trong tam giác $%sH%s$ vuông tại $H$, ta có:\\\\
        $%sH^2 + %sH^2 = %s%s^2 \\Rightarrow %sH^2 = %s%s^2 - %sH^2 = %s^2 - %s^2 = %s$.\\\\
        Suy ra $%sH = %s\\text{ cm}$. Vậy khoảng cách từ tâm $%s$ đến dây $%s%s$ bằng $%s\\text{ cm}$.'''
                   % (tam, d1, d2,
                      tam, d1, d2, tam, d1, tam, d2, R, tam, d1, d2, tam,
                      tam, d1, d2, d1, d1, d2, day, nua_day,
                      tam, d1,
                      tam, d1, tam, d1, tam, tam, d1, d1, R, nua_day, kc * kc,
                      tam, kc, tam, d1, d2, kc))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
