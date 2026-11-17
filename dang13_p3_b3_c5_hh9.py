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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang13_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([25, 30, 35])
        n = random.choice([12, 15, 18, 20])
        R_m = R / 100
        R_m_str = str(R_m).replace('.', ',')
        val = 60 * (n / 180) * 3.14 * R_m
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Thanh treo của một chiếc đồng hồ quả lắc có chiều dài $%d\\text{ cm}$. Khi đồng hồ hoạt động, thanh treo dao động đều đặn từ vị trí biên trái sang vị trí biên phải tạo thành một góc $%d^\\circ$, mất $1\\text{ giây}$ cho mỗi lượt đi từ biên này sang biên kia. Hỏi trong $1\\text{ phút}$, đầu mút dưới của thanh treo đi được quãng đường dài bao nhiêu mét (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\draw[thick] (0,0) -- (-105:2.4);
\\draw[dashed] (0,0) -- (-75:2.4);
\\draw[<->, thick, red] (-105:2.4) arc (-105:-75:2.4);
\\filldraw[fill=orange!50] (-105:2.4) circle (0.22);
\\filldraw[dashed, fill=orange!20] (-75:2.4) circle (0.22);
\\fill (0,0) circle (2pt) node[above] {$O$};
\\node at (-90:1.3) {$%d^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (R, n, n))

        # Nội dung lời giải
        loigiai = ('''Đổi chiều dài thanh treo $R = %d\\text{ cm} = %s\\text{ m}$ và thời gian $1\\text{ phút} = 60\\text{ giây}$. \\\\
Trong mỗi giây ($1$ lượt dao động), đầu mút dưới của thanh treo vạch nên một cung tròn có số đo $%d^\\circ$ trên đường tròn bán kính $R = %s\\text{ m}$, có độ dài là:
$$l = \\dfrac{%d}{180}\\pi R \\approx \\dfrac{%d}{180} \\cdot 3,14 \\cdot %s\\text{ (m)}.$$
Trong $60\\text{ giây}$ ($60$ lượt dao động), tổng quãng đường đầu mút dưới đi được là:
$$L = 60 \\cdot l \\approx 60 \\cdot \\dfrac{%d}{180} \\cdot 3,14 \\cdot %s \\approx %s\\text{ (m)}.$$''' % (
            R, R_m_str, n, R_m_str, n, n, R_m_str, n, R_m_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
