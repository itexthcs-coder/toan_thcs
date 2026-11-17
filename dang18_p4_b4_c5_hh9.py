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


def bt_dang18_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = 3 * randint(3, 10)
        om = 2 * r
        ma = r * sqrt(3)
        cung = Rational(4 * r, 3)
        tong_exact = 2 * ma + cung * 3.14
        tong_dec = Decimal(str(float(tong_exact))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        tong_str = str(tong_dec).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Người ta dùng một sợi dây đai không dãn căng chặt để cố định một ống thép hình trụ bán kính $R = %s\\text{ cm}$ vào một chốt nhọn tại điểm $M$ nằm cách tâm ống $O$ một khoảng $MO = %s\\text{ cm}$ (hai nhánh dây đai $MA$, $MB$ tiếp xúc với ống thép lần lượt tại $A$ và $B$). Tính tổng chiều dài phần dây đai từ điểm $M$ ôm vòng qua mặt sau ống thép trở về điểm $M$ (lấy $\\pi \\approx 3,14$ và làm tròn kết quả đến chữ số thập phân thứ hai). \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate (M) at (-3.2,0);
            \\coordinate (A) at (-0.8,1.3856);
            \\coordinate (B) at (-0.8,-1.3856);
            \\draw[line width=1pt] (A) arc (120:-120:1.6);
            \\draw[line width=1pt, dashed] (A) arc (120:240:1.6);
            \\draw[line width=1pt] (M)--(A) (M)--(B);
            \\draw[line width=1pt, dashed] (M)--(O) (O)--(A) (O)--(B);
            \\fill (O) circle (1pt) node[right] {$O$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(r), latex(om)))

        # Nội dung lời giải
        loigiai = ('''Vì $MA$ và $MB$ là hai tiếp tuyến của đường tròn $(O; %s\\text{ cm})$ cắt nhau tại $M$ nên $\\widehat{OAM} = \\widehat{OBM} = 90^\\circ$, $MA = MB$ và $OM$ là tia phân giác của góc $\\widehat{AOB}$. \\\\
        Xét tam giác $OAM$ vuông tại $A$, áp dụng định lí Pythagore ta có: \\\\
        $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)} \\Rightarrow MB = %s\\text{ cm}$. \\\\
        Mặt khác, $\\cos \\widehat{AOM} = \\dfrac{OA}{OM} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{AOM} = 60^\\circ$. \\\\
        Suy ra $\\widehat{AOB} = 2\\widehat{AOM} = 2 \\cdot 60^\\circ = 120^\\circ$. \\\\
        Do đó, cung lớn $\\wideparen{AB}$ mà dây đai ôm vòng qua phía sau ống thép có số đo là: \\\\
        $360^\\circ - 120^\\circ = 240^\\circ$. \\\\
        Độ dài cung lớn $\\wideparen{AB}$ là: \\\\
        $l = \\dfrac{\\pi \\cdot R \\cdot 240}{180} = \\dfrac{\\pi \\cdot %s \\cdot 4}{3} = %s\\pi\\text{ (cm)}$. \\\\
        Vậy tổng chiều dài phần dây đai cần dùng là: \\\\
        $L = MA + MB + l = %s + %s + %s \\cdot 3,14 \\approx %s\\text{ (cm)}$.'''
        %(latex(r), latex(om), latex(r), latex(ma), latex(ma), latex(r), latex(om), latex(r), latex(cung), latex(ma), latex(ma), latex(cung), tong_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
