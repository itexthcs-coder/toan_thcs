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


def bt_dang2_p4_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        b1, b2 = random.choice([('Lan', 'Mai'), ('Vy', 'Chi'), ('Hà', 'Trang')])
        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Bóng $\\backslash$ Thẻ & $U$ & $E$ \\\\
\\hline
Đỏ ($Đ$) & $(Đ, U)$ & $(Đ, E)$ \\\\
\\hline
Xanh ($X$) & $(X, U)$ & $(X, E)$ \\\\
\\hline
Vàng ($V$) & $(V, U)$ & $(V, E)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Một túi đựng $3$ quả bóng cùng kích thước và khối lượng gồm một quả màu Đỏ ($Đ$), một quả màu Xanh ($X$) và một quả màu Vàng ($V$). Một hộp đựng $2$ tấm thẻ ghi chữ cái $U$ và $E$. Bạn %s lấy ngẫu nhiên $1$ quả bóng từ túi và bạn %s rút ngẫu nhiên $1$ tấm thẻ từ hộp. Tính xác suất của các biến cố:\\\\
a) $E$: ``Bạn %s lấy được quả bóng màu Đỏ'';\\\\
b) $F$: ``Bạn %s không lấy được quả bóng màu Vàng và bạn %s rút được tấm thẻ chữ $E$''.'''
                         % (b1, b2, b1, b1, b2))

        loigiai = ('''Ta lập bảng liệt kê không gian mẫu $\\Omega$ của phép thử:%s
Không gian mẫu $\\Omega$ gồm $6$ kết quả đồng khả năng nên $n(\\Omega) = 6$.
\\begin{enumEX}[a)]{1}
\\item Các kết quả thuận lợi cho biến cố $E$ là $(Đ, U)$ và $(Đ, E)$, suy ra $n(E) = 2$.\\\\
Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{n(E)}{n(\\Omega)} = \\dfrac{2}{6} = \\dfrac{1}{3}$.
\\item Các kết quả thuận lợi cho biến cố $F$ là $(Đ, E)$ và $(X, E)$, suy ra $n(F) = 2$.\\\\
Vậy xác suất của biến cố $F$ là $P(F) = \\dfrac{n(F)}{n(\\Omega)} = \\dfrac{2}{6} = \\dfrac{1}{3}$.
\\end{enumEX}''' % (bang_mau))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
