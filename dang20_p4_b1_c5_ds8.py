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


def bt_dang20_p4_b1_c5_ds8(self):
    # Dạng 20: Bài toán tổng hợp thiết kế dự án thống kê liên môn
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        chu_de_list = [
            ("Tình hình tự học buổi tối ở nhà của học sinh khối $8$",
             "ước lượng thời gian tự học buổi tối và tìm hiểu môn học được ưu tiên ôn tập của học sinh khối $8$ trong trường",
             "Mỗi tối bạn làm xong bài tập của bao nhiêu môn học?",
             "Thời gian tự học buổi tối trung bình của bạn là bao nhiêu giờ?",
             "Môn học nào bạn dành nhiều thời gian tự học nhất?"),
            ("Thói quen rèn luyện thể dục thể thao hằng ngày của học sinh khối $8$",
             "tìm hiểu mức độ tham gia vận động thể chất và môn thể thao phổ biến của học sinh khối $8$",
             "Mỗi tuần bạn tham gia tập thể dục thể thao bao nhiêu buổi?",
             "Mỗi buổi tập của bạn kéo dài trung bình bao nhiêu phút?",
             "Môn thể thao nào bạn yêu thích nhất?")
        ]
        ten_cd, muc_tieu, ch_rr, ch_lt, ch_ks = random.choice(chu_de_list)

        bang_mau = (
            "\\begin{center}\n"
            "\\begin{tabular}{|c|l|l|}\n"
            "\\hline\n"
            "\\textbf{Câu hỏi} & \\textbf{Nội dung câu hỏi khảo sát} & \\textbf{Loại dữ liệu thu được} \\\\\n"
            "\\hline\n"
            "$1$ & %s & Số liệu rời rạc \\\\\n"
            "\\hline\n"
            "$2$ & %s & Số liệu liên tục \\\\\n"
            "\\hline\n"
            "$3$ & %s & Dữ liệu không là số \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (ch_rr, ch_lt, ch_ks)
        )

        noidungcauhoi = ('''Xét dự án thống kê thực tế gắn với đời sống học đường có chủ đề: \\textit{"%s"}. Hãy xây dựng bản kế hoạch thực hiện dự án gồm các nội dung sau:\\\\
a) Xác định mục tiêu khảo sát và đối tượng được quan tâm.\\\\
b) Đề xuất phương pháp thu thập dữ liệu và cách chọn mẫu để đảm bảo tính đại diện.\\\\
c) Trình bày $3$ câu hỏi khảo sát sao cho dữ liệu thu về bao gồm đủ cả \\textbf{số liệu rời rạc}, \\textbf{số liệu liên tục}, và \\textbf{dữ liệu không là số} (giải thích rõ từng loại).'''
                         % ten_cd)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item \\textbf{Mục tiêu khảo sát:} Nhằm %s. \\textbf{Đối tượng được quan tâm:} Toàn thể học sinh khối $8$ của nhà trường.
\\item \\textbf{Phương pháp thu thập và chọn mẫu:} Sử dụng \\textbf{phương pháp thu thập dữ liệu trực tiếp} bằng cách lập bảng hỏi (phiếu khảo sát). Để đảm bảo tính đại diện, chọn ngẫu nhiên mỗi lớp khối $8$ khoảng $10$ học sinh (gồm cả nam và nữ ở các mức học lực khác nhau) để phát phiếu khảo sát.
\\item Hệ thống $3$ câu hỏi khảo sát tương ứng với ba loại dữ liệu được tổng hợp trong bảng sau:
%s
- Câu $1$ thu được từ phép đếm nên là \\textbf{số liệu rời rạc}.\\\\
- Câu $2$ thu được từ phép đo thời gian nên là \\textbf{số liệu liên tục}.\\\\
- Câu $3$ cho kết quả là tên gọi, không có thứ bậc nên là \\textbf{dữ liệu không là số, không thể sắp thứ tự}.
\\end{enumEX}''' % (muc_tieu, bang_mau))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
