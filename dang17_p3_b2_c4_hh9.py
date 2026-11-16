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


def bt_dang17_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        rong = 4.4
        cao = 1.8
        dai = random.choice([3.0, 3.5, 4.0])
        mai_val = math.sqrt(cao**2 + (rong / 2.0)**2)
        dt_val = 2 * mai_val * dai

        rong_str = str(rong).replace('.', ',')
        cao_str = str(cao).replace('.', ',')
        dai_str = str(dai).replace('.', ',')
        mai_str = str(Decimal(str(mai_val)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).replace('.', ',')
        number = Decimal(str(dt_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (H) at (1.5,0);
    \\coordinate (C) at (3.0,0);
    \\coordinate (A) at (1.5,1.25);
    \\coordinate (B1) at (1.8,0.8);
    \\coordinate (C1) at (4.8,0.8);
    \\coordinate (A1) at (3.3,2.05);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(A1)--(C1)--(C);
    \\draw[line width=1pt, dashed] (A)--(H) (B)--(B1)--(C1) (A1)--(B1);
    \\draw[line width=1pt] (1.5,0.2)--(1.7,0.2)--(1.7,0);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[right] at (1.5,0.62) {$%s\\text{ m}$};
    \\node[below] at (1.5,-0.25) {$%s\\text{ m}$};
    \\node[below right] at (3.9,0.4) {$%s\\text{ m}$};
    \\end{tikzpicture}
    \\end{center}''' % (cao_str, rong_str, dai_str))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc lều trại dạng lăng trụ đứng có đáy là tam giác cân $ABC$ với bề rộng đáy $BC = %s\\text{ m}$, chiều cao trụ giữa $AH = %s\\text{ m}$ và chiều dài dọc theo thân lều bằng $%s\\text{ m}$ (như hình vẽ). Tính tổng diện tích vải bạt dùng để phủ kín hai mái nghiêng của lều theo đơn vị $\\text{m}^2$ (làm tròn kết quả đến hàng phần mười).
    %s''' % (rong_str, cao_str, dai_str, hinhve))

        # Nội dung lời giải
        loigiai = ('''Vì tam giác $ABC$ cân tại $A$ nên đường cao $AH$ đồng thời là đường trung tuyến, suy ra $HC = \\dfrac{BC}{2} = \\dfrac{%s}{2} = 2,2\\text{ (m)}$.\\\\
    Áp dụng định lí Pythagore trong tam giác vuông $AHC$, chiều rộng một mái nghiêng là:\\\\
    $AC = \\sqrt{AH^2 + HC^2} = \\sqrt{%s^2 + 2,2^2} = \\sqrt{8,08} \\approx %s\\text{ (m)}$.\\\\
    Tổng diện tích vải bạt phủ kín hai mái nghiêng hình chữ nhật là:\\\\
    $S = 2 \\cdot AC \\cdot %s \\approx 2 \\cdot %s \\cdot %s \\approx %s\\text{ (m}^2\\text{)}$.'''
                   % (rong_str, cao_str, mai_str,
                      dai_str, mai_str, dai_str, str(kq_str)))

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
