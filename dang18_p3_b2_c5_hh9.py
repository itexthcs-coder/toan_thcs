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

def bt_dang18_p3_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pytago = random.choice([(12, 5, 13), (8, 6, 10), (15, 8, 17), (24, 7, 25), (12, 9, 15)])
        OH, AH, R = bo_pytago
        dk = 2 * R
        sau = R - OH
        AB = 2 * AH
        kq_str = str(AB)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một trục máy bằng thép có mặt cắt ngang là hình tròn tâm $O$, đường kính $%s\\text{ mm}$. Người thợ phay một rãnh phẳng $AB$ trên bề mặt trục sâu $%s\\text{ mm}$ tính từ mép ngoài vào tâm (như hình vẽ). Tính bề rộng của mặt phẳng rãnh cắt $AB$ đó (đơn vị: $\\text{mm}$).
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (O) at (0,0);
        \\coordinate (A) at (112:1.8);
        \\coordinate (B) at (68:1.8);
        \\coordinate (H) at (0,1.66);
        \\coordinate (M) at (0,1.8);
        \\draw[line width=1pt] (B) arc (68:-248:1.8);
        \\draw[line width=1pt] (A)--(B);
        \\draw[line width=1pt, dashed] (B) arc (68:112:1.8) (O)--(A) (O)--(M);
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (B) circle (1pt) node[above right] {$B$};
        \\fill (H) circle (1pt) node[below right] {$H$};
        \\end{tikzpicture}
        \\end{center}''' % (dk, sau))

        # Nội dung lời giải
        loigiai = ('''Bán kính mặt cắt ngang của trục máy là $R = \\dfrac{%s}{2} = %s\\text{ mm}$.\\\\
        Gọi $H$ là trung điểm của dây cung $AB$, ta có $OH \\perp AB$ và khoảng cách từ tâm $O$ đến mặt phẳng rãnh cắt là $OH = %s - %s = %s\\text{ mm}$.\\\\
        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
        $AH = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ mm}$.\\\\
        Vậy bề rộng của mặt phẳng rãnh cắt là $AB = 2AH = 2 \\cdot %s = %s\\text{ mm}$.'''
                   % (dk, R, R, sau, OH, R, OH, AH, AH, AB))

        #Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
