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


def bt_dang3_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        half_a = random.randint(3, 12)
        a = 2 * half_a
        diff_sq = half_a ** 2
        val = 3.14 * diff_sq
        number = Decimal(str(val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn đồng tâm $(O; R)$ và $(O; r)$ ($R > r$). Một dây cung $MN$ của đường tròn lớn tiếp xúc với đường tròn nhỏ và có độ dài $MN = %d\\text{ cm}$. Tính diện tích hình vành khuyên giới hạn bởi hai đường tròn đó theo đơn vị $\\text{cm}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng đơn vị).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[teal!12] (0,0) circle (2.2);
\\fill[white] (0,0) circle (1.3);
\\draw (0,0) circle (2.2);
\\draw (0,0) circle (1.3);
\\draw[thick] (-1.77,-1.3) -- (1.77,-1.3);
\\draw[dashed] (0,0) -- (0,-1.3);
\\draw[dashed] (0,0) -- (-1.77,-1.3);
\\draw (0,-1.12) -- (0.18,-1.12) -- (0.18,-1.3);
\\fill (0,0) circle (1.5pt) node[above] {$O$};
\\fill (0,-1.3) circle (1.5pt) node[below] {$H$};
\\node[left] at (-1.77,-1.3) {$M$};
\\node[right] at (1.77,-1.3) {$N$};
\\node[left] at (-0.9,-0.55) {$R$};
\\node[right] at (0,-0.65) {$r$};
\\end{tikzpicture}
\\end{center}''' % (a))

        # Nội dung lời giải
        loigiai = ('''Gọi $H$ là tiếp điểm của dây cung $MN$ với đường tròn $(O; r)$. \\\\
Vì $MN$ tiếp xúc với $(O; r)$ tại $H$ nên $OH \\perp MN$ và $OH = r$. \\\\
Đường kính vuông góc với dây cung thì đi qua trung điểm của dây đó nên $MH = \\dfrac{MN}{2} = \\dfrac{%d}{2} = %d\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore trong tam giác $OMH$ vuông tại $H$, ta có:
$$R^2 - r^2 = OM^2 - OH^2 = MH^2 = %d^2 = %d.$$
Diện tích hình vành khuyên cần tìm là:
$$S_v = \\pi(R^2 - r^2) \\approx 3,14 \\cdot %d \\approx %s\\text{ (cm}^2\\text{)}.$$''' % (
            a, half_a, half_a, diff_sq, diff_sq, kq_str))

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
