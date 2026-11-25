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


def bt_dang17_p4_b2_c6_ds8(self):
    # Dạng 17: Môi trường & Kinh tế - Bài toán phân tích hàm chi phí xử lý chất thải công nghiệp
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        k_str = '2,5'
        pct = '\\%'
        c50 = '2,5'
        c80 = '10'
        c90 = '22,5'
        c95 = '47,5'

        noidungcauhoi = ('Để loại bỏ $x%s$ chất gây ô nhiễm không khí từ khí thải của một nhà máy luyện kim, người ta ước tính chi phí cần thiết là $C(x) = \\dfrac{%sx}{100 - x}$ (tỉ đồng).\\\n'
                         'a) Viết điều kiện xác định của phân thức $C(x)$ và giải thích ý nghĩa thực tiễn của điều kiện này đối với việc xử lý ô nhiễm của nhà máy.\\\n'
                         'b) Tính chi phí cần thiết khi nhà máy muốn loại bỏ lần lượt $50%s$, $80%s$, $90%s$ và $95%s$ chất gây ô nhiễm. Nhận xét về tốc độ tăng chi phí khi tỉ lệ loại bỏ tiến gần tới $100%s$.\\\n'
                         'c) Với ngân sách tối đa là $%s$ tỉ đồng, nhà máy có thể loại bỏ được nhiều nhất bao nhiêu phần trăm chất gây ô nhiễm?'
                         % (pct, k_str, pct, pct, pct, pct, pct, c90))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Điều kiện xác định của phân thức $C(x)$ là $100 - x \\neq 0$, hay $x \\neq 100$.\\\n'
                   'Ý nghĩa thực tiễn: Tại $x = 100$ thì phân thức chi phí không xác định, điều này có nghĩa là về mặt kĩ thuật và chi phí, nhà máy không thể loại bỏ hoàn toàn $100%s$ chất gây ô nhiễm khỏi khí thải.\n'
                   '\\item Thay lần lượt các giá trị của $x$ vào phân thức $C(x) = \\dfrac{%sx}{100 - x}$:\\\n'
                   '- Với $x = 50$: $C(50) = \\dfrac{%s \\cdot 50}{100 - 50} = %s$ (tỉ đồng).\\\n'
                   '- Với $x = 80$: $C(80) = \\dfrac{%s \\cdot 80}{100 - 80} = %s$ (tỉ đồng).\\\n'
                   '- Với $x = 90$: $C(90) = \\dfrac{%s \\cdot 90}{100 - 90} = %s$ (tỉ đồng).\\\n'
                   '- Với $x = 95$: $C(95) = \\dfrac{%s \\cdot 95}{100 - 95} = %s$ (tỉ đồng).\\\n'
                   'Nhận xét: Khi tỉ lệ loại bỏ $x$ càng tiến gần tới $100%s$ thì chi phí xử lý tăng lên rất nhanh.\n'
                   '\\item Với ngân sách $%s$ tỉ đồng, ta có $\\dfrac{%sx}{100 - x} = %s \\Leftrightarrow %sx = %s(100 - x) \\Leftrightarrow %sx = 2250 - %sx \\Leftrightarrow 25x = 2250 \\Leftrightarrow x = 90$.\\\n'
                   'Vậy với ngân sách tối đa $%s$ tỉ đồng, nhà máy có thể loại bỏ được nhiều nhất $90%s$ chất gây ô nhiễm.\n'
                   '\\end{enumEX}'
                   % (pct, k_str, k_str, c50, k_str, c80, k_str, c90, k_str, c95, pct,
                      c90, k_str, c90, k_str, c90, k_str, c90, c90, pct))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
