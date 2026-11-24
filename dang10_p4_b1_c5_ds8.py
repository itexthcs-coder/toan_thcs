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


def bt_dang10_p4_b1_c5_ds8(self):
    # Dạng 10: Phân tích dữ liệu kinh doanh tại một cửa hàng sách
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        s1 = random.randint(45, 75)
        s2 = random.randint(50, 85)
        d1 = str(round(random.uniform(4.2, 7.8), 1)).replace('.', ',')
        d2 = str(round(random.uniform(5.1, 9.4), 1)).replace('.', ',')

        bang_sach = (
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|}\n"
            "\\hline\n"
            "\\textbf{Chỉ tiêu theo dõi} & \\textbf{Ngày thứ nhất} & \\textbf{Ngày thứ hai} \\\\\n"
            "\\hline\n"
            "Số lượng sách bán ra (quyển) & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "Doanh thu bán hàng (triệu đồng) & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "Thể loại được mua nhiều nhất & Văn học & Khoa học \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (s1, s2, d1, d2)
        )

        noidungcauhoi = ('''Chủ một hiệu sách muốn đánh giá tình hình kinh doanh trong quý I thông qua hai nguồn thông tin: (1) Trích xuất dữ liệu từ phần mềm bán hàng có sẵn (bảng minh họa bên dưới) về \\textit{Số lượng sách bán ra mỗi ngày} và \\textit{Doanh thu mỗi ngày (triệu đồng)}; (2) Phát phiếu khảo sát trực tiếp cho khách hàng tại quầy thanh toán về \\textit{Thể loại sách yêu thích nhất}.
%s
a) Xác định phương pháp thu thập dữ liệu ở mỗi nguồn thông tin $(1)$ và $(2)$.\\\\
b) Phân loại dữ liệu của ba tiêu chí: \\textit{Số lượng sách bán ra}, \\textit{Doanh thu mỗi ngày}, và \\textit{Thể loại sách yêu thích nhất}.''' % bang_sach)

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xác định phương pháp thu thập dữ liệu:\\\\
- Nguồn thông tin $(1)$ trích xuất số liệu lịch sử đã được lưu trữ sẵn trên phần mềm bán hàng nên là \\textbf{phương pháp thu thập dữ liệu gián tiếp}.\\\\
- Nguồn thông tin $(2)$ phát phiếu hỏi trực tiếp khách hàng đến mua sách nên là \\textbf{phương pháp thu thập dữ liệu trực tiếp}.
\\item Phân loại dữ liệu của ba tiêu chí:\\\\
- \\textit{Số lượng sách bán ra mỗi ngày}: thu được từ phép đếm số quyển sách nên là \\textbf{số liệu rời rạc}.\\\\
- \\textit{Doanh thu mỗi ngày (triệu đồng)}: có thể nhận giá trị thực tùy ý trong một khoảng không âm nên là \\textbf{số liệu liên tục}.\\\\
- \\textit{Thể loại sách yêu thích nhất}: biểu diễn bằng tên gọi, không có thứ bậc hơn kém nên là \\textbf{dữ liệu không là số, không thể sắp thứ tự}.
\\end{enumEX}''' % ())

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
