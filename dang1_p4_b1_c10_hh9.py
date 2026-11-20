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


def bt_dang1_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ti_so = random.choice([2, 4, 6])
        k_val = ti_so // 2
        r_val = random.choice([2, 3, 4, 5])
        h_val = k_val * r_val
        tong_pi = (2 * k_val + 1) * (r_val ** 2)
        v_pi = (r_val ** 2) * h_val

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình trụ có tỉ số giữa diện tích xung quanh và diện tích một mặt đáy bằng $%s$, và tổng diện tích xung quanh với diện tích một mặt đáy bằng $%s\\pi\\text{ cm}^2$ (như hình vẽ). Tính bán kính đáy, chiều cao và thể tích của hình trụ đó.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (1.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0)--(-1.2,2.4) (1.2,0)--(1.2,2.4);
\\draw[line width=1pt, dashed] (0,2.4)--(0,0)--(1.2,0);
\\node[left] at (0,1.2) {$h$};
\\node[below] at (0.6,0) {$R$};
\\end{tikzpicture}
\\end{center}'''
                         % (ti_so, tong_pi))

        # Nội dung lời giải
        loigiai = ('''Gọi $R\\text{ (cm)}$ và $h\\text{ (cm)}$ lần lượt là bán kính đáy và chiều cao của hình trụ ($R > 0, h > 0$). \\\\
Theo đề bài, tỉ số giữa diện tích xung quanh và diện tích một mặt đáy bằng $%s$ nên:
$$\\frac{S_{xq}}{S_{\\text{đáy}}} = \\frac{2\\pi R h}{\\pi R^2} = \\frac{2h}{R} = %s \\Rightarrow h = %sR.$$
Mặt khác, tổng diện tích xung quanh và diện tích một mặt đáy bằng $%s\\pi\\text{ cm}^2$ nên:
$$2\\pi R h + \\pi R^2 = %s\\pi \\Rightarrow 2\\pi R \\cdot (%sR) + \\pi R^2 = %s\\pi \\Rightarrow %s\\pi R^2 = %s\\pi \\Rightarrow R^2 = %s \\Rightarrow R = %s\\text{ (cm)}.$$
Chiều cao của hình trụ là: $h = %s \\cdot %s = %s\\text{ (cm)}$. \\\\
Thể tích của hình trụ là:
$$V = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$'''
                   % (ti_so, ti_so, k_val, tong_pi, tong_pi, k_val, tong_pi, 2 * k_val + 1,
                      tong_pi, r_val ** 2, r_val, k_val, r_val, h_val, r_val, h_val, v_pi))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
