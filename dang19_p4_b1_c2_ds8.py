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

def bt_dang19_p4_b1_c2_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a0 = randint(45, 75)
        b0 = randint(20, a0 - 10)
        while (a0 + b0) % 2 != 0:
            b0 = randint(20, a0 - 10)
        tong_cv = 4 * (a0 + b0)
        hieu_dt = a0**2 - b0**2
        tong_ab = a0 + b0
        hieu_ab = a0 - b0

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tại một khu đô thị mới, người ta quy hoạch hai quảng trường dạng hình vuông có tổng chu vi là $%s\\text{ m}$. Biết hiệu diện tích giữa quảng trường lớn và quảng trường nhỏ là $%s\\text{ m}^2$. Hãy tính độ dài cạnh của mỗi quảng trường.'''
                         % (latex(tong_cv), latex(hieu_dt)))

        # Nội dung lời giải
        loigiai = ('''Gọi độ dài cạnh của quảng trường lớn và quảng trường nhỏ lần lượt là $a$ và $b$ ($a > b > 0$, đơn vị: $\\text{m}$).\\\\
Vì tổng chu vi hai quảng trường là $%s\\text{ m}$ nên:
$$4a + 4b = %s \\Leftrightarrow a + b = %s.$$
Mặt khác, hiệu diện tích giữa hai quảng trường bằng $%s\\text{ m}^2$ nên:
$$a^2 - b^2 = %s \\Leftrightarrow (a - b)(a + b) = %s.$$
Thay $a + b = %s$ vào đẳng thức trên, ta được:
$$(a - b) \\cdot %s = %s \\Leftrightarrow a - b = %s.$$
Từ $a + b = %s$ và $a - b = %s$, suy ra:
$$a = \\frac{%s + %s}{2} = %s\\text{ (m)}, \\quad b = %s - %s = %s\\text{ (m)}.$$
Vậy độ dài cạnh của quảng trường lớn là $%s\\text{ m}$ và cạnh của quảng trường nhỏ là $%s\\text{ m}$.'''
                   % (latex(tong_cv), latex(tong_cv), latex(tong_ab),
                      latex(hieu_dt), latex(hieu_dt), latex(hieu_dt),
                      latex(tong_ab), latex(tong_ab), latex(hieu_dt), latex(hieu_ab),
                      latex(tong_ab), latex(hieu_ab),
                      latex(tong_ab), latex(hieu_ab), latex(a0),
                      latex(tong_ab), latex(a0), latex(b0),
                      latex(a0), latex(b0)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
