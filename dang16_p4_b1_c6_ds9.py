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


def bt_dang16_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [(20, Decimal('12.5'), Rational(1, 8), 6, Decimal('4.5'), Decimal('8.0')),
                 (20, Decimal('10'), Rational(1, 10), 6, Decimal('3.6'), Decimal('6.4')),
                 (16, Decimal('8'), Rational(1, 8), 4, Decimal('2.0'), Decimal('6.0'))]
        diam, depth, a_par, x_pt, y_pt, dist_rim = random.choice(cases)
        rad = diam // 2
        
        depth_str = str(depth).rstrip('0').rstrip('.').replace('.', ',')
        y_pt_str = str(y_pt).rstrip('0').rstrip('.').replace('.', ',')
        dist_str = str(dist_rim).rstrip('0').rstrip('.').replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Mặt cắt qua trục của một chóa đèn pha ô tô có dạng một đường parabol $y = ax^2$ ($a > 0$), trong đó đỉnh $O(0; 0)$ là vị trí đặt chân bóng đèn. Biết đường kính vành ngoài của chóa đèn là $%s$ cm và chiều sâu của chóa đèn (tính từ tâm vành ngoài đến đỉnh $O$) là $%s$ cm. \\\\
a) Chọn hệ trục tọa độ $Oxy$ sao cho trục $Oy$ là trục đối xứng của chóa đèn hướng về phía trước. Hãy xác định hệ số $a$ của parabol. \\\\
b) Một điểm sáng phản xạ $M$ trên thành chóa đèn cách trục đối xứng $%s$ cm thì nằm cách mặt phẳng chứa vành ngoài của chóa đèn bao nhiêu centimet?'''
                         %(latex(diam), depth_str, latex(x_pt)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $A$ và $B$ là hai điểm nằm trên vành ngoài của mặt cắt chóa đèn (với $B$ nằm bên phải trục $Oy$). \\\\
Vì đường kính vành ngoài là $%s$ cm nên bán kính vành ngoài là $\\frac{%s}{2} = %s$ cm. \\\\
Chiều sâu của chóa đèn là $%s$ cm nên tọa độ điểm $B$ là $(%s; %s)$. \\\\
Thay $x = %s$ và $y = %s$ vào phương trình $y = ax^2$, ta được: \\\\
$%s = a \\cdot %s^2 \\Rightarrow %sa = %s \\Rightarrow a = %s$. \\\\
Vậy hệ số cần tìm là $a = %s$.
\\item Điểm sáng $M$ trên thành chóa đèn cách trục đối xứng $Oy$ một khoảng $%s$ cm nên hoành độ của $M$ thỏa mãn $|x_M| = %s \\Rightarrow x_M^2 = %s$. \\\\
Tung độ của điểm $M$ là: \\\\
$y_M = %s \\cdot %s = %s$ (cm). \\\\
Khoảng cách từ điểm $M$ đến mặt phẳng chứa vành ngoài của chóa đèn là: \\\\
$%s - %s = %s$ (cm). \\\\
\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.6) -- (0,4.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.5:2.5] plot(\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2.5,3.125);
\\coordinate (B) at (2.5,3.125);
\\coordinate (I) at (0,3.125);
\\coordinate (M) at (1.5,1.125);
\\coordinate (H) at (1.5,3.125);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt, dashed] (M)--(H);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (M) circle (1pt) node[below right] {$M$};
\\fill (H) circle (1pt) node[above] {$H$};
\\end{tikzpicture}
\\end{center}
\\end{enumEX}'''
                   %(latex(diam), latex(diam), latex(rad),
                     depth_str, latex(rad), depth_str,
                     latex(rad), depth_str,
                     depth_str, latex(rad), latex(rad**2), depth_str, latex(a_par),
                     latex(a_par),
                     latex(x_pt), latex(x_pt), latex(x_pt**2),
                     latex(a_par), latex(x_pt**2), y_pt_str,
                     depth_str, y_pt_str, dist_str
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
