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


def bt_dang18_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (6, 8, 10, 4, 6),
            (6, 8, 10, 2, 24),
            (9, 12, 15, 6, 9),
            (8, 15, 17, 4, 20)
        ]
        r_non, h_non, l_non, r_tru, h_tru = random.choice(cau_hinh)
        d_non = 2 * r_non
        v_pi = ((r_non ** 2) * h_non) // 3
        kq_str = str(h_tru)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một phễu lọc hóa chất bằng thủy tinh có phần chứa dạng hình nón với đường kính miệng phễu là $%s\\text{ cm}$ và độ dài đường sinh là $%s\\text{ cm}$ (như hình vẽ). Người ta đổ đầy chất lỏng vào phễu rồi rót toàn bộ lượng chất lỏng đó vào một bình đong dạng hình trụ có bán kính đáy bằng $%s\\text{ cm}$. Hỏi mực chất lỏng trong bình đong hình trụ cao bao nhiêu centimet (coi độ dày thủy tinh không đáng kể)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.4 and 0.32);
\\draw[line width=1pt] (-1.4,2.4)--(0,0.4)--(1.4,2.4);
\\draw[line width=1pt] (0,0.4)--(0,0);
\\draw[->, line width=1pt] (1.9,1.2)--(3.1,1.2);
\\draw[line width=1pt] (4.8,2.4) ellipse (0.9 and 0.25);
\\draw[line width=1pt] (3.9,0) arc (180:360:0.9 and 0.25);
\\draw[line width=1pt, dashed] (5.7,0) arc (0:180:0.9 and 0.25);
\\draw[line width=1pt] (3.9,0)--(3.9,2.4) (5.7,0)--(5.7,2.4);
\\draw[line width=1pt, dashed] (4.8,1.3) ellipse (0.9 and 0.25);
\\end{tikzpicture}
\\end{center}'''
                         % (d_non, l_non, r_tru))

        # Nội dung lời giải
        loigiai = ('''Bán kính miệng phễu hình nón là: $r = \\frac{%s}{2} = %s\\text{ (cm)}$. \\\\
Chiều cao của phần chứa dạng hình nón là:
$$h_{\\text{nón}} = \\sqrt{l^2 - r^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Thể tích chất lỏng có trong phễu là:
$$V = \\frac{1}{3}\\pi r^2 h_{\\text{nón}} = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Khi rót toàn bộ lượng chất lỏng này vào bình đong hình trụ có bán kính đáy $R = %s\\text{ cm}$, chiều cao mực chất lỏng trong bình đong là:
$$h_{\\text{trụ}} = \\frac{V}{\\pi R^2} = \\frac{%s\\pi}{\\pi \\cdot %s^2} = %s\\text{ (cm)}.$$'''
                   % (d_non, r_non, l_non, r_non, h_non, r_non, h_non, v_pi, r_tru, v_pi, r_tru, h_tru))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
