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



def bt_dang15_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R_mt = Rational(randint(155, 165), 10)
        r_m = R_mt - Rational(randint(10, 18), 10)
        hieu = R_mt - r_m
        
        R_mt_str = str(float(R_mt)).replace('.', ',')
        r_m_str = str(float(r_m)).replace('.', ',')
        hieu_str = str(float(hieu)).replace('.', ',')

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (O) circle (2.2cm);
\\draw[line width=1pt] (O) circle (1.75cm);
\\draw[line width=1pt] (O)--(2.2,0);
\\fill (O) circle (1pt) node[left] {$O$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Nhật thực hình khuyên xảy ra khi Mặt Trăng đi qua giữa Trái Đất và Mặt Trời, nhưng do ở xa Trái Đất nên đĩa Mặt Trăng nhìn từ Trái Đất có bán kính biểu kiến nhỏ hơn đĩa Mặt Trời, để lại một vòng sáng rực rỡ bao quanh đĩa Mặt Trăng tối màu. Trên một ảnh chụp thiên văn, đĩa Mặt Trời có bán kính $R = %s\\text{ mm}$ và đĩa Mặt Trăng có bán kính $r = %s\\text{ mm}$.\\\\
        a) Ở giai đoạn cực đại của nhật thực hình khuyên (tâm của hai đĩa trùng nhau), hai đường tròn biểu diễn Mặt Trời và Mặt Trăng có vị trí tương đối như thế nào? Tính bề rộng của vòng sáng bao quanh.\\\\
        b) Khoảng cách $d$ giữa hai tâm của hai đĩa trên ảnh chụp phải thỏa mãn điều kiện nào để vẫn còn quan sát thấy hiện tượng nhật thực hình khuyên (toàn bộ đĩa Mặt Trăng nằm lọt bên trong đĩa Mặt Trời và không chạm viền ngoài)? %s'''
                         % (R_mt_str, r_m_str, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Ở giai đoạn cực đại, tâm của đĩa Mặt Trời và tâm của đĩa Mặt Trăng trùng nhau, đồng thời hai bán kính khác nhau ($R = %s\\text{ mm} > r = %s\\text{ mm}$) nên hai đường tròn biểu diễn Mặt Trời và Mặt Trăng là hai đường tròn đồng tâm (trường hợp đặc biệt của đường tròn lớn đựng đường tròn nhỏ).\\\\
        Bề rộng của vòng sáng bao quanh (hình vành khăn) là: $b = R - r = %s - %s = %s\\text{ (mm)}$.
        \\item Để toàn bộ đĩa Mặt Trăng nằm lọt hẳn bên trong đĩa Mặt Trời và không chạm viền ngoài thì đường tròn $(O; %s\\text{ mm})$ phải đựng đường tròn $(O'; %s\\text{ mm})$.\\\\
        Điều kiện để đường tròn lớn đựng đường tròn nhỏ là khoảng cách hai tâm thỏa mãn:\\\\
        $0 \\le d < R - r \\Leftrightarrow 0 \\le d < %s - %s \\Leftrightarrow 0 \\le d < %s\\text{ (mm)}$.\\\\
        Vậy khoảng cách giữa hai tâm phải nhỏ hơn $%s\\text{ mm}$.
        \\end{enumEX}'''
                   % (R_mt_str, r_m_str, R_mt_str, r_m_str, hieu_str,
                      R_mt_str, r_m_str, R_mt_str, r_m_str, hieu_str, hieu_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
