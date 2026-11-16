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


def bt_dang19_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        kc = random.choice([4, 5, 6])
        goc = 20
        rad = math.radians(goc)
        than_val = kc * math.tan(rad)
        ngon_val = kc / math.cos(rad)
        tong_val = than_val + ngon_val
        con_val = than_val - 0.5

        than_str = str(Decimal(str(than_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        ngon_str = str(Decimal(str(ngon_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        tong_str = str(Decimal(str(tong_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        con_str = str(Decimal(str(con_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (C) at (0,0);
    \\coordinate (A) at (4.2,0);
    \\coordinate (B) at (4.2,1.53);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt] (3.98,0)--(3.98,0.22)--(4.2,0.22);
    \\draw[line width=1pt] (0.7,0) arc (0:20:0.7);
    \\fill (A) circle (1pt) node[below right] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below left] {$C$};
    \\node[below] at (2.1,0) {$%s\\text{ m}$};
    \\node at (1.05,0.2) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (kc, goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Sau một trận bão lớn, một cây xanh mọc thẳng đứng bên đường bị gãy ngang thân tại $B$; phần ngọn cây đổ gục xuống chạm mặt đất tại $C$ cách gốc cây $A$ một đoạn $AC = %s\\text{ m}$. Biết gốc cây, điểm gãy và ngọn cây tạo thành một tam giác vuông và đoạn cây bị gãy $BC$ tạo với mặt đất một góc $%s^\\circ$ (như hình vẽ). \\\\
    a) Tính chiều cao của cây xanh đó trước khi bị bão đánh gãy (làm tròn kết quả đến hàng phần mười). \\\\
    b) Để phòng tránh nguy hiểm cho người đi đường, đội cây xanh quyết định cưa bỏ hoàn toàn phần ngọn cây bị gãy và hạ thấp phần thân đứng còn lại xuống thêm $0,5\\text{ m}$. Tính chiều cao phần thân cây còn giữ lại sau khi xử lý (làm tròn đến hàng phần mười).
    %s''' % (kc, goc, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $ABC$ vuông tại $A$, ta có:\\\\
    Chiều cao phần thân cây còn đứng thẳng là $AB = AC \\cdot \\tan C = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (m)}$.\\\\
    Độ dài phần ngọn cây bị gãy đổ là $BC = \\dfrac{AC}{\\cos C} = \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ (m)}$.\\\\
    Chiều cao của cây xanh trước khi bị bão đánh gãy là $h = AB + BC \\approx %s + %s \\approx %s\\text{ (m)}$.
    \\item Chiều cao phần thân cây còn giữ lại sau khi hạ thấp thêm $0,5\\text{ m}$ là:\\\\
    $h' = AB - 0,5 \\approx %s - 0,5 \\approx %s\\text{ (m)}$.
    \\end{enumEX}'''
                   % (kc, goc, than_str, kc, goc, ngon_str, than_str, ngon_str, tong_str,
                      than_str, con_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
