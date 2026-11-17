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


def bt_dang12_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(80, 150)
        delta_d = randint(20, 60)
        d0 = r + delta_d
        s = 2 * delta_d

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cơn bão có tâm ở vị trí $O$, vùng gió mạnh nguy hiểm được xác định là hình tròn tâm $O$ bán kính $R = %s\\text{ km}$. Đường bờ biển của một tỉnh được xem như một đường thẳng $a$. Tại thời điểm khảo sát, tâm bão $O$ cách bờ biển $a$ một khoảng $%s\\text{ km}$ và đang di chuyển thẳng về phía bờ biển theo phương tạo với đường bờ biển một góc $30^\\circ$. Hỏi tâm bão phải di chuyển thêm bao nhiêu ki-lô-mét nữa thì vùng gió mạnh bắt đầu chạm tới bờ biển? \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (-2.5,2.4);
            \\coordinate (Op) at (-0.42,1.2);
            \\coordinate (H) at (-2.5,0);
            \\coordinate (Hp) at (-0.42,0);
            \\coordinate (K) at (-0.42,2.4);
            \\coordinate (M) at (1.66,0);
            \\draw[line width=1pt] (-3.5,0)--(3,0) node[below] {$a$};
            \\draw[line width=1pt] (Op) circle (1.2);
            \\draw[line width=1pt] (O)--(M);
            \\draw[line width=1pt, dashed] (O)--(H) (Op)--(Hp) (Op)--(K);
            \\fill (O) circle (1pt) node[above left] {$O$};
            \\fill (Op) circle (1pt) node[above right] {$O'$};
            \\fill (H) circle (1pt) node[below] {$H$};
            \\fill (Hp) circle (1pt) node[below] {$H'$};
            \\fill (K) circle (1pt) node[above] {$K$};
            \\fill (M) circle (1pt) node[below] {$M$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(r), latex(d0)))

        # Nội dung lời giải
        loigiai = ('''Gọi $O'$ là vị trí của tâm bão khi vùng gió mạnh bắt đầu chạm tới bờ biển $a$. Khi đó đường tròn $(O'; %s)$ tiếp xúc với đường thẳng $a$ tại $H'$, nên khoảng cách từ $O'$ đến đường thẳng $a$ là $O'H' = R = %s\\text{ km}$. \\\\
        Kẻ $OH \\perp a$ tại $H$ ($OH = %s\\text{ km}$) và kẻ $O'K \\perp OH$ tại $K$. \\\\
        Tứ giác $O'H'HK$ có ba góc vuông nên là hình chữ nhật, suy ra $KH = O'H' = %s\\text{ km}$. \\\\
        Do đó $OK = OH - KH = %s - %s = %s\\text{ (km)}$. \\\\
        Vì $O'K // a$ nên $\\widehat{OO'K} = 30^\\circ$ (hai góc đồng vị). \\\\
        Xét tam giác $OO'K$ vuông tại $K$, quãng đường $OO'$ mà tâm bão di chuyển là: \\\\
        $OO' = \\dfrac{OK}{\\sin 30^\\circ} = \\dfrac{%s}{0,5} = %s\\text{ (km)}$. \\\\
        Vậy tâm bão phải di chuyển thêm $%s\\text{ km}$ nữa thì vùng gió mạnh bắt đầu chạm tới bờ biển.'''
        %(latex(r), latex(r), latex(d0), latex(r), latex(d0), latex(r), latex(delta_d), latex(delta_d), latex(s), latex(s)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
