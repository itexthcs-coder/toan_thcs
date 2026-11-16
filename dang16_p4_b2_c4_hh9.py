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


def bt_dang16_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        thanh = 3
        thung = 4
        day = 5
        goc_do = int(Decimal(str(math.degrees(math.acos(4 / 5)))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        cao_chong = '2,4'
        cao_mep = '3,0'

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (C) at (4.0,0);
    \\coordinate (B) at (2.56,1.92);
    \\draw[line width=1pt] (A)--(C)--(B)--cycle;
    \\draw[line width=1pt] ($(B)!0.22cm!(A)$)--($(B)!0.22cm!(A)+(B)!0.22cm!(C)-(B)$)--($(B)!0.22cm!(C)$);
    \\draw[line width=1pt] (0.65,0) arc (0:36.87:0.65);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\node[above left] at (1.28,0.96) {$%s\\text{ m}$};
    \\node[above right] at (3.28,0.96) {$%s\\text{ m}$};
    \\node[below] at (2.0,0) {$%s\\text{ m}$};
    \\node at (0.95,0.24) {$\\alpha$};
    \\end{tikzpicture}
    \\end{center}''' % (thung, thanh, day))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một xe chở rác chuyên dụng có thùng xe dài $5\\text{ m}$. Khi vận hành cơ cấu nâng thùng xe để đổ rác, bản lề phía sau của thùng xe tại $A$ và điểm cố định của xi-lanh thủy lực trên khung gầm tại $C$ cách nhau $AC = %s\\text{ m}$; thanh đẩy thủy lực $BC$ vươn dài vuông góc với đáy thùng xe tại $B$ một đoạn $BC = %s\\text{ m}$, với $AB = %s\\text{ m}$ (như hình vẽ). \\\\
    a) Tính góc nghiêng $\\alpha$ của thùng xe so với phương ngang (làm tròn đến độ). \\\\
    b) Tính độ cao của điểm đầu thanh đẩy $B$ và độ cao của mép trên cùng thùng xe (cách $A$ một đoạn $5\\text{ m}$) so với mặt phẳng khung gầm $AC$.
    %s''' % (day, thanh, thung, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $ABC$ vuông tại $B$, theo định nghĩa tỉ số lượng giác góc nhọn ta có:\\\\
    $\\cos \\alpha = \\dfrac{AB}{AC} = \\dfrac{4}{5} = 0,8$.\\\\
    Sử dụng máy tính cầm tay, tìm được $\\alpha \\approx 36,87^\\circ \\approx %s^\\circ$.
    \\item Trong tam giác vuông $ABC$, ta có $\\sin \\alpha = \\dfrac{BC}{AC} = \\dfrac{3}{5} = 0,6$.\\\\
    Độ cao của điểm đầu thanh đẩy $B$ so với khung gầm $AC$ là $h_B = AB \\cdot \\sin \\alpha = 4 \\cdot 0,6 = %s\\text{ (m)}$.\\\\
    Độ cao của mép trên cùng thùng xe (cách $A$ một đoạn $5\\text{ m}$) so với khung gầm là $h = 5 \\cdot \\sin \\alpha = 5 \\cdot 0,6 = %s\\text{ (m)}$.
    \\end{enumEX}'''
                   % (goc_do, cao_chong, cao_mep))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
