# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""

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


def bt_dang2_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab_val = random.randint(4, 7)
        ad_val = ab_val + random.randint(2, 4)
        s_hcn = ab_val * ad_val
        cv_hcn = 2 * (ab_val + ad_val)
        nua_cv = ab_val + ad_val
        sxq_chung = 2 * s_hcn
        ti_so_v = Rational(ad_val, ab_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho một hình chữ nhật $ABCD$ có diện tích bằng $%s\\text{ cm}^2$. Nếu quay hình chữ nhật quanh cạnh $AB$ một vòng ta được hình trụ có diện tích xung quanh là $S_1$, nếu quay quanh cạnh $AD$ một vòng ta được hình trụ có diện tích xung quanh là $S_2$ (như hình vẽ). \\\\
a) Chứng minh rằng $S_1 = S_2$ và tính giá trị chung đó. \\\\
b) Biết thêm chu vi hình chữ nhật $ABCD$ bằng $%s\\text{ cm}$ ($AB < AD$), hãy tính tỉ số thể tích $\\frac{V_1}{V_2}$ của hai hình trụ tạo thành.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,1.8);
\\coordinate (B) at (0,0);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (2.6,1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[above] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (s_hcn, cv_hcn))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khi quay hình chữ nhật $ABCD$ quanh cạnh $AB$ một vòng, ta được hình trụ có bán kính đáy $R_1 = AD$ và chiều cao $h_1 = AB$. Diện tích xung quanh của hình trụ này là:
$$S_1 = 2\\pi R_1 h_1 = 2\\pi \\cdot AD \\cdot AB.$$
Khi quay hình chữ nhật $ABCD$ quanh cạnh $AD$ một vòng, ta được hình trụ có bán kính đáy $R_2 = AB$ và chiều cao $h_2 = AD$. Diện tích xung quanh của hình trụ này là:
$$S_2 = 2\\pi R_2 h_2 = 2\\pi \\cdot AB \\cdot AD.$$
Vậy $S_1 = S_2 = 2\\pi \\cdot S_{ABCD} = 2\\pi \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.
\\item Nửa chu vi hình chữ nhật $ABCD$ là $AB + AD = \\frac{%s}{2} = %s\\text{ (cm)}$. \\\\
Vì $AB \\cdot AD = %s$ và $AB < AD$ nên tìm được $AB = %s\\text{ cm}$ và $AD = %s\\text{ cm}$. \\\\
Tỉ số thể tích của hai hình trụ tạo thành là:
$$\\frac{V_1}{V_2} = \\frac{\\pi R_1^2 h_1}{\\pi R_2^2 h_2} = \\frac{\\pi \\cdot AD^2 \\cdot AB}{\\pi \\cdot AB^2 \\cdot AD} = \\frac{AD}{AB} = \\frac{%s}{%s} = %s.$$
\\end{enumEX}'''
                   % (s_hcn, sxq_chung, cv_hcn, nua_cv, s_hcn, ab_val, ad_val, ad_val, ab_val, latex(ti_so_v)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
