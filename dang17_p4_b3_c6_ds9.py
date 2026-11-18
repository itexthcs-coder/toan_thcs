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


def bt_dang17_p4_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        a0, b0, c0 = random.choice(triples)
        k = randint(4, 10)
        v1 = a0 * k
        v2 = b0 * k
        d_chim_bay = c0 * k
        S_tong = v1 + v2
        P_tich = v1 * v2
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai xe máy cùng xuất phát tại một ngã tư $O$ theo hai hướng vuông góc với nhau (xe thứ nhất đi về hướng Bắc, xe thứ hai đi về hướng Đông như hình vẽ). Sau $1$ giờ, khoảng cách đường chim bay giữa hai xe là $%s\\text{ km}$. Biết rằng tổng quãng đường hai xe đi được trong $1$ giờ đó là $%s\\text{ km}$ và xe đi về hướng Đông chạy nhanh hơn xe đi về hướng Bắc. Tính vận tốc của mỗi xe.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (0,2.5);
\\coordinate (B) at (3.5,0);
\\draw[line width=1pt, ->] (O)--(A);
\\draw[line width=1pt, ->] (O)--(B);
\\draw[line width=1pt, dashed] (A)--(B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$ (Bắc)};
\\fill (B) circle (1pt) node[below] {$B$ (Đông)};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(d_chim_bay), latex(S_tong)))
        
        # Nội dung lời giải
        loigiai = ('''Gọi vận tốc của xe đi về hướng Bắc là $v_{1}$ (km/h) và vận tốc của xe đi về hướng Đông là $v_{2}$ (km/h) (điều kiện: $v_{2} > v_{1} > 0$). \\\\
Sau $1$ giờ, quãng đường xe đi về hướng Bắc là $OA = v_{1}$ (km) và quãng đường xe đi về hướng Đông là $OB = v_{2}$ (km). \\\\
Theo giả thiết, tổng quãng đường hai xe đi được là $%s\\text{ km}$ nên $v_{1} + v_{2} = %s$. \\\\
Vì hai hướng đi vuông góc với nhau nên tam giác $OAB$ vuông tại $O$. Áp dụng định lí Pythagore, ta có: \\\\
$OA^{2} + OB^{2} = AB^{2} \\Leftrightarrow v_{1}^{2} + v_{2}^{2} = %s^{2} = %s$. \\\\
Mặt khác: $v_{1}^{2} + v_{2}^{2} = (v_{1} + v_{2})^{2} - 2v_{1}v_{2} \\Leftrightarrow %s^{2} - 2v_{1}v_{2} = %s \\Leftrightarrow v_{1}v_{2} = \\dfrac{%s - %s}{2} = %s$. \\\\
Khi đó, $v_{1}$ và $v_{2}$ là hai nghiệm của phương trình bậc hai: $x^{2} - %sx + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0 \\Rightarrow \\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt là $x_{1} = %s$ và $x_{2} = %s$. \\\\
Vì $v_{2} > v_{1} > 0$ nên $v_{1} = %s$ và $v_{2} = %s$. \\\\
Vậy vận tốc của xe đi về hướng Bắc là $%s\\text{ km/h}$ và vận tốc của xe đi về hướng Đông là $%s\\text{ km/h}$.'''
                   % (latex(S_tong), latex(S_tong),
                      latex(d_chim_bay), latex(d_chim_bay**2),
                      latex(S_tong), latex(d_chim_bay**2), latex(S_tong**2), latex(d_chim_bay**2), latex(P_tich),
                      latex(S_tong), latex(P_tich),
                      latex(S_tong), latex(P_tich), latex((v2 - v1)**2), latex(v2 - v1),
                      latex(v1), latex(v2),
                      latex(v1), latex(v2),
                      latex(v1), latex(v2)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
