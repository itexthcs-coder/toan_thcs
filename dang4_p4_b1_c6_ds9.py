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


def bt_dang4_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh = random.choice([2, 4, 6, 8])
        nua_canh = canh // 2
        a_res = Rational(1, nua_canh) * sqrt(3)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho parabol $(P): y = ax^2$ ($a > 0$). Tìm hệ số $a$ biết rằng trên $(P)$ có hai điểm $A$ và $B$ đối xứng nhau qua trục tung sao cho tam giác $OAB$ là tam giác đều có cạnh bằng $%s$.'''
                         %(latex(canh)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi $H$ là giao điểm của đoạn thẳng $AB$ với trục tung $Oy$. \\\\
Vì $A$ và $B$ đối xứng nhau qua trục tung $Oy$ và nằm phía trên trục hoành (do $a > 0$) nên $Oy$ là đường trung trực của đoạn thẳng $AB$, suy ra $OH \\perp AB$ và $HA = HB = \\frac{AB}{2} = \\frac{%s}{2} = %s$. \\\\
Xét tam giác $OAB$ đều có cạnh bằng $%s$, đường cao $OH$ được tính theo định lý Pythagore trong tam giác vuông $OHB$: \\\\
$OH = \\sqrt{OB^2 - HB^2} = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3}$. \\\\
Giả sử điểm $B$ nằm bên phải trục tung, khi đó tọa độ điểm $B$ là $\\left(%s; %s\\sqrt{3}\\right)$. \\\\
Vì điểm $B$ thuộc parabol $(P): y = ax^2$ nên thay $x = %s$ và $y = %s\\sqrt{3}$ vào công thức hàm số, ta được: \\\\
$%s\\sqrt{3} = a \\cdot %s^2$ \\\\
$%sa = %s\\sqrt{3}$ \\\\
$a = %s$ (thỏa mãn điều kiện $a > 0$). \\\\
Vậy $a = %s$. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.4:2.4] plot(\\x, {0.866*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2,3.464);
\\coordinate (B) at (2,3.464);
\\coordinate (H) at (0,3.464);
\\draw[line width=1pt] (O)--(A)--(B)--cycle;
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\end{tikzpicture}
\\end{center}'''
                   %(latex(canh), latex(nua_canh),
                     latex(canh),
                     latex(canh), latex(nua_canh), latex(nua_canh),
                     latex(nua_canh), latex(nua_canh),
                     latex(nua_canh), latex(nua_canh),
                     latex(nua_canh), latex(nua_canh),
                     latex(nua_canh**2), latex(nua_canh),
                     latex(a_res),
                     latex(a_res)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
