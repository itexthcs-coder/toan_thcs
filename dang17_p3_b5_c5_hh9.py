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


def bt_dang17_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap_ban_kinh = [(9, 4), (16, 9), (25, 4), (16, 1), (18, 8), (36, 4)]
        R1, R2 = random.choice(cap_ban_kinh)
        MN = int(2 * math.sqrt(R1 * R2))
        kq_str = str(MN)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (1.5, 1.8);
\\coordinate (Op) at (4.33, 1.0);
\\coordinate (M) at (1.5, 0);
\\coordinate (N) at (4.33, 0);
\\coordinate (H) at (1.5, 1.0);
\\draw[line width=1pt] (0,0)--(6.0,0);
\\draw[line width=1pt] (O) circle (1.8cm);
\\draw[line width=1pt] (Op) circle (1.0cm);
\\draw[line width=1pt] (O)--(Op) (O)--(M) (Op)--(N);
\\draw[line width=1pt, dashed] (Op)--(H);
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (Op) circle (1pt) node[above] {$O'$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một con tàu đi thẳng từ cảng $A$ đến cảng $B$ theo một tuyến đường biển thẳng. Trên hải đồ, có hai bãi đá ngầm nguy hiểm có vùng ảnh hưởng dạng hình tròn cùng tiếp xúc với tuyến đường thẳng $AB$ về cùng một phía, với bán kính vùng nguy hiểm lần lượt là $%s\\text{ hải lí}$ và $%s\\text{ hải lí}$. Biết hai vùng nguy hiểm này tiếp xúc ngoài với nhau. Tính khoảng cách giữa hai tiếp điểm của hai vùng nguy hiểm trên tuyến đường $AB$ (đơn vị: $\\text{hải lí}$).\\\\
%s''' % (R1, R2, hinhve))

        loigiai = ('''Gọi $(O; %s)$ và $(O'; %s)$ là hai đường tròn biểu diễn hai vùng nguy hiểm, tiếp xúc với đường thẳng $AB$ lần lượt tại $M$ và $N$. \\\\
Vì hai vùng nguy hiểm tiếp xúc ngoài với nhau nên $OO' = R_1 + R_2 = %s + %s = %s\\text{ (hải lí)}$. \\\\
Vì đường thẳng $AB$ tiếp xúc với $(O)$ tại $M$ và tiếp xúc với $(O')$ tại $N$ nên $OM \\perp AB$ và $O'N \\perp AB$. \\\\
Kẻ $O'H \\perp OM$ tại $H$, ta được hình chữ nhật $MNO'H$, suy ra $MN = O'H$ và $MH = O'N = %s\\text{ hải lí}$. \\\\
Do đó $OH = OM - MH = %s - %s = %s\\text{ (hải lí)}$. \\\\
Áp dụng định lí Pythagore vào tam giác vuông $OHO'$, ta có: \\\\
$MN = O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (hải lí)}$.'''
                   % (R1, R2, R1, R2, R1 + R2, R2, R1, R2, R1 - R2, R1 + R2, R1 - R2, MN))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
