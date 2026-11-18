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


def bt_dang8_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (40, 5, 1, 2),
            (36, 4, 1, 3),
            (45, 5, 2, 6),
            (42, 7, 1, 1),
            (48, 6, 2, 4)
        ])
        tong_hs, to_dau, bot_to, them_hs = bo_so
        hs_dau = tong_hs // to_dau
        c_pt = (tong_hs * bot_to) // them_hs
        nghiem_am = -(to_dau - bot_to)
        delta = bot_to**2 + 4 * c_pt
        can_delta = int(math.isqrt(delta))

        noidungcauhoi = ('''Lớp $9$A có $%s$ học sinh được cô giáo chia đều thành các tổ để thảo luận nhóm. Nếu bớt đi $%s$ tổ thì số học sinh ở mỗi tổ còn lại sẽ tăng thêm $%s$ bạn so với dự định ban đầu. \\\\
a) Tính số tổ dự định chia ban đầu của lớp $9$A. \\\\
b) Tính số học sinh trong mỗi tổ theo dự định ban đầu.'''
                         %(latex(tong_hs), latex(bot_to), latex(them_hs)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x$ là số tổ dự định chia ban đầu. Điều kiện: $x \\in \\mathbb{N}^*$ và $x > %s$. \\\\
Số học sinh mỗi tổ theo dự định ban đầu là $\\frac{%s}{x}$ (học sinh). \\\\
Khi bớt đi $%s$ tổ, số tổ còn lại là $x - %s$ (tổ), khi đó số học sinh ở mỗi tổ là $\\frac{%s}{x - %s}$ (học sinh). \\\\
Vì số học sinh mỗi tổ tăng thêm $%s$ bạn nên ta có phương trình: \\\\
$\\frac{%s}{x - %s} - \\frac{%s}{x} = %s$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$x^2 - %sx - %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = \\frac{%s - %s}{2} = %s$ (loại); \\quad $x_2 = \\frac{%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy dự định ban đầu cô giáo chia lớp $9$A thành $%s$ tổ.
\\item Số học sinh trong mỗi tổ theo dự định ban đầu là: $\\frac{%s}{%s} = %s$ (học sinh).
\\end{enumEX}'''
                   %(latex(bot_to), latex(tong_hs), latex(bot_to), latex(bot_to), latex(tong_hs), latex(bot_to),
                     latex(them_hs), latex(tong_hs), latex(bot_to), latex(tong_hs), latex(them_hs),
                     latex(bot_to), latex(c_pt),
                     latex(bot_to), latex(c_pt), latex(delta), latex(can_delta),
                     latex(bot_to), latex(can_delta), latex(nghiem_am), latex(bot_to), latex(can_delta), latex(to_dau),
                     latex(to_dau),
                     latex(tong_hs), latex(to_dau), latex(hs_dau)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
