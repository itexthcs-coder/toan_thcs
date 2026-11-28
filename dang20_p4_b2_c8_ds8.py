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


def bt_dang20_p4_b2_c8_ds8(self):
    # Dạng 20: Xác suất trong tình huống sắp xếp vị trí ngẫu nhiên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_sach = random.choice([
            ('Toán', 'Văn', 'Anh', 'Khoa học'),
            ('Toán', 'Lí', 'Hóa', 'Sinh'),
            ('Sử', 'Địa', 'Tin', 'Công nghệ')
        ])
        s1, s2, s3, s4 = bo_sach
        sub = random.choice(['canh_nhau', 'khong_canh_nhau'])
        if sub == 'canh_nhau':
            dk_text = 'quyển sách %s và quyển sách %s luôn được xếp đứng cạnh nhau' % (s1, s2)
            so_tl = 12
            xs_str = '\\frac{1}{2}'
            giai_thich = (
                'Các cách xếp thỏa mãn quyển sách %s và quyển sách %s đứng cạnh nhau là:\\\\\n'
                '- Cặp (%s, %s) đứng ở vị trí $1$ và $2$: có $2 \\cdot 2 = 4$ cách xếp.\\\\\n'
                '- Cặp (%s, %s) đứng ở vị trí $2$ và $3$: có $2 \\cdot 2 = 4$ cách xếp.\\\\\n'
                '- Cặp (%s, %s) đứng ở vị trí $3$ và $4$: có $2 \\cdot 2 = 4$ cách xếp.\\\\\n'
                'Tổng cộng có $4 + 4 + 4 = 12$ kết quả thuận lợi.'
            ) % (s1, s2, s1, s2, s1, s2, s1, s2)
        else:
            dk_text = 'quyển sách %s và quyển sách %s không đứng cạnh nhau' % (s1, s2)
            so_tl = 12
            xs_str = '\\frac{1}{2}'
            giai_thich = (
                'Các cách xếp quyển sách %s và quyển sách %s đứng cạnh nhau gồm $3$ cặp vị trí $(1;2), (2;3), (3;4)$, mỗi cặp vị trí có $2 \\cdot 2 = 4$ cách xếp nên có $3 \\cdot 4 = 12$ cách.\\\\\n'
                'Do đó, số cách xếp để quyển sách %s và quyển sách %s không đứng cạnh nhau là $24 - 12 = 12$ kết quả thuận lợi.'
            ) % (s1, s2, s1, s2)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) -- (6.4,0);\n'
            '\\foreach \\i/\\name in {0.4/%s, 1.9/%s, 3.4/%s, 4.9/%s}{\n'
            '  \\draw[line width=1pt] (\\i,0) rectangle (\\i+1.1,1.6);\n'
            '  \\node at (\\i+0.55,0.8) {\\name};\n'
            '}\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (s1, s2, s3, s4)

        noidungcauhoi = (
            'Có $4$ quyển sách khác nhau gồm: %s, %s, %s, %s được xếp ngẫu nhiên thành một hàng ngang trên giá sách. '
            'Tính xác suất để %s.%s'
        ) % (s1, s2, s3, s4, dk_text, tikz_img)

        loigiai = (
            'Xếp $4$ quyển sách khác nhau thành một hàng ngang trên giá sách:\\\\\n'
            '- Vị trí thứ nhất có $4$ cách chọn sách.\\\\\n'
            '- Vị trí thứ hai có $3$ cách chọn sách.\\\\\n'
            '- Vị trí thứ ba có $2$ cách chọn sách.\\\\\n'
            '- Vị trí thứ tư có $1$ cách chọn sách.\\\\\n'
            'Tổng số cách xếp $4$ quyển sách là $4 \\cdot 3 \\cdot 2 \\cdot 1 = 24$ cách. '
            'Vì xếp ngẫu nhiên nên $24$ kết quả có thể này là đồng khả năng.\\\\\n'
            '%s\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{24} = %s$.'
        ) % (giai_thich, so_tl, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
