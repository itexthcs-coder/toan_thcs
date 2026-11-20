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


def bt_dang3_p3_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab_val = random.randint(3, 7)
        hieu_val = random.randint(2, 5)
        ad_val = ab_val + hieu_val
        nua_cv = ab_val + ad_val
        cv_val = 2 * nua_cv
        a_val = (ad_val ** 2) * ab_val
        kq_str = str(a_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình chữ nhật $ABCD$ có chu vi bằng $%s\\text{ cm}$ và chiều dài $AD$ hơn chiều rộng $AB$ là $%s\\text{ cm}$. Quay hình chữ nhật $ABCD$ một vòng quanh cạnh $AB$ cố định để tạo thành một hình trụ (như hình vẽ). Biết thể tích của hình trụ tạo thành có dạng $a\\pi\\text{ (cm}^3\\text{)}$, hãy tìm giá trị của $a$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (1.8,0);
\\coordinate (D) at (1.8,2.2);
\\draw[line width=1pt] (0,2.2) ellipse (1.8 and 0.4);
\\draw[line width=1pt] (-1.8,0) arc (180:360:1.8 and 0.4);
\\draw[line width=1pt, dashed] (1.8,0) arc (0:180:1.8 and 0.4);
\\draw[line width=1pt] (-1.8,0)--(-1.8,2.2) (1.8,0)--(1.8,2.2);
\\draw[line width=1pt, dashed] (A)--(B)--(C) (A)--(D);
\\draw[line width=1pt] (D)--(C);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (cv_val, hieu_val))

        # Nội dung lời giải
        loigiai = ('''Nửa chu vi của hình chữ nhật $ABCD$ là: $AD + AB = \\frac{%s}{2} = %s\\text{ (cm)}$. \\\\
Vì $AD - AB = %s\\text{ cm}$ nên chiều dài là $AD = \\frac{%s + %s}{2} = %s\\text{ (cm)}$ và chiều rộng là $AB = %s - %s = %s\\text{ (cm)}$. \\\\
Khi quay hình chữ nhật $ABCD$ một vòng quanh cạnh $AB$ cố định, ta được hình trụ có chiều cao $h = AB = %s\\text{ cm}$ và bán kính đáy $R = AD = %s\\text{ cm}$. \\\\
Thể tích của hình trụ tạo thành là:
$$V = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Vậy $a = %s$.'''
                   % (cv_val, nua_cv, hieu_val, nua_cv, hieu_val, ad_val, nua_cv, ad_val, ab_val,
                      ab_val, ad_val, ad_val, ab_val, a_val, a_val))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
