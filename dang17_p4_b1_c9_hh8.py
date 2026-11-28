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


def bt_dang17_p4_b1_c9_hh8(self):
    # Dạng 17: Tính chiều cao tòa nhà bằng phương pháp ngắm qua gương phẳng đặt trên mặt đất
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([15, 20, 25])
        h_nguoi_cm = random.choice([150, 160, 170])
        h_nguoi = Decimal(h_nguoi_cm) / Decimal(100)
        str_h_nguoi = str(h_nguoi).replace('.', ',')
        
        d_nguoi_cm = random.choice([120, 140, 150])
        d_nguoi = Decimal(d_nguoi_cm) / Decimal(100)
        str_d_nguoi = str(d_nguoi).replace('.', ',')
        
        d_nha = d_nguoi * Decimal(k)
        str_d_nha = str(d_nha.normalize()).replace('.', ',')
        
        h_nha = h_nguoi * Decimal(k)
        str_h_nha = str(h_nha.normalize()).replace('.', ',')
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (A) at (0,1.4);\n'
            '\\coordinate (E) at (2,0);\n'
            '\\coordinate (D) at (6.5,0);\n'
            '\\coordinate (C) at (6.5,3.15);\n'
            '\\draw[line width=1pt] (B)--(D) (B)--(A) (D)--(C) (A)--(E)--(C);\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (E) circle (1pt) node[below] {$E$};\n'
            '\\fill (D) circle (1pt) node[below right] {$D$};\n'
            '\\fill (C) circle (1pt) node[above right] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Một bạn học sinh có tầm mắt cao $AB = %s\\text{ m}$ muốn đo chiều cao $CD$ của một tòa nhà văn phòng. '
            'Bạn đặt một chiếc gương phẳng nhỏ nằm ngửa trên mặt đất tại điểm $E$ cách chân tòa nhà $ED = %s\\text{ m}$, '
            'sau đó lùi lại phía sau cách gương $EB = %s\\text{ m}$ ($B, E, D$ thẳng hàng) thì nhìn thấy đỉnh $C$ của tòa nhà nằm chính giữa tâm gương. '
            'Biết rằng góc tới bằng góc phản xạ nên $\\widehat{AEB} = \\widehat{CED}$ và $AB \\perp BD$, $CD \\perp BD$. '
            'Hãy tính chiều cao $CD$ của tòa nhà.\\\n%s'
            % (str_h_nguoi, str_d_nha, str_d_nguoi, tikz)
        )
        
        loigiai = (
            'Lấy điểm $A^{\prime}$ đối xứng với $A$ qua mặt đất $BD$ ($B$ là trung điểm của $AA^{\prime}$).\\\n'
            'Khi đó $BA^{\prime} = AB = %s\\text{ m}$ và $\\widehat{A^{\prime}EB} = \\widehat{AEB}$.\\\n'
            'Mà theo định luật phản xạ ánh sáng, $\\widehat{AEB} = \\widehat{CED}$, suy ra $\\widehat{A^{\prime}EB} = \\widehat{CED}$.\\\n'
            'Do đó ba điểm $A^{\prime}, E, C$ thẳng hàng.\\\n'
            'Xét $\\Delta EDC$ có đường thẳng $BA^{\prime}$ cắt phần kéo dài của hai cạnh $EC, ED$ tại $A^{\prime}, B$ và $BA^{\prime} // CD$ (cùng vuông góc với $BD$).\\\n'
            'Theo hệ quả định lí về hai tam giác đồng dạng, ta có $\\Delta EBA^{\prime} \\backsim \\Delta EDC$.\\\n'
            'Suy ra $\\dfrac{BA^{\prime}}{CD} = \\dfrac{EB}{ED} \\Rightarrow \\dfrac{%s}{CD} = \\dfrac{%s}{%s} \\Rightarrow CD = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (m)}$.\\\n'
            'Vậy chiều cao của tòa nhà là $%s\\text{ m}$.'
            % (str_h_nguoi, str_h_nguoi, str_d_nguoi, str_d_nha, str_h_nguoi, str_d_nha, str_d_nguoi, str_h_nha, str_h_nha)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
