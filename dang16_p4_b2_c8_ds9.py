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


def bt_dang16_p4_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Chục $\\backslash$ Đơn vị & $0$ & $1$ & $3$ & $5$ & $6$ \\\\
\\hline
$1$ & $10$ & $11$ & $13$ & $15$ & $16$ \\\\
\\hline
$3$ & $30$ & $31$ & $33$ & $35$ & $36$ \\\\
\\hline
$5$ & $50$ & $51$ & $53$ & $55$ & $56$ \\\\
\\hline
$6$ & $60$ & $61$ & $63$ & $65$ & $66$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Từ các chữ số $0; 1; 3; 5; 6$, lập ngẫu nhiên một số tự nhiên có hai chữ số (hai chữ số có thể giống nhau). Tính xác suất của các biến cố:\\\\
a) $A$: ``Số lập được chia hết cho $5$'';\\\\
b) $B$: ``Số lập được có chữ số hàng chục nhỏ hơn chữ số hàng đơn vị''.''')

        loigiai = ('''Chữ số hàng chục có $4$ cách chọn ($\\in \\{1; 3; 5; 6\\}$), chữ số hàng đơn vị có $5$ cách chọn ($\\in \\{0; 1; 3; 5; 6\\}$). Ta lập bảng liệt kê không gian mẫu $\\Omega$:%s
Không gian mẫu $\\Omega$ gồm $4 \\cdot 5 = 20$ số tự nhiên có hai chữ số đồng khả năng nên $n(\\Omega) = 20$.
\\begin{enumEX}[a)]{1}
\\item Số chia hết cho $5$ có tận cùng là $0$ hoặc $5$, gồm $8$ số là $10; 15; 30; 35; 50; 55; 60; 65$, suy ra $n(A) = 8$.\\\\
Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{8}{20} = \\dfrac{2}{5}$.
\\item Các số có chữ số hàng chục nhỏ hơn chữ số hàng đơn vị gồm:\\\\
- Hàng chục là $1$: $13; 15; 16$ ($3$ số).\\\\
- Hàng chục là $3$: $35; 36$ ($2$ số).\\\\
- Hàng chục là $5$: $56$ ($1$ số).\\\\
Suy ra $n(B) = 6$. Vậy xác suất của biến cố $B$ là $P(B) = \\dfrac{6}{20} = \\dfrac{3}{10}$.
\\end{enumEX}''' % (bang_mau))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
