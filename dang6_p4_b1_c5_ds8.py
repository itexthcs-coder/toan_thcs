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


def bt_dang6_p4_b1_c5_ds8(self):
    # Dạng 6: Lập kế hoạch khảo sát chất lượng nước sinh hoạt khu dân cư
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        so_to = random.choice([8, 10, 12])
        so_ho_to = random.choice([2, 3])
        tong_mau = so_to * so_ho_to

        tikz_phuong = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n"
            "\\draw[line width=1pt] (0,0) rectangle (6,2.2);\n"
            "\\draw[line width=1pt] (2,0) -- (2,2.2) (4,0) -- (4,2.2) (0,1.1) -- (6,1.1);\n"
            "\\fill (1.0,1.65) circle (1pt) node[right] {Mẫu A};\n"
            "\\fill (3.0,0.55) circle (1pt) node[right] {Mẫu B};\n"
            "\\fill (5.0,1.65) circle (1pt) node[right] {Mẫu C};\n"
            "\\node at (3,-0.35) {Sơ đồ phân bố điểm lấy mẫu nước tại các tổ dân phố};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = ('''Một nhóm nghiên cứu môi trường muốn đánh giá chất lượng nguồn nước máy tại một phường gồm $%s$ tổ dân phố thông qua việc lấy mẫu nước tại các hộ gia đình để đo \\textit{Độ pH của nước}, \\textit{Hàm lượng clo dư (mg/l)}, và ghi nhận \\textit{Cảm quan về mùi của nước (Không mùi, Mùi nhẹ, Mùi nồng)}.
%s
a) Phương pháp thu thập dữ liệu được sử dụng ở đây là gì? Để đảm bảo tính đại diện cho toàn phường, nhóm cần chọn vị trí lấy mẫu như thế nào?\\\\
b) Phân loại dữ liệu của ba chỉ tiêu quan trắc trên.''' % (so_to, tikz_phuong))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Nhóm nghiên cứu trực tiếp lấy mẫu nước, đo đạc các thông số hóa lí và kiểm tra cảm quan nên đây là \\textbf{phương pháp thu thập dữ liệu trực tiếp} (thông qua làm thí nghiệm và quan sát). Để đảm bảo tính đại diện cho toàn phường, nhóm cần chọn ngẫu nhiên ở mỗi tổ dân phố khoảng $%s$ hộ gia đình nằm ở các vị trí khác nhau (đầu nguồn, giữa tuyến và cuối tuyến ống dẫn nước, tổng cộng $%s$ mẫu).
\\item Phân loại dữ liệu của ba chỉ tiêu:\\\\
- \\textit{Độ pH của nước}: nhận giá trị thực tùy ý trong khoảng từ $0$ đến $14$ nên là \\textbf{số liệu liên tục}.\\\\
- \\textit{Hàm lượng clo dư (mg/l)}: thu được từ phép đo nồng độ nên là \\textbf{số liệu liên tục}.\\\\
- \\textit{Cảm quan về mùi của nước (Không mùi, Mùi nhẹ, Mùi nồng)}: không phải là số nhưng sắp xếp được theo mức độ mùi tăng dần nên là \\textbf{dữ liệu không là số, có thể sắp thứ tự}.
\\end{enumEX}''' % (so_ho_to, tong_mau))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
