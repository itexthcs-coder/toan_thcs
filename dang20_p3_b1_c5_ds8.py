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


def bt_dang20_p3_b1_c5_ds8(self):
    # Dạng 20: Tổng hợp phân loại dữ liệu trong bảng điều tra dân số
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ds_so_lieu = [
            "Số nhân khẩu trong hộ",
            "Số người dưới $18$ tuổi",
            "Diện tích nhà ở ($\\text{m}^2$)",
            "Thu nhập bình quân mỗi tháng (triệu đồng)",
            "Lượng điện tiêu thụ tháng trước ($\\text{kWh}$)",
            "Số phòng ngủ của gia đình"
        ]
        ds_khong_so = [
            "Họ và tên chủ hộ",
            "Giới tính",
            "Dân tộc",
            "Trình độ học vấn",
            "Nghề nghiệp hiện tại",
            "Tình trạng hôn nhân"
        ]
        n_sl = random.choice([4, 5, 6])
        n_ks = 10 - n_sl
        chon_sl = random.sample(ds_so_lieu, n_sl)
        chon_ks = random.sample(ds_khong_so, n_ks)
        tat_ca = chon_sl + chon_ks
        random.shuffle(tat_ca)

        kq_str = str(n_sl)

        noidungcauhoi = ('''Trong một phiếu điều tra hộ gia đình tại địa phương gồm $12$ mục hỏi:\\\\
- \\textbf{Thu thập gián tiếp} từ căn cước công dân ($2$ mục): \\textit{Số định danh cá nhân, Ngày tháng năm sinh}.\\\\
- \\textbf{Thu thập trực tiếp} qua phỏng vấn ($10$ mục): \\textit{%s}.\\\\
Trong $10$ mục thu thập trực tiếp trên, có bao nhiêu mục cho kết quả là \\textbf{số liệu} (bao gồm cả số liệu rời rạc và số liệu liên tục)?'''
                         % ", ".join(tat_ca))

        loigiai = ('''Trong $10$ mục hỏi được thu thập trực tiếp qua phỏng vấn:\\\\
- Các mục cho kết quả là con số (số liệu) gồm $%s$ mục là: \\textit{%s}.\\\\
- Các mục còn lại (%s) đều cho kết quả là chữ hoặc tên gọi nên thuộc nhóm dữ liệu không là số.\\\\
Vậy có tất cả $%s$ mục thu thập trực tiếp cho kết quả là số liệu.'''
                   % (kq_str, ", ".join(chon_sl), ", ".join(chon_ks), kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
