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



def bt_dang3_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pytago = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
        R, r, d = random.choice(bo_pytago)
        
        alpha = math.acos(R / d)
        beta = math.acos(r / d)
        S_quat1 = (R**2) * alpha
        S_quat2 = (r**2) * beta
        S_tugiac = R * r
        S_chung_val = S_quat1 + S_quat2 - S_tugiac
        S_chung_tron = str(Decimal(str(S_chung_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (4,0);
\\coordinate (A) at (1.44,1.92);
\\coordinate (B) at (1.44,-1.92);
\\draw[line width=1pt] (O) circle (2.4cm);
\\draw[line width=1pt] (O') circle (3.2cm);
\\draw[line width=1pt] (O)--(O') (O)--(A) (O')--(A) (O)--(B) (O')--(B);
\\draw[line width=1pt, dashed] (A)--(B);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O') circle (1pt) node[right] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ cắt nhau tại $A$ và $B$ sao cho tiếp tuyến của $(O)$ tại $A$ đi qua $O'$ và tiếp tuyến của $(O')$ tại $A$ đi qua $O$.\\\\
        a) Chứng minh tam giác $OAO'$ là tam giác vuông và tính khoảng cách hai tâm $OO'$.\\\\
        b) Tính diện tích phần chung của hai hình tròn (làm tròn kết quả đến hàng phần mười). %s'''
                         % (latex(R), latex(r), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì $O'A$ là tiếp tuyến của đường tròn $(O)$ tại tiếp điểm $A$ nên $OA \\perp O'A$, suy ra $\\widehat{OAO'} = 90^\\circ$.\\\\
        Vậy tam giác $OAO'$ vuông tại $A$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $OAO'$, ta có:\\\\
        $OO' = \\sqrt{OA^2 + O'A^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s\\text{ (cm)}$.
        \\item Do tính đối xứng qua đường nối tâm $OO'$, ta có $\\triangle OBO' = \\triangle OAO'$ (c.c.c), suy ra $\\widehat{AOB} = 2\\widehat{AOO'}$ và $\\widehat{AO'B} = 2\\widehat{AO'O}$.\\\\
        Trong tam giác vuông $OAO'$, ta có $\\cos \\widehat{AOO'} = \\frac{OA}{OO'} = \\frac{%s}{%s}$ và $\\cos \\widehat{AO'O} = \\frac{O'A}{OO'} = \\frac{%s}{%s}$.\\\\
        Diện tích tứ giác $OAO'B$ là: $S_{OAO'B} = 2 S_{\\triangle OAO'} = OA \\cdot O'A = %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.\\\\
        Diện tích hình quạt tròn $OAB$ của $(O)$ là: $S_1 = \\frac{\\pi \\cdot %s^2 \\cdot \\widehat{AOB}}{360^\\circ}$.\\\\
        Diện tích hình quạt tròn $O'AB$ của $(O')$ là: $S_2 = \\frac{\\pi \\cdot %s^2 \\cdot \\widehat{AO'B}}{360^\\circ}$.\\\\
        Diện tích phần chung của hai hình tròn là:\\\\
        $S = S_1 + S_2 - S_{OAO'B} \\approx %s\\text{ (cm}^2\\text{)}$.
        \\end{enumEX}'''
                   % (latex(R), latex(r), latex(R**2 + r**2), latex(d),
                      latex(R), latex(d), latex(r), latex(d),
                      latex(R), latex(r), latex(R*r),
                      latex(R), latex(r), S_chung_tron))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
