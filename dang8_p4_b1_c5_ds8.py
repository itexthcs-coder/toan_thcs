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


def bt_dang8_p4_b1_c5_ds8(self):
    # Dạng 8: Xử lí tình huống khảo sát thể lực vận động viên trẻ
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            t1 = random.randint(530, 565)
            t2 = random.randint(530, 565)
            t3 = random.randint(530, 565)
            t4 = random.randint(530, 565)
            if len({t1, t2, t3, t4}) == 4 and (t1 + t2 + t3 + t4) % 4 == 0:
                break
        t_am = -random.randint(521, 559)

        def fmt1(v):
            s = str(Decimal(v) / Decimal(10)).replace('.', ',')
            if s.endswith(',0'):
                return s[:-2]
            return s

        day = [fmt1(t1), fmt1(t2), fmt1(t_am), fmt1(t3), fmt1(t4)]
        random.shuffle(day)
        day_str = ";\\; ".join(day)

        tb_val = Decimal(t1 + t2 + t3 + t4) / Decimal(40)
        tb_str = str(tb_val).replace('.', ',')
        if tb_str.endswith(',0'):
            tb_str = tb_str[:-2]

        noidungcauhoi = ('''Huấn luyện viên đội tuyển điền kinh trẻ của tỉnh kiểm tra thể lực đầu vào của các vận động viên bằng cách đo \\textit{Nhịp tim khi nghỉ ngơi (nhịp/phút)}, đo \\textit{Thành tích chạy cự li $400\\,\\text{m}$ (giây)} và đếm \\textit{Số lần hít đất tối đa thực hiện được trong $1$ phút}.\\\\
a) Hãy phân loại dữ liệu của ba bài kiểm tra trên và giải thích rõ dựa trên tính chất phép đo và phép đếm.\\\\
b) Trong bảng ghi chép thành tích chạy $400\\,\\text{m}$ của $5$ vận động viên có kết quả: $%s$. Hãy phát hiện giá trị không hợp lí và tính thành tích trung bình của các vận động viên có số liệu hợp lí.''' % day_str)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Phân loại dữ liệu của ba bài kiểm tra:\\\\
- \\textit{Nhịp tim khi nghỉ ngơi (nhịp/phút)} và \\textit{Thành tích chạy cự li $400\\,\\text{m}$ (giây)} đều thu được từ các phép đo lường sinh học và thời gian, có thể nhận giá trị thực tùy ý trong một khoảng nên thuộc loại \\textbf{số liệu liên tục}.\\\\
- \\textit{Số lần hít đất tối đa trong $1$ phút} thu được từ phép đếm số động tác hoàn chỉnh nên chỉ nhận các giá trị nguyên không âm, thuộc loại \\textbf{số liệu rời rạc}.
\\item Trong dãy số liệu $%s$, giá trị $%s$ là không hợp lí vì thời gian chạy không thể là số âm.\\\\
Loại bỏ giá trị $%s$, thành tích trung bình của $4$ vận động viên còn lại là:
$$\\dfrac{%s + %s + %s + %s}{4} = %s\\text{ (giây)}.$$
\\end{enumEX}''' % (day_str, fmt1(t_am), fmt1(t_am),
                      fmt1(t1), fmt1(t2), fmt1(t3), fmt1(t4), tb_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
