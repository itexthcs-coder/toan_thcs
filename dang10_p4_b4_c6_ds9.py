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


def bt_dang10_p4_b4_c6_ds9(self):
    def fmt_vn(val):
        s = f"{val.normalize():f}"
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t1 = randint(1, 2)
        t2 = t1 + randint(1, 2)
        h0 = random.choice([Decimal('1.2'), Decimal('1.5'), Decimal('1.8'), Decimal('2.0')])
        g_half = Decimal('4.9')
        v0 = g_half * (t1 + t2)
        h_muc_tieu = h0 + g_half * t1 * t2
        h_diff = h_muc_tieu - h0
        tong_t = t1 + t2
        tich_t = t1 * t2
        delta = tong_t**2 - 4 * tich_t
        can_delta = int(math.isqrt(delta))

        h0_str = fmt_vn(h0)
        v0_str = fmt_vn(v0)
        h_mt_str = fmt_vn(h_muc_tieu)
        h_diff_str = fmt_vn(h_diff)

        noidungcauhoi = ('''Một quả bóng được ném thẳng đứng lên cao từ độ cao $%s\\text{ m}$ so với mặt đất. Độ cao $h\\text{ (m)}$ của quả bóng sau $t$ giây ($t \\ge 0$) được cho bởi công thức $h = -4,9t^2 + %st + %s$. \\\\
a) Xác định độ cao của quả bóng tại thời điểm bắt đầu ném ($t = 0$). \\\\
b) Tìm các thời điểm $t$ mà tại đó quả bóng đạt độ cao $%s\\text{ m}$ so với mặt đất.'''
                         %(h0_str, v0_str, h0_str, h_mt_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thay $t = 0$ vào công thức $h = -4,9t^2 + %st + %s$, ta được: \\\\
$h = -4,9 \\cdot 0^2 + %s \\cdot 0 + %s = %s\\text{ (m)}$. \\\\
Vậy tại thời điểm bắt đầu ném, quả bóng ở độ cao $%s\\text{ m}$.
\\item Để quả bóng đạt độ cao $%s\\text{ m}$, ta thay $h = %s$ vào công thức đã cho: \\\\
$-4,9t^2 + %st + %s = %s$ hay $-4,9t^2 + %st - %s = 0$. \\\\
Chia cả hai vế của phương trình cho $-4,9$, ta được phương trình bậc hai: \\\\
$t^2 - %st + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot %s = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$t_1 = \\frac{%s - %s}{2} = %s$ (thoả mãn điều kiện); \\quad $t_2 = \\frac{%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\
Vậy quả bóng đạt độ cao $%s\\text{ m}$ tại hai thời điểm là $t = %s$ giây (khi đang bay lên) và $t = %s$ giây (khi đang rơi xuống).
\\end{enumEX}'''
                   %(v0_str, h0_str, v0_str, h0_str, h0_str, h0_str,
                     h_mt_str, h_mt_str, v0_str, h0_str, h_mt_str, v0_str, h_diff_str,
                     latex(tong_t), latex(tich_t),
                     latex(tong_t), latex(tich_t), latex(delta), latex(can_delta),
                     latex(tong_t), latex(can_delta), latex(t1), latex(tong_t), latex(can_delta), latex(t2),
                     h_mt_str, latex(t1), latex(t2)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
