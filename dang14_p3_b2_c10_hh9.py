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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang14_p3_b2_c10_hh9(self):
    # Thiết diện qua trục là tam giác cân SAB ngoại tiếp đường tròn (O; R).
    # Chọn nửa góc ở đỉnh alpha sao cho sin(alpha) = 3/5, cos(alpha) = 4/5, tan(alpha) = 3/4.
    # Khi đó h_non = R + R / sin(alpha) = R + 5R/3 = 8R/3; r_day = h_non * tan(alpha) = (8R/3)*(3/4) = 2R.
    # Chọn R = 3k => h_non = 8k, r_day = 6k, l_non = 10k!
    k = random.choice([1, 2, 3])
    R = 3 * k
    h_non = 8 * k
    r_day = 6 * k
    l_non = 10 * k
    V_non_heso = (r_day**2 * h_non) // 3
    kq_str = str(V_non_heso)

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (H) at (0,0);
\\coordinate (S) at (0,2.4);
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (O) at (0,0.9);
\\draw[line width=1pt] (A) arc (180:360:1.8cm and 0.4cm);
\\draw[line width=1pt, dashed] (B) arc (0:180:1.8cm and 0.4cm);
\\draw[line width=1pt] (A)--(S)--(B);
\\draw[line width=1pt] (O) circle (0.9cm);
\\draw[line width=1pt, dashed] (S)--(H)--(B);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho một hình nón có bán kính đáy $r = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$. Đặt một hình cầu nằm bên trong hình nón sao cho hình cầu tiếp xúc với mặt đáy của hình nón và tiếp xúc với tất cả các đường sinh của hình nón. Tính bán kính $R$ của hình cầu đó (đơn vị: $\\text{cm}$).%s'''
                     % (r_day, h_non, hinh_ve))
    kq_str = str(R)

    loigiai = ('''Xét thiết diện qua trục của hình nón là tam giác cân $SAB$ có đáy $AB = 2r = %s\\text{ cm}$, đường cao $SH = h = %s\\text{ cm}$, nội tiếp đường tròn $(O; R)$ tiếp xúc với $AB$ tại $H$ và tiếp xúc với $SB$ tại $T$.\\\nĐộ dài đường sinh của hình nón là: $l = SB = \\sqrt{SH^2 + HB^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.\\\nTa có $BT = BH = %s\\text{ cm} \\Rightarrow ST = SB - BT = %s - %s = %s\\text{ (cm)}$.\\\nHai tam giác vuông $STO$ và $SHB$ đồng dạng (chung góc $S$), suy ra:
$$\\dfrac{OT}{HB} = \\dfrac{ST}{SH} \\Rightarrow \\dfrac{R}{%s} = \\dfrac{%s}{%s} \\Rightarrow R = %s\\text{ (cm)}.$$'''
               % (2 * r_day, h_non, h_non, r_day, l_non, r_day, l_non, r_day, l_non - r_day, r_day, l_non - r_day, h_non, R))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
