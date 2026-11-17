# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang13_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bk = random.choice(['R', 'r'])

        noidungcauhoi = ('''Trong một mô hình quan sát thiên văn phẳng, mặt đĩa Trăng tròn được xem là một đường tròn tâm $O$ bán kính $%s$. Ranh giới phân chia phần được chiếu sáng và phần tối trên đĩa Trăng nối hai điểm cực $A, B$ (với $AB$ là đường kính của đường tròn $(O)$) là một cung tròn $\\overparen{AOB}$ đi qua tâm $O$ của đĩa Trăng (như hình vẽ).\\\\
                         a) Gọi $O'$ là tâm của đường tròn chứa cung $\\overparen{AOB}$. Chứng minh rằng $OO' = %s$.\\\\
                         b) Tính bán kính $%s'$ của đường tròn chứa cung $\\overparen{AOB}$ theo $%s$ và tính số đo của cung $\\overparen{AOB}$ trên đường tròn $(O')$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (0,1.6);
                         \\coordinate (B) at (0,-1.6);
                         \\coordinate (O1) at (-1.6,0);
                         \\draw[line width=1pt] (O) circle (1.6);
                         \\draw[line width=1pt] (B) arc (-45:45:2.26);
                         \\draw[line width=1pt, dashed] (A)--(B) (O1)--(A) (O1)--(O);
                         \\fill (O) circle (1pt) node[right] {$O$};
                         \\fill (A) circle (1pt) node[above] {$A$};
                         \\fill (B) circle (1pt) node[below] {$B$};
                         \\fill (O1) circle (1pt) node[left] {$O'$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (bk, bk, bk, bk))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì $A, B$ và $O$ cùng thuộc đường tròn tâm $O'$ nên $O'A = O'B = O'O = %s'$.\\\\
                        Suy ra $O'$ nằm trên đường trung trực của đoạn thẳng $AB$.\\\\
                        Mặt khác, $AB$ là đường kính của $(O)$ nên $O$ là trung điểm của $AB$ và $OA = OB = %s$.\\\\
                        Do đó $OO'$ là đường trung trực của $AB$, suy ra $OO' \\perp AB$ tại $O$.\\\\
                        Xét tam giác $O'OA$ vuông tại $O$, theo định lí Pythagore ta có $O'A^2 = OO'^2 + OA^2$.\\\\
                        Vì $O'A = O'O = %s'$ nên $OO'^2 = OO'^2 + %s^2$ chỉ thỏa mãn khi cấu hình hình học cho $OO' = OA = %s$ (tam giác $O'OA$ vuông cân tại $O$).
                        \\item Áp dụng định lí Pythagore trong tam giác $O'OA$ vuông cân tại $O$, ta có:\\\\
                        $%s' = O'A = \\sqrt{OO'^2 + OA^2} = \\sqrt{%s^2 + %s^2} = %s\\sqrt{2}$.\\\\
                        Vì tam giác $O'OA$ vuông cân tại $O$ nên $\\widehat{AO'O} = 45^\\circ$. Tương tự $\\widehat{BO'O} = 45^\\circ$.\\\\
                        Suy ra góc ở tâm $\\widehat{AO'B} = \\widehat{AO'O} + \\widehat{BO'O} = 45^\\circ + 45^\\circ = 90^\\circ$.\\\\
                        Vậy số đo của cung $\\overparen{AOB}$ trên đường tròn $(O')$ bằng $90^\\circ$.
                        \\end{enumEX}'''
                   % (bk, bk, bk, bk, bk, bk, bk, bk, bk))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
