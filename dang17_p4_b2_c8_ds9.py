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


def bt_dang17_p4_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        b1, b2 = random.choice([('Nam', 'Việt'), ('Hùng', 'Dũng'), ('Long', 'Sơn')])
        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
%s $\\backslash$ %s & $1$ & $4$ & $5$ & $8$ & $9$ \\\\
\\hline
$2$ & $(2, 1)$ & $(2, 4)$ & $(2, 5)$ & $(2, 8)$ & $(2, 9)$ \\\\
\\hline
$4$ & $(4, 1)$ & $(4, 4)$ & $(4, 5)$ & $(4, 8)$ & $(4, 9)$ \\\\
\\hline
$6$ & $(6, 1)$ & $(6, 4)$ & $(6, 5)$ & $(6, 8)$ & $(6, 9)$ \\\\
\\hline
$8$ & $(8, 1)$ & $(8, 4)$ & $(8, 5)$ & $(8, 8)$ & $(8, 9)$ \\\\
\\hline
$10$ & $(10, 1)$ & $(10, 4)$ & $(10, 5)$ & $(10, 8)$ & $(10, 9)$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (b1, b2)

        noidungcauhoi = ('''Hai bạn %s và %s chơi một trò chơi: %s chọn ngẫu nhiên một số trong tập hợp $M = \\{2; 4; 6; 8; 10\\}$; %s chọn ngẫu nhiên một số trong tập hợp $N = \\{1; 4; 5; 8; 9\\}$. Người thắng cuộc là người chọn được số lớn hơn; nếu hai số bằng nhau thì hai bạn hòa nhau. Tính xác suất của các biến cố:\\\\
a) $A$: ``Hai bạn hòa nhau'';\\\\
b) $B$: ``Bạn %s thắng cuộc'';\\\\
c) $C$: ``Tổng hai số hai bạn chọn được là một số nguyên tố''.'''
                         % (b1, b2, b1, b2, b1))

        loigiai = ('''Ta lập bảng liệt kê không gian mẫu $\\Omega$ của phép thử:%s
Không gian mẫu $\\Omega$ gồm $5 \\cdot 5 = 25$ cặp số $(a, b)$ đồng khả năng nên $n(\\Omega) = 25$.
\\begin{enumEX}[a)]{1}
\\item Hai bạn hòa nhau khi $a = b$: có $2$ cặp là $(4, 4)$ và $(8, 8)$, suy ra $n(A) = 2$.\\\\
Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{2}{25}$.
\\item Các cặp $(a, b)$ để bạn %s thắng cuộc ($a > b$) gồm:\\\\
- Với $a = 2$: $(2, 1)$ ($1$ cặp).\\\\
- Với $a = 4$: $(4, 1)$ ($1$ cặp).\\\\
- Với $a = 6$: $(6, 1); (6, 4); (6, 5)$ ($3$ cặp).\\\\
- Với $a = 8$: $(8, 1); (8, 4); (8, 5)$ ($3$ cặp).\\\\
- Với $a = 10$: $(10, 1); (10, 4); (10, 5); (10, 8); (10, 9)$ ($5$ cặp).\\\\
Suy ra $n(B) = 13$. Vậy xác suất của biến cố $B$ là $P(B) = \\dfrac{13}{25}$.
\\item Các cặp có tổng $a + b$ là số nguyên tố ($3; 7; 11; 13; 17; 19$) gồm $10$ cặp: $(2, 1); (2, 5); (2, 9); (4, 9); (6, 1); (6, 5); (8, 5); (8, 9); (10, 1); (10, 9)$, suy ra $n(C) = 10$.\\\\
Vậy xác suất của biến cố $C$ là $P(C) = \\dfrac{10}{25} = \\dfrac{2}{5}$.
\\end{enumEX}''' % (bang_mau, b1))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
