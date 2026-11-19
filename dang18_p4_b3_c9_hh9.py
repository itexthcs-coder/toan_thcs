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


def bt_dang18_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([10, 16, 20, 24, 30])
        nua_a = a // 2
        r_expr = nua_a * sqrt(2)
        d_expr = a * sqrt(2)
        s_vuong = a**2
        r_sq = 2 * (nua_a**2)
        s_tron = Decimal(str(3.14 * r_sq)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s_da = s_tron - Decimal(str(s_vuong))

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-1.1,1.1);
\\coordinate (B) at (-1.1,-1.1);
\\coordinate (C) at (1.1,-1.1);
\\coordinate (D) at (1.1,1.1);
\\coordinate (O) at (0,0);
\\draw[line width=1pt, dashed] (O) circle (1.5556);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (A)--(C) (B)--(D);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một quảng trường nhỏ có dạng hình vuông $ABCD$ cạnh $%s\\text{ m}$. Ban quản lý dự án muốn lắp đặt một cột đèn chiếu sáng tại tâm $O$ của quảng trường sao cho vùng sáng hình tròn của đèn vừa đủ bao phủ tới cả bốn góc của quảng trường. \\\\
a) Xác định vị trí điểm $O$ trên bản vẽ quảng trường và tính khoảng cách từ cột đèn đến mỗi góc quảng trường. \\\\
b) Để tăng tính thẩm mỹ, người ta lát đá hoa cương cho phần diện tích hình tròn ngoại tiếp quảng trường nằm bên ngoài hình vuông $ABCD$. Tính diện tích phần lát đá hoa cương đó (lấy $\\pi \\approx 3,14$, đơn vị: $\\text{m}^2$).%s''' % (a, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì vùng sáng hình tròn vừa đủ bao phủ tới cả bốn góc của hình vuông $ABCD$ nên đó chính là đường tròn ngoại tiếp hình vuông $ABCD$. Do đó, vị trí điểm $O$ là giao điểm của hai đường chéo $AC$ và $BD$.\\\\
Độ dài đường chéo của quảng trường hình vuông là $AC = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.\\\\
Khoảng cách từ cột đèn $O$ đến mỗi góc quảng trường bằng bán kính đường tròn ngoại tiếp: $R = \\dfrac{AC}{2} = %s\\text{ (m)}$.
\\item Diện tích của quảng trường hình vuông là $S_{ABCD} = %s^2 = %s\\text{ (m}^2)$.\\\\
Diện tích hình tròn ngoại tiếp quảng trường là $S_{\\text{tròn}} = \\pi R^2 \\approx 3,14 \\cdot (%s)^2 = %s\\text{ (m}^2)$.\\\\
Vậy diện tích phần lát đá hoa cương nằm bên ngoài hình vuông là $S_{\\text{đá}} = %s - %s = %s\\text{ (m}^2)$.
\\end{enumEX}''' % (a, a, latex(d_expr), latex(r_expr), a, s_vuong, latex(r_expr), str(s_tron).replace('.', ','), str(s_tron).replace('.', ','), s_vuong, str(s_da).replace('.', ',')))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
