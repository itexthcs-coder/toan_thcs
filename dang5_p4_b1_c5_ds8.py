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


def bt_dang5_p4_b1_c5_ds8(self):
    # Dạng 5: Thiết kế phiếu khảo sát văn hóa đọc và không gian thư viện
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        bang_phieu = (
            "\\begin{center}\n"
            "\\begin{tabular}{|c|l|l|}\n"
            "\\hline\n"
            "\\textbf{STT} & \\textbf{Nội dung khảo sát} & \\textbf{Hình thức ghi nhận} \\\\\n"
            "\\hline\n"
            "$(1)$ & Mức độ hài lòng với ánh sáng và bàn ghế & Rất hài lòng / Hài lòng / Chưa hài lòng \\\\\n"
            "\\hline\n"
            "$(2)$ & Số lượt đến thư viện trong tháng vừa qua & Ghi số lượt cụ thể (ví dụ: $0; 3; 5; \\dots$) \\\\\n"
            "\\hline\n"
            "$(3)$ & Thời gian ngồi đọc trung bình mỗi lần (phút) & Ghi số phút (ví dụ: $25,5; 40; \\dots$) \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
        )

        noidungcauhoi = ('''Thư viện nhà trường dự định cải tạo không gian đọc sách và muốn lấy ý kiến học sinh theo mẫu phiếu khảo sát sau:
%s
a) Nên sử dụng phương pháp thu thập dữ liệu nào để đạt hiệu quả cao và đảm bảo tính đại diện cho toàn trường?\\\\
b) Xác định loại dữ liệu của từng nội dung $(1)$, $(2)$, $(3)$.''' % bang_phieu)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thư viện nên sử dụng \\textbf{phương pháp thu thập dữ liệu trực tiếp} bằng cách phát phiếu khảo sát (hoặc gửi biểu mẫu trực tuyến) cho một mẫu học sinh được chọn ngẫu nhiên ở tất cả các lớp thuộc cả $4$ khối $6, 7, 8, 9$ (bao gồm cả những bạn thường xuyên và ít khi đến thư viện) để đảm bảo tính đại diện.
\\item Phân loại dữ liệu của từng nội dung:\\\\
- Nội dung $(1)$ (Mức độ hài lòng): là \\textbf{dữ liệu không là số, có thể sắp thứ tự} (theo mức độ hài lòng giảm dần hoặc tăng dần).\\\\
- Nội dung $(2)$ (Số lượt đến thư viện): thu được từ phép đếm nên là \\textbf{số liệu rời rạc}.\\\\
- Nội dung $(3)$ (Thời gian ngồi đọc trung bình tính theo phút): thu được từ phép đo thời gian nên là \\textbf{số liệu liên tục}.
\\end{enumEX}''' % ())

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
