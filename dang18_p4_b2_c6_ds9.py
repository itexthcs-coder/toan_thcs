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


def bt_dang18_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x_ans = randint(1, 3)
        gia_moi = 80 - 5 * x_ans
        khach_moi = 200 + 25 * x_ans
        doanh_thu_nghin = gia_moi * khach_moi
        doanh_thu_trieu = Rational(doanh_thu_nghin, 1000)
        dt_str = str(float(doanh_thu_trieu)).replace('.', ',') if doanh_thu_nghin % 1000 != 0 else str(doanh_thu_nghin // 1000)
        
        rhs = doanh_thu_nghin // 125
        c_pt = rhs - 128
        delta = 64 - 4 * c_pt
        x_other = 8 - x_ans
        gia_other = 80 - 5 * x_other
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một rạp chiếu phim có sức chứa $300$ ghế. Với giá vé hiện tại là $80\\text{ nghìn đồng/vé}$, trung bình mỗi suất chiếu có $200$ khán giả đến xem. Qua khảo sát thị trường, quản lý rạp nhận thấy cứ giảm giá vé đi $5\\text{ nghìn đồng}$ thì số lượng khán giả lại tăng thêm $25$ người. Hỏi rạp chiếu phim nên đặt giá vé là bao nhiêu để doanh thu một suất chiếu đạt $%s\\text{ triệu đồng}$ (biết rạp muốn ưu tiên mức giá vé thấp hơn để thu hút nhiều khán giả nhất)?'''
                         %(dt_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Đổi đơn vị: $%s\\text{ triệu đồng} = %s\\text{ nghìn đồng}$. \\\\
                   Gọi số lần giảm giá vé (mỗi lần giảm $5\\text{ nghìn đồng}$) là $x$ (lần). \\\\
                   Khi đó, giá vé mới là $80 - 5x$ (nghìn đồng) và số lượng khán giả là $200 + 25x$ (người). \\\\
                   Điều kiện: $0 < 80 - 5x < 80$ và $200 + 25x \\le 300 \\Leftrightarrow 0 < x \\le 4$. \\\\
                   Doanh thu một suất chiếu là $(80 - 5x)(200 + 25x)$ (nghìn đồng). \\\\
                   Theo đề bài, ta có phương trình: \\\\
                   $(80 - 5x)(200 + 25x) = %s$ \\\\
                   $\\Leftrightarrow 5(16 - x) \\cdot 25(8 + x) = %s$ \\\\
                   $\\Leftrightarrow 125(128 + 8x - x^2) = %s$ \\\\
                   $\\Leftrightarrow 128 + 8x - x^2 = %s$ \\\\
                   $\\Leftrightarrow x^2 - 8x + %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 1$, $b = -8$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = (-8)^2 - 4 \\cdot 1 \\cdot %s = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{8 - \\sqrt{%s}}{2 \\cdot 1} = %s$; \\\\
                   $x_2 = \\dfrac{8 + \\sqrt{%s}}{2 \\cdot 1} = %s$. \\\\
                   Vì rạp muốn ưu tiên mức giá vé thấp hơn (tương ứng số lần giảm giá nhiều hơn) nên ta chọn $x = %s$ (thỏa mãn $0 < x \\le 4$). \\\\
                   Vậy rạp chiếu phim nên đặt giá vé là $80 - 5 \\cdot %s = %s\\text{ nghìn đồng/vé}$.'''
                   %(dt_str, latex(doanh_thu_nghin),
                     latex(doanh_thu_nghin),
                     latex(doanh_thu_nghin),
                     latex(doanh_thu_nghin),
                     latex(rhs),
                     latex(c_pt),
                     latex(c_pt),
                     latex(c_pt), latex(delta),
                     latex(delta), latex(x_ans),
                     latex(delta), latex(x_other),
                     latex(x_other),
                     latex(x_other), latex(gia_other)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
