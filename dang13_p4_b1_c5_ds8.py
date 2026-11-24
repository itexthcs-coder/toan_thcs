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


def bt_dang13_p4_b1_c5_ds8(self):
    # Dạng 13: Phân tích dữ liệu giao thông và tai nạn đường bộ từ báo cáo thống kê
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        v1, v2, v3 = random.randint(120, 180), random.randint(90, 140), random.randint(150, 210)
        p1 = str(round(random.uniform(91.5, 96.8), 1)).replace('.', ',')
        p2 = str(round(random.uniform(88.2, 94.5), 1)).replace('.', ',')
        p3 = str(round(random.uniform(93.0, 98.4), 1)).replace('.', ',')

        bang_gt = (
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Địa phương} & \\textbf{Số vụ tai nạn} & \\textbf{Tỉ lệ đội mũ đạt chuẩn (\\%%)} & \\textbf{Mức độ ùn tắc} \\\\\n"
            "\\hline\n"
            "Tỉnh A & $%s$ & $%s$ & Trung bình \\\\\n"
            "\\hline\n"
            "Tỉnh B & $%s$ & $%s$ & Nhẹ \\\\\n"
            "\\hline\n"
            "Tỉnh C & $%s$ & $%s$ & Nghiêm trọng \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (v1, p1, v2, p2, v3, p3)
        )

        noidungcauhoi = ('''Để thực hiện chuyên đề an toàn giao thông, nhóm học sinh lớp $8D$ truy cập cổng thông tin của Ủy ban An toàn giao thông Quốc gia để lấy bảng số liệu của các địa phương (bảng minh họa dưới đây) về: \\textit{Số vụ tai nạn giao thông trong năm}, \\textit{Tỉ lệ người đội mũ bảo hiểm đạt chuẩn (\\%%)}, và \\textit{Mức độ ùn tắc giao thông (Nghiêm trọng, Trung bình, Nhẹ)}.
%s
a) Nhóm học sinh đã sử dụng phương pháp thu thập dữ liệu nào? Nêu ưu điểm của phương pháp này trong tình huống trên.\\\\
b) Hãy phân loại dữ liệu của cả ba cột thông tin trong bảng thống kê trên.''' % bang_gt)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Nhóm học sinh đã sử dụng \\textbf{phương pháp thu thập dữ liệu gián tiếp} vì số liệu được lấy từ cổng thông tin điện tử có sẵn của cơ quan chức năng. Ưu điểm của phương pháp này trong tình huống trên là tiết kiệm thời gian, chi phí và đảm bảo độ tin cậy vì học sinh không thể tự mình thống kê số vụ tai nạn trên phạm vi nhiều tỉnh thành.
\\item Phân loại dữ liệu của ba cột thông tin:\\\\
- Cột \\textit{Số vụ tai nạn}: thu được từ phép đếm nên là \\textbf{số liệu rời rạc}.\\\\
- Cột \\textit{Tỉ lệ người đội mũ bảo hiểm đạt chuẩn (\\%%)}: có thể nhận giá trị thực tùy ý trong đoạn $[0; 100]$ nên là \\textbf{số liệu liên tục}.\\\\
- Cột \\textit{Mức độ ùn tắc giao thông}: biểu thị mức độ từ nhẹ đến nghiêm trọng nên là \\textbf{dữ liệu không là số, có thể sắp thứ tự}.
\\end{enumEX}''' % ())

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
