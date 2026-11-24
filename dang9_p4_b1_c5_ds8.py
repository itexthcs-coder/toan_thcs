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


def bt_dang9_p4_b1_c5_ds8(self):
    # Dạng 9: Thiết kế khảo sát nhu cầu câu lạc bộ ngoại khóa sau giờ học
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        noidungcauhoi = ('''Liên đội trường trung học cơ sở muốn thành lập các câu lạc bộ ngoại khóa (\\textit{Bóng rổ, Cờ vua, Mỹ thuật, Tin học, Nhảy hiện đại}) và khảo sát nhu cầu tham gia của học sinh toàn trường.\\\\
a) Hãy xây dựng một quy trình thu thập dữ liệu gồm $3$ bước cụ thể để đảm bảo tính khách quan và đại diện cho tất cả học sinh.\\\\
b) Nếu phiếu khảo sát gồm hai câu hỏi: \\textit{Câu 1: "Bạn muốn đăng kí tham gia câu lạc bộ nào?"} và \\textit{Câu 2: "Bạn có thể dành bao nhiêu giờ mỗi tuần để tham gia câu lạc bộ?"}, hãy phân loại dữ liệu thu được ở từng câu hỏi.''' % ())

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Quy trình thu thập dữ liệu gồm $3$ bước cụ thể:\\\\
- \\textbf{Bước 1 (Thiết kế công cụ):} Xây dựng phiếu khảo sát ngắn gọn, rõ ràng (trên giấy hoặc biểu mẫu trực tuyến) nêu rõ danh sách các câu lạc bộ dự kiến.\\\\
- \\textbf{Bước 2 (Chọn mẫu đại diện):} Chọn ngẫu nhiên một tỉ lệ học sinh đồng đều (ví dụ $20\\%%$ sĩ số) ở tất cả các lớp thuộc cả $4$ khối $6, 7, 8, 9$ để đảm bảo mọi lứa tuổi đều được tham gia ý kiến.\\\\
- \\textbf{Bước 3 (Thu thập và làm sạch dữ liệu):} Phát phiếu trực tiếp cho các học sinh được chọn, thu hồi đầy đủ và loại bỏ các phiếu bỏ trống hoặc ghi thông tin không hợp lí.
\\item Phân loại dữ liệu:\\\\
- Câu $1$ cho kết quả là tên câu lạc bộ yêu thích nên là \\textbf{dữ liệu không là số, không thể sắp thứ tự}.\\\\
- Câu $2$ cho kết quả là thời gian (tính theo giờ) có thể nhận giá trị thực tùy ý trong một khoảng nên là \\textbf{số liệu liên tục}.
\\end{enumEX}''' % ())

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
