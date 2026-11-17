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


def bt_dang11_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ba = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
        hc, oh, r = random.choice(bo_ba)
        cd = 2 * hc

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ngọn hải đăng đặt tại vị trí $O$ phát tín hiệu cảnh báo một bãi đá ngầm được mô hình hóa là hình tròn tâm $O$, bán kính $R = %s\\text{ hải lí}$. Một con tàu di chuyển theo đường thẳng $AB$. Biết khoảng cách ngắn nhất từ ngọn hải đăng $O$ đến đường thẳng $AB$ là $%s\\text{ hải lí}$. Hỏi con tàu có đi vào vùng bãi đá ngầm không? Nếu có, quãng đường con tàu di chuyển bên trong vùng nguy hiểm dài bao nhiêu hải lí? \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate (H) at (0,-1.2);
            \\coordinate (C) at (-1.6,-1.2);
            \\coordinate (D) at (1.6,-1.2);
            \\draw[line width=1pt] (O) circle (2);
            \\draw[line width=1pt] (-3,-1.2) node[above] {$A$} -- (3,-1.2) node[above] {$B$};
            \\draw[line width=1pt, dashed] (O)--(H) (O)--(C) (O)--(D);
            \\fill (O) circle (1pt) node[above] {$O$};
            \\fill (H) circle (1pt) node[below] {$H$};
            \\fill (C) circle (1pt) node[below left] {$C$};
            \\fill (D) circle (1pt) node[below right] {$D$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(r), latex(oh)))

        # Nội dung lời giải
        loigiai = ('''Gọi $H$ là chân đường vuông góc hạ từ ngọn hải đăng $O$ xuống tuyến đường thẳng $AB$. Khi đó khoảng cách từ tâm $O$ đến đường thẳng $AB$ là $d = OH = %s\\text{ hải lí}$. \\\\
        So sánh khoảng cách $d$ và bán kính vùng nguy hiểm $R = %s\\text{ hải lí}$, ta thấy $d < R$ ($%s < %s$). \\\\
        Do đó, đường thẳng $AB$ cắt đường tròn $(O; %s)$ tại hai điểm phân biệt $C$ và $D$, nghĩa là con tàu có đi vào vùng bãi đá ngầm nguy hiểm. \\\\
        Xét tam giác $OHC$ vuông tại $H$ ($OC = R = %s\\text{ hải lí}$, $OH = %s\\text{ hải lí}$), áp dụng định lí Pythagore ta có: \\\\
        $HC = \\sqrt{OC^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (hải lí)}$. \\\\
        Vì $OH \\perp CD$ nên $H$ là trung điểm của dây cung $CD$, suy ra quãng đường con tàu đi trong vùng nguy hiểm là: \\\\
        $CD = 2HC = 2 \\cdot %s = %s\\text{ (hải lí)}$.'''
        %(latex(oh), latex(r), latex(oh), latex(r), latex(r), latex(r), latex(oh), latex(r), latex(oh), latex(hc), latex(hc), latex(cd)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
