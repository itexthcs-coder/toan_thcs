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



def bt_dang14_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(12, 10, 8), (16, 12, 10), (20, 16, 10), (24, 14, 25)]
        W, d, R2 = random.choice(bo_so)
        half_W = Rational(W, 2)
        R_min = Rational(d, 2)
        half_d = Rational(d, 2)
        MH = sqrt(R2**2 - half_d**2)

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (-1.5,0);
\\coordinate (O2) at (1.5,0);
\\coordinate (H) at (0,0);
\\coordinate (M) at (0,1.6);
\\coordinate (N) at (0,-1.6);
\\draw[line width=1pt] (-4,-2.2) rectangle (4,2.2);
\\draw[line width=1pt, dashed] (-4,0)--(4,0);
\\draw[line width=1pt] (O1) circle (2.19cm);
\\draw[line width=1pt] (O2) circle (2.19cm);
\\draw[line width=1pt] (M)--(N) (O1)--(M);
\\fill (O1) circle (1pt) node[below left] {$O_1$};
\\fill (O2) circle (1pt) node[below right] {$O_2$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Một mảnh vườn hình chữ nhật có chiều rộng $%s\\text{ m}$. Người ta đặt hai vòi phun nước tự động xoay tròn $360^\\circ$ có cùng bán kính phun $R$ tại hai điểm $O_1, O_2$ nằm trên đường trung bình theo chiều dài của mảnh vườn. Biết hai vòi phun cách nhau $%s\\text{ m}$.\\\\
        a) Tìm bán kính phun $R$ để hai vùng tưới hình tròn tiếp xúc ngoài với nhau. Khi đó, phần diện tích theo chiều rộng mảnh vườn tại vị trí đặt vòi có được tưới hết không?\\\\
        b) Nếu điều chỉnh bán kính phun của mỗi vòi lên $R = %s\\text{ m}$, hãy chứng minh rằng hai giao điểm của hai đường tròn biên vùng tưới nằm hoàn toàn bên trong mảnh vườn. %s'''
                         % (latex(W), latex(d), latex(R2), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Để hai đường tròn vùng tưới $(O_1; R)$ và $(O_2; R)$ tiếp xúc ngoài với nhau thì khoảng cách hai tâm phải bằng tổng hai bán kính:\\\\
        $O_1O_2 = R + R \\Leftrightarrow 2R = %s \\Leftrightarrow R = %s\\text{ (m)}$.\\\\
        Vì $O_1, O_2$ nằm trên đường trung bình theo chiều dài mảnh vườn nên khoảng cách từ mỗi vòi phun đến hai mép chiều dài của vườn bằng một nửa chiều rộng mảnh vườn, tức là $\\frac{%s}{2} = %s\\text{ m}$.\\\\
        Do bán kính tưới $R = %s\\text{ m} < %s\\text{ m}$ nên nước chưa thể phun tới hai mép biên của mảnh vườn, vậy phần diện tích theo chiều rộng mảnh vườn tại vị trí đặt vòi chưa được tưới hết.
        \\item Khi điều chỉnh bán kính $R = %s\\text{ m}$, vì $R + R = %s\\text{ m} > %s\\text{ m}$ và $R - R = 0 < %s\\text{ m}$ nên hai đường tròn cắt nhau tại hai điểm phân biệt $M$ và $N$.\\\\
        Gọi $H$ là giao điểm của $O_1O_2$ và $MN$. Vì hai đường tròn bằng nhau nên $H$ là trung điểm của $O_1O_2$ và $O_1O_2 \\perp MN$ tại $H$.\\\\
        Ta có $O_1H = \\frac{O_1O_2}{2} = \\frac{%s}{2} = %s\\text{ m}$.\\\\
        Áp dụng định lí Pythagore vào tam giác vuông $O_1HM$, ta tính được khoảng cách từ $M$ và $N$ đến đường trung bình $O_1O_2$ là:\\\\
        $MH = NH = \\sqrt{O_1M^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (m)}$.\\\\
        Vì $MH = NH = %s\\text{ m} < %s\\text{ m}$ (khoảng cách từ đường trung bình đến hai mép vườn) nên hai giao điểm $M, N$ nằm hoàn toàn bên trong mảnh vườn.
        \\end{enumEX}'''
                   % (latex(d), latex(R_min), latex(W), latex(half_W),
                      latex(R_min), latex(half_W),
                      latex(R2), latex(2*R2), latex(d), latex(d),
                      latex(d), latex(half_d),
                      latex(R2), latex(half_d), latex(MH),
                      latex(MH), latex(half_W)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
