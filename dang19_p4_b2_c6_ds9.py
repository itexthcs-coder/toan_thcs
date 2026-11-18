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


def bt_dang19_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        h_cat = randint(3, 5)
        w_ans = randint(12, 18)
        l_ans = 2 * w_ans
        V = h_cat * (w_ans - 2*h_cat) * (2*w_ans - 2*h_cat)
        rhs = V // (2 * h_cat)
        b_pt = -3 * h_cat
        c_pt = 2 * (h_cat**2) - rhs
        delta = b_pt**2 - 4 * c_pt
        w_loai = 3 * h_cat - w_ans
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\draw[line width=1pt] (0,0) rectangle (6,3);
                   \\draw[line width=1pt, dashed] (0.7,0.7) rectangle (5.3,2.3);
                   \\draw[line width=1pt] (0.7,0) -- (0.7,0.7) -- (0,0.7);
                   \\draw[line width=1pt] (5.3,0) -- (5.3,0.7) -- (6,0.7);
                   \\draw[line width=1pt] (0.7,3) -- (0.7,2.3) -- (0,2.3);
                   \\draw[line width=1pt] (5.3,3) -- (5.3,2.3) -- (6,2.3);
                   \\node[left] at (0,1.5) {$x$};
                   \\node[above] at (3,3) {$2x$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Từ một tấm bìa cứng hình chữ nhật có chiều dài gấp đôi chiều rộng, người ta cắt bỏ ở bốn góc bốn hình vuông có cạnh bằng $%s\\text{ cm}$ rồi gấp lại thành một chiếc hộp không nắp có thể tích bằng $%s\\text{ cm}^3$ (như hình vẽ minh họa). Tính chiều dài và chiều rộng của tấm bìa cứng ban đầu. %s'''
                         %(latex(h_cat), latex(V), hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi chiều rộng của tấm bìa cứng ban đầu là $x$ ($\\text{cm}$), điều kiện: $x > %s$. \\\\
                   Vì chiều dài gấp đôi chiều rộng nên chiều dài của tấm bìa ban đầu là $2x$ ($\\text{cm}$). \\\\
                   Sau khi cắt bỏ ở bốn góc bốn hình vuông cạnh $%s\\text{ cm}$ và gấp lên, chiếc hộp hình hộp chữ nhật không nắp thu được có: \\\\
                   - Chiều cao là $%s\\text{ cm}$; \\\\
                   - Chiều rộng đáy là $x - %s$ ($\\text{cm}$); \\\\
                   - Chiều dài đáy là $2x - %s$ ($\\text{cm}$). \\\\
                   Vì thể tích của chiếc hộp bằng $%s\\text{ cm}^3$ nên ta có phương trình: \\\\
                   $%s(x - %s)(2x - %s) = %s$ \\\\
                   $\\Leftrightarrow %s(x - %s)(x - %s) = %s$ \\\\
                   $\\Leftrightarrow (x - %s)(x - %s) = %s$ \\\\
                   $\\Leftrightarrow x^2 - %sx + %s = %s$ \\\\
                   $\\Leftrightarrow x^2 - %sx - %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 1$, $b = %s$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot (%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{%s + \\sqrt{%s}}{2 \\cdot 1} = %s$ (thỏa mãn điều kiện $x > %s$); \\\\
                   $x_2 = \\dfrac{%s - \\sqrt{%s}}{2 \\cdot 1} = %s$ (không thỏa mãn điều kiện nên loại). \\\\
                   Vậy tấm bìa cứng ban đầu có chiều rộng là $%s\\text{ cm}$ và chiều dài là $2 \\cdot %s = %s\\text{ cm}$.'''
                   %(latex(2*h_cat),
                     latex(h_cat),
                     latex(h_cat), latex(2*h_cat), latex(2*h_cat),
                     latex(V),
                     latex(h_cat), latex(2*h_cat), latex(2*h_cat), latex(V),
                     latex(2*h_cat), latex(2*h_cat), latex(h_cat), latex(V),
                     latex(2*h_cat), latex(h_cat), latex(rhs),
                     latex(3*h_cat), latex(2*(h_cat**2)), latex(rhs),
                     latex(3*h_cat), latex(abs(c_pt)),
                     latex(b_pt), latex(c_pt),
                     latex(b_pt), latex(c_pt), latex(delta),
                     latex(-b_pt), latex(delta), latex(w_ans), latex(2*h_cat),
                     latex(-b_pt), latex(delta), latex(w_loai),
                     latex(w_ans), latex(w_ans), latex(l_ans)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
